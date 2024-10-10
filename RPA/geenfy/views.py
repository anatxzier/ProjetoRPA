from django.shortcuts import render, redirect, get_object_or_404
from .models import Homepage, Login, NovaTurma, Cadastro, Lixeira, Processo, User, Funcionario, Usuario, Perfil, Cadastro_Info, PerfilEditar, In_progress_file, Finished_file
from .forms import FormLogin, FormNovaTurma, FormCadastro, FormCadastro_Info
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.core.cache import cache
import subprocess
import threading
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


def group_required(group_name):
     def in_group(user):
         if user.is_authenticated:
             return user.groups.filter(name=group_name).exists()
         return False
     return user_passes_test(in_group)

def Homepage_View (request):
    context = {}    
    dados_homepage = Homepage.objects.all()
    context["dados_homepage"] = dados_homepage
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador   
    return render(request, 'homepage.html', context)

def Login_View(request):


    context = {}
    dados_login = Login.objects.all()
    context["dados_login"] = dados_login

    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
            var_user = form.cleaned_data['user']  
            var_password = form.cleaned_data['password']
        
            user = authenticate(request, username=var_user, password=var_password)

            if user is not None:
                auth_login(request, user)

#logica apara redirecionamento 
                try:
                    usuario = Usuario.objects.get(user=user)
                    if usuario.login_CAF and usuario.login_IHX:  # Verifica se ambos os campos estão preenchidos
                        return redirect('novaturma')  # Redireciona se ambos estiverem preenchidos
                    else:
                        return redirect('cadinfo')  # Redireciona para cadinfo se algum campo estiver vazio
                except Usuario.DoesNotExist:
                    return redirect('cadinfo')  # Redireciona se o usuário não existir na tabela Usuario

#//



            else:
                context['error'] = "Usuário ou senha incorretos"
                context['form'] = form
                return render(request, "login.html", context)

    else:
        form = FormLogin()
        context['form'] = form
        return render(request, "login.html", context)

@login_required
def NovaTurma_View(request):
    context = {}
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    if request.method == 'POST':
        form = FormNovaTurma(request.POST, request.FILES)
        if form.is_valid():
            print("esse aqui 2")
            var_turma = form.cleaned_data['nome_da_turma']
            var_arquivo = form.cleaned_data['arquivo']
            arquivo_in_progress = In_progress_file(turma=var_turma,arquivo_inprogress=var_arquivo)
            arquivo_in_progress.save()
            return redirect('processo')
        else:
            context['error_message'] = 'Ocorreu um erro durante o processamento do formulário.'
            form = FormNovaTurma()
            context['form'] = form 
            return render(request, "novaTurma.html", context ) 
    else:
        form = FormNovaTurma()
        context["form"] = form
    return render(request, "novaTurma.html", context )

@login_required
@group_required('Coordenador')
def Cadastro_View(request):
    cache.clear()
    context = {}
    dados_cadastro = Cadastro.objects.all()
    context["dados_cadastro"] = dados_cadastro
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            try:
            
                var_first_name = form.cleaned_data['first_name']
                var_user = form.cleaned_data['user']
                var_email = form.cleaned_data['email']
                var_password = form.cleaned_data['password']
                

                if  User.objects.filter(username=var_user).exists():
                    print("Esse04")
                    context['error_message'] = 'Nome de usuário já existe, por favor tente novamente'
                    form = FormCadastro()
                    context['form'] = form
                    return render(request, "cadastro.html", context)
                
                else:
                    user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
                    user.first_name = var_first_name
                    user.save()
                    group = Group.objects.get(name='funcionario')
                    user.groups.add(group) 
                    # usuario = Usuario(user=user) 
                                
                    messages.success(request,"Cadastro feito com sucesso!")                    
                    return redirect('cadastro')
                
            except Exception as error:
                context['error_message'] = 'Ocorreu um erro durante o processamento do formulário.'
                form = FormCadastro()
                context['form'] = form                
                return redirect("cadastro")
            
        else:
            form = FormCadastro()
            context['form'] = form
            return render(request, "cadastro.html", context)
        
    else:
        form = FormCadastro()
        context['form'] = form
        return render(request, "cadastro.html", context)

@login_required
def Storage_View(request):
    context = {}
    dados_lixeira = Lixeira.objects.all()
    form = FormNovaTurma()
    context["form"] = form
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    dados_finalizados = Finished_file.objects.order_by('-upload_time')
    context ["dados_finalizados"] = dados_finalizados
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    context["dados_lixeira"] = dados_lixeira

    return render(request, "armazenamento.html", context)

@login_required
def Processo_View(request):
    context = {}
    dados_processo = Processo.objects.all()
    context ["dados_processo"] = dados_processo
    dados_progresso = In_progress_file.objects.all()
    context ["dados_progresso"] = dados_progresso
    # Pegando todos os arquivos finalizados e ordenando do mais recente para o mais antigo
    dados_finalizados = Finished_file.objects.order_by('-upload_time')[:5]
    context ["dados_finalizados"] = dados_finalizados
    form = FormNovaTurma()
    context["form"] = form
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    arquivo_em_progresso = In_progress_file.objects.filter(status="Em Progresso").exists()
    context["arquivo_em_progresso"] = arquivo_em_progresso

    return render(request, "processo.html", context)

# @login_required
# @group_required('Coordenador')
def Funcionario_View(request):
    context = {}
     # Obtenha o grupo de "Funcionário"
    grupo_funcionario = Group.objects.get(name="funcionario")
    # Filtra os usuários que pertencem ao grupo "Funcionário"
    dados_usuario = Usuario.objects.filter(user__groups=grupo_funcionario)
    context["dados_usuario"] = dados_usuario
    dados_funcionario = Funcionario.objects.all()
    context ["dados_funcionario"] = dados_funcionario
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador   

    return render(request, "funcionarios.html", context)




@login_required
def Perfil_View(request):
    context = {}
    dados_Perfil = Perfil.objects.all()
    context ['dados_Perfil'] = dados_Perfil
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    
    user = request.user
    
    # Definir o formulário independentemente de o perfil existir ou não
    form = FormNovaTurma(initial={
        'email': user.email,
        'user': user.username,
        'first_name': user.first_name,
        'password': '',  # Deixe a senha vazia no formulário
    })

    try:
        # Tentar obter o perfil do usuário autenticado
        usuario = Usuario.objects.get(user=request.user)
        context['usuario'] = usuario
    except Usuario.DoesNotExist:
        # Se o perfil não existir, passar uma mensagem de erro
        context['error'] = "O perfil do usuário não foi encontrado."
    
    # Adicionar o formulário ao contexto, independentemente do perfil existir ou não
    context['form'] = form
    return render(request, 'perfil.html', context)




@login_required
def Editar_Perfil_View(request):
    context = {}
    usuario = get_object_or_404(Usuario, user=request.user)
    user = request.user

    form1 = FormCadastro(initial={
        'email': user.email,
        'user': user.username,
        'first_name': user.first_name,
        'password': '', 
    })

    form2 = FormCadastro_Info(initial={
        'LoginIHX': usuario.login_IHX,
        'SenhaIHX': '',  
        'LoginCAF': usuario.login_CAF,
        'SenhaCAF': '', 
    })

    if request.method == "POST":
        form1 = FormCadastro(request.POST)
        form2 = FormCadastro_Info(request.POST)

        if form1.is_valid() and form2.is_valid():
            # Atualizando dados do User
            user.email = form1.cleaned_data['email']
            user.username = form1.cleaned_data['user']
            user.first_name = form1.cleaned_data['first_name']
            password = form1.cleaned_data.get('password')

            # Se a senha foi preenchida, atualiza, senão mantém a senha atual
            if password:
                user.set_password(password)

        
            usuario.login_CAF = form2.cleaned_data['LoginCAF']
            usuario.senha_CAF = form2.cleaned_data['SenhaCAF']
            usuario.login_IHX = form2.cleaned_data['LoginIHX']
            usuario.senha_IHX = form2.cleaned_data['SenhaIHX']

    
            user.save()
            usuario.save()

            update_session_auth_hash(request, user)

            return redirect('perfil')
        else:
            
            print("Erros do Form1:", form1.errors)
            print("Erros do Form2:", form2.errors)

    # Sempre retornar a resposta, seja na requisição GET ou se os formulários forem inválidos
    context['form1'] = form1
    context['form2'] = form2
    return render(request, 'editar_perfil.html', context)







@login_required
def Cadastro_Info_View(request):
    context = {}
    dados_CadInfo = Cadastro_Info.objects.all()
    context["dados_CadInfo"] = dados_CadInfo

    #tratar erro de o msm user inserir info 2 vezes

    if request.method == 'POST':
        form = FormCadastro_Info(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                user = request.user
            usuario = get_object_or_404(Usuario, user=user)    
            usuario.login_CAF=form.cleaned_data['LoginCAF']
            usuario.senha_CAF=form.cleaned_data['SenhaCAF']
            usuario.login_IHX=form.cleaned_data['LoginIHX']
            usuario.senha_IHX=form.cleaned_data['SenhaIHX']
            usuario.save() 
            return redirect('novaturma')  
    else:
        form = FormCadastro_Info()  

    context["form"] = form  
    return render(request, "cad_info.html", context)



def excluir_funcionario(request):
    if request.method == 'POST':
        funcionario_id = request.POST.get('funcionario_id')
        funcionario = get_object_or_404(User, id=funcionario_id)
        funcionario_usuario = get_object_or_404(Usuario, user=funcionario)
        funcionario_usuario.delete()
        funcionario.delete()
        return redirect('funcionarios')
    else:
        return redirect('funcionarios')

def excluir_file(request):
    if request.method == 'POST':
        file_status = request.POST.get('file_status')
        file_id = request.POST.get('file_id')
        if file_status == 'Pendente': 
            in_progress_file = get_object_or_404(In_progress_file, id=file_id)
            in_progress_file.delete()
        else:
            finished_file = get_object_or_404(Finished_file, id=file_id)
            finished_file.delete()     
        return redirect('processo')
    else:
        return redirect('processo')



def logout(request):
    auth_logout(request)
    return redirect("home")




def executar_script_async(login_IHX, senha_IHX, login_CAF, senha_CAF, nome_turma, id_arquivo, caminho_arquivo_inprogress):
    # Caminho para o interpretador Python
    python_path = r"C:\Users\Aluno\AppData\Local\Programs\Python\Python312\python.exe"
    
    # Caminho para o script Python que você quer executar
    script_path = r"C:\Users\Aluno\Documents\Test_tcc\test_terminal.py"

    # Executa o script com os argumentos necessários
    subprocess.run([python_path, script_path, login_IHX, senha_IHX, login_CAF, senha_CAF, nome_turma, id_arquivo, caminho_arquivo_inprogress])

def executar_script(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        file = get_object_or_404(In_progress_file, id=file_id)
        file.status = 'Em Progresso'
        file.save()

        # Obtendo os dados do usuário logado
        usuario = get_object_or_404(Usuario, user=request.user)
        login_IHX = usuario.login_IHX
        senha_IHX = usuario.senha_IHX
        login_CAF = usuario.login_CAF
        senha_CAF = usuario.senha_CAF

        # Obtendo o nome da turma associada ao arquivo em progresso
        nome_turma = file.turma  # Assumindo que 'turma' é o campo que contém o nome da turma
        id_arquivo = file_id
        # Obtendo o caminho do arquivo em progresso
        caminho_arquivo_inprogress = file.arquivo_inprogress.path

        # Inicia o script em uma thread separada com os dados do usuário, nome da turma e o caminho do arquivo
        thread = threading.Thread(target=executar_script_async, args=(login_IHX, senha_IHX, login_CAF, senha_CAF, nome_turma, id_arquivo, caminho_arquivo_inprogress))
        thread.start()

        # Retorna uma resposta imediata ao usuário
        return redirect('processo')
    else:
        return redirect('processo')


