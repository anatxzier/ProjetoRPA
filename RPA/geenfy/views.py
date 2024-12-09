from django.shortcuts import render, redirect, get_object_or_404
from .models import Homepage, Login, NovaTurma, Cadastro, Storage, Processo, User, Funcionario, Usuario, Perfil, Cadastro_Info, PerfilEditar, In_progress_file, Finished_file, ErrorLog
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


# Função para verificar se o usuário pertence a um grupo específico
def group_required(group_name):
    def in_group(user):
        if user.is_authenticated:
            return user.groups.filter(name=group_name).exists()  # Verifica se o usuário está no grupo
        return False
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or not request.user.groups.filter(name=group_name).exists():
                return redirect('home') # Redireciona para a página inicial se o usuário não estiver no grupo
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# Função para renderizar a página inicial
def Homepage_View (request):
    context = {}    
    dados_homepage = Homepage.objects.all()  # Busca todos os dados para a página inicial
    context["dados_homepage"] = dados_homepage
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador   
    return render(request, 'homepage.html', context) # Renderiza o template da página inicial com o contexto

# Função para tratar a funcionalidade de login
def Login_View(request):
    context = {}
    dados_login = Login.objects.all() # Busca todos os dados de login
    context["dados_login"] = dados_login

    if request.method == "POST":
        form = FormLogin(request.POST) # Processa o envio do formulário
        if form.is_valid():
            var_user = form.cleaned_data['user']  
            var_password = form.cleaned_data['password']
            user = authenticate(request, username=var_user, password=var_password) # Autentica o usuário
            if user is not None:
                auth_login(request, user) # Faz o login do usuário
                # Lógica para redirecionar para a página correta, dependendo do status do usuário
                try:
                    usuario = Usuario.objects.get(user=user)
                    if usuario.login_CAF and usuario.login_IHX and usuario.senha_CAF and usuario.senha_IHX:  # Verifica se ambos os campos estão preenchidos
                        return redirect('novaturma')  # Redireciona se ambos estiverem preenchidos
                    else:
                        return redirect('cadinfo')  # Redireciona para cadinfo se algum campo estiver vazio
                except Usuario.DoesNotExist:
                    return redirect('cadinfo')  # Redireciona se o usuário não existir na tabela Usuario
            else:
                context['error'] = "Usuário ou senha incorretos"  # Se a autenticação falhar, exibe mensagem de erro
                context['form'] = form
                return render(request, "login.html", context) # Retorna ao template de login com mensagem de erro

    else:
        form = FormLogin() # Caso a requisição não seja POST, cria um formulário vazio
        context['form'] = form
        return render(request, "login.html", context) # Retorna ao template de login com o formulário vazio
//
@login_required
def NovaTurma_View(request):
    context = {}
    dados_NovaTurma = NovaTurma.objects.all() # Busca todos os registros da tabela NovaTurma para exibir na página
    context["dados_NovaTurma"] = dados_NovaTurma
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    if request.method == 'POST': # Verifica se a requisição é do tipo POST (quando o formulário é enviado)
        form = FormNovaTurma(request.POST, request.FILES)
        if form.is_valid(): # Verifica se o formulário é válido
            varescolha = request.POST.get('user_choice')
            var_turma = form.cleaned_data['nome_da_turma']
            var_arquivo = form.cleaned_data['arquivo']
            # Cria um objeto 'In_progress_file' e o salva no banco de dados
            arquivo_in_progress = In_progress_file(turma=var_turma,arquivo_inprogress=var_arquivo)
            arquivo_in_progress.save()

            # Redireciona dependendo da escolha do usuário
            if varescolha == "não":
                return redirect('processo')
            else:
                form = FormNovaTurma()
                context['form'] = form 
                return render(request, "novaTurma.html", context ) 
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
    dados_cadastro = Cadastro.objects.all() # Busca todos os registros da tabela Cadastro
    context["dados_cadastro"] = dados_cadastro
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    # Verifica se a requisição é do tipo POST (quando o formulário de cadastro é enviado)
    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            try:
                # Obtém os dados preenchidos no formulário
                var_first_name = form.cleaned_data['first_name']
                var_user = form.cleaned_data['user']
                var_email = form.cleaned_data['email']
                var_password = form.cleaned_data['password']

                # Verifica se o nome de usuário já existe
                if User.objects.filter(username=var_user).exists():
                    context['error_message'] = 'Nome de usuário já existe, por favor tente novamente'
                    form = FormCadastro()
                    context['form'] = form
                    return render(request, "cadastro.html", context)
                    
                # Cria o usuário no banco de dados
                user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
                user.first_name = var_first_name
                user.save()
                # Adiciona o usuário ao grupo 'funcionario'
                group = Group.objects.get(name='funcionario')
                user.groups.add(group)

                messages.success(request, "Cadastro feito com sucesso!")
                return redirect('cadastro')
                
            except Exception as error:
                context['error_message'] = 'Ocorreu um erro durante o processamento do formulário.'
                form = FormCadastro()
                context['form'] = form
                return render(request, "cadastro.html", context)
        else:
            context['form'] = form
            return render(request, "cadastro.html", context)

    else:
        form = FormCadastro()
        context['form'] = form
        return render(request, "cadastro.html", context)

@login_required
def Storage_View(request):
    context = {}
    # Busca todos os registros das tabelas necessárias para exibir os dados
    dados_storage = Storage.objects.all()
    form = FormNovaTurma()
    context["form"] = form
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    dados_finalizados = Finished_file.objects.order_by('-upload_time')
    context ["dados_finalizados"] = dados_finalizados
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    context["dados_lixeira"] = dados_storage

    return render(request, "armazenamento.html", context)
//
@login_required
def Processo_View(request):
    context = {}
    # Busca todos os registros da tabela Processo e adiciona ao contexto
    dados_processo = Processo.objects.all()
    context ["dados_processo"] = dados_processo
    # Busca todos os registros de arquivos em progresso
    dados_progresso = In_progress_file.objects.all()
    context ["dados_progresso"] = dados_progresso
    # Busca os arquivos finalizados e os ordena do mais recente para o mais antigo, limitando a 5 registros
    dados_finalizados = Finished_file.objects.order_by('-upload_time')[:5]
    context ["dados_finalizados"] = dados_finalizados
    # Cria uma instância do formulário de NovaTurma
    form = FormNovaTurma()
    context["form"] = form
    # Busca os dados de NovaTurma
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    # Verifica se existe algum arquivo em progresso
    arquivo_em_progresso = In_progress_file.objects.filter(status="Em Progresso").exists()
    context["arquivo_em_progresso"] = arquivo_em_progresso
    # Obtém o primeiro erro registrado na tabela ErrorLog
    erro = ErrorLog.objects.first()
    context["erro"] = erro

    # Renderiza a página de processo com todos os dados no contexto
    return render(request, "processo.html", context)

@login_required
@group_required('Coordenador')
def Funcionario_View(request):
    context = {}
     # Obtenha o grupo de "Funcionário"
    grupo_funcionario = Group.objects.get(name="funcionario")
    # Filtra os usuários que pertencem ao grupo "Funcionário"
    dados_usuario = Usuario.objects.filter(user__groups=grupo_funcionario)
    context["dados_usuario"] = dados_usuario
    # Busca todos os registros da tabela Funcionario
    dados_funcionario = Funcionario.objects.all()
    context ["dados_funcionario"] = dados_funcionario
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador   

    # Renderiza a página de funcionários com os dados no contexto
    return render(request, "funcionarios.html", context)




@login_required
def Perfil_View(request):
    context = {}
    # Busca todos os registros da tabela Perfil
    dados_Perfil = Perfil.objects.all()
    context ['dados_Perfil'] = dados_Perfil
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    # Obtém o usuário atual
    user = request.user
    
    # Define o formulário com os dados do usuário
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
    # Renderiza a página de perfil com os dados no contexto
    return render(request, 'perfil.html', context)


//

@login_required
def Editar_Perfil_View(request):
    context = {}
    # Recupera todos os dados relacionados à edição de perfil
    dados_EditarPerfil = PerfilEditar.objects.all()
    context['dados_EditarPerfil'] = dados_EditarPerfil
    # Obtém o objeto 'Usuario' correspondente ao usuário autenticado
    usuario = get_object_or_404(Usuario, user=request.user)
    # Verifica se o usuário pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    user = request.user

    # Inicializa os formulários com o modo de edição
    form1 = FormCadastro(initial={
        'email': user.email,
        'user': user.username,
        'first_name': user.first_name,
        'password': '',  # Senha em branco
        'new_password': ''  # Campo para nova senha
    }, is_editing=True)

    form2 = FormCadastro_Info(initial={
        'LoginIHX': usuario.login_IHX,
        'SenhaIHX': '',  
        'LoginCAF': usuario.login_CAF,
        'SenhaCAF': '', 
    }, is_editing=True)

    if request.method == "POST":  # Verifica se a requisição é POST (envio de formulário)
        # Recarrega os formulários com os dados enviados pelo usuário
        form1 = FormCadastro(request.POST, is_editing=True)
        form2 = FormCadastro_Info(request.POST, is_editing=True)

        # Valida os formulários
        if form1.is_valid() and form2.is_valid():
            senha_geenfy = form1.cleaned_data.get('password')  # Captura a senha fornecida
            new_password = form1.cleaned_data.get('new_password')  # Captura a nova senha

            # Verifica se a senha atual foi fornecida
            if not senha_geenfy:  # Verifica se o campo senha_geenfy está vazio
                context['password_error'] = "O campo da senha GEENFY não pode estar vazio."
                context['modal_open'] = True  # Flag para manter a modal aberta
            elif senha_geenfy and not user.check_password(senha_geenfy):
                # Senha GEENFY incorreta, manter a modal aberta
                context['password_error'] = "Senha GEENFY incorreta."
                context['modal_open'] = True  # Flag para manter a modal aberta
            else:
                # Atualiza dados do User se a senha for correta
                user.email = form1.cleaned_data['email']
                user.username = form1.cleaned_data['user']
                user.first_name = form1.cleaned_data['first_name']


                # Verifica se uma nova senha foi fornecida e se é diferente da senha atual
                if new_password and new_password == senha_geenfy:
                    context['new_password_error'] = "A nova senha deve ser diferente da senha atual."
                    context['modal_open'] = True  # Manter modal aberta se houver erro de nova senha
                elif new_password:  # Se a nova senha for válida, atualiza a senha do usuário
                    user.set_password(new_password)

                # Somente atualiza se não houver erros
                if not context.get('password_error') and not context.get('new_password_error'):
                    # Atualiza os dados do modelo Usuario
                    usuario.login_CAF = form2.cleaned_data['LoginCAF']
                    usuario.senha_CAF = form2.cleaned_data['SenhaCAF']
                    usuario.login_IHX = form2.cleaned_data['LoginIHX']
                    usuario.senha_IHX = form2.cleaned_data['SenhaIHX']

                    # Salva as alterações no banco de dados
                    user.save()
                    usuario.save()

                    # Atualiza a sessão com a nova senha
                    update_session_auth_hash(request, user)

                    return redirect('perfil')  # Redireciona para a tela de perfil
        else:
            # Se os formulários não forem válidos, capture os erros
            context['form1_errors'] = form1.errors
            context['form2_errors'] = form2.errors

    context['form1'] = form1
    context['form2'] = form2
    return render(request, 'editar_perfil.html', context)






@login_required
def Cadastro_Info_View(request):
    context = {}
    # Recupera todos os dados de Cadastro_Info para exibição
    dados_CadInfo = Cadastro_Info.objects.all()
    context["dados_CadInfo"] = dados_CadInfo
    # Verifica se o usuário autenticado pertence ao grupo "Coordenador"
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

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


@login_required
@group_required('Coordenador')
def excluir_funcionario(request):
    if request.method == 'POST': # Verifica se a requisição é POST (confirmação de exclusão)
        funcionario_id = request.POST.get('funcionario_id') # Obtém o ID do funcionário enviado no formulário
        # Busca o objeto User correspondente ao ID fornecido
        funcionario = get_object_or_404(User, id=funcionario_id)
        # Busca o objeto Usuario relacionado ao User
        funcionario_usuario = get_object_or_404(Usuario, user=funcionario)
        funcionario_usuario.delete() # Exclui o objeto Usuario
        funcionario.delete() # Exclui o objeto User
        return redirect('funcionarios')
    else:
        return redirect('funcionarios')

//


def excluir_file(request):
    # Verifica se a requisição é do tipo POST
    if request.method == 'POST':
        # Obtém os dados enviados pelo formulário
        file_status = request.POST.get('file_status') # Status do arquivo ("Pendente" ou outro)
        file_id = request.POST.get('file_id') # ID do arquivo a ser excluído
        rota = request.POST.get('rota') # Rota para redirecionamento após a exclusão
        # Verifica o status do arquivo para determinar o modelo a ser usado
        if file_status == 'Pendente': 
            # Exclui um arquivo em progresso (In_progress_file)
            in_progress_file = get_object_or_404(In_progress_file, id=file_id)
            in_progress_file.delete()
        else:
            # Exclui um arquivo finalizado (Finished_file)
            finished_file = get_object_or_404(Finished_file, id=file_id)
            finished_file.delete()
        # Redireciona para a rota apropriada com base no valor de 'rota'
        if rota == 'processo':     
            return redirect('processo')
        else:
            return redirect('storage')
    else:
        # Redireciona para a página "processo" se a requisição não for POST
        return redirect('processo')



def logout(request):
    # Realiza o logout do usuário autenticado
    auth_logout(request)
    # Redireciona para a página inicial após o logout
    return redirect("home")




def executar_script_async(login_IHX, senha_IHX, login_CAF, senha_CAF, nome_turma, id_arquivo, caminho_arquivo_inprogress):
    try:
        # Caminho para o interpretador Python
        python_path = r"/usr/bin/python3"
        
        # Caminho para o script Python que você quer executar
        script_path = r"/home/instrutor/Documents/repositorio/Test_tcc/test_terminal.py"

        # Executa o script com os argumentos necessários
        resultado = subprocess.run(
            [python_path, script_path, login_IHX, senha_IHX, login_CAF, senha_CAF, nome_turma, id_arquivo, caminho_arquivo_inprogress],
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
            
        ErrorLog.objects.all().delete()  # Deleta todos os registros de erro

    except Exception as e:
        mensagem_erro = f"Algo de errado aconteceu com a turma {nome_turma}. Verifique:\n" \
                    "- Se as informações de login do CAF e IHX estão corretas;\n" \
                    "- Se o Excel está no formato correto;\n" \
                    "- Se os alunos estão corretamente cadastrados no sistema."

         # Remove qualquer erro existente antes de criar um novo
        ErrorLog.objects.all().delete()  # Deleta todos os registros de erro, mantendo apenas um
        error = ErrorLog.objects.create(mensagem=mensagem_erro)
        error.save()
        # Atualiza o status do arquivo para 'Pendente' em caso de erro
        file = In_progress_file.objects.get(id=id_arquivo)
        file.status = 'Pendente'
        file.save()


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
        thread = threading.Thread(
            target=executar_script_async, 
            args=(login_IHX, senha_IHX, login_CAF, senha_CAF, nome_turma, id_arquivo, caminho_arquivo_inprogress))
        thread.start()

        # Retorna uma resposta imediata ao usuário
        return redirect('processo')
    else:
        return redirect('processo')


