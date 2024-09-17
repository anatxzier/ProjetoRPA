from django.shortcuts import render, redirect
from .models import Homepage, Login, NovaTurma, Cadastro, Lixeira, Processo, User, Funcionario, Usuario
from .forms import FormLogin, FormNovaTurma, FormCadastro
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.core.cache import cache
import subprocess
import threading
from django.http import HttpResponse
from django.contrib import messages


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
                return redirect('home')
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
    form = FormNovaTurma()
    context["form"] = form
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    if request.method == 'POST':
        form = FormNovaTurma(request.POST, request.FILES)
        if form.is_valid():
            # Processa o arquivo (por exemplo, salvar ou manipular)
            pass
    else:
        form = FormNovaTurma()
#configurar upload de arquivos
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
def Lixeira_View(request):
    context = {}
    dados_lixeira = Lixeira.objects.all()
    form = FormNovaTurma()
    context["form"] = form
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 
    context["dados_lixeira"] = dados_lixeira

    return render(request, "lixeira.html", context)

@login_required
def Processo_View(request):
    context = {}
    dados_processo = Processo.objects.all(),
    context ["dados_processo"] = dados_processo
    form = FormNovaTurma()
    context["form"] = form
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador 

    return render(request, "processo.html", context)

# @login_required
# @group_required('Coordenador')
def Funcionario_View(request):
    context = {}
    dados_usuario = Usuario.objects.all()
    context ["dados_usuario"] = dados_usuario
    dados_funcionario = Funcionario.objects.all()
    context ["dados_funcionario"] = dados_funcionario
    user_is_Coordenador = request.user.groups.filter(name="Coordenador").exists() if request.user.is_authenticated else False
    context["user_is_Coordenador"] = user_is_Coordenador   

    return render(request, "funcionarios.html", context)


def logout(request):
    auth_logout(request)
    return redirect("home")




def executar_script_async():
    # Caminho para o interpretador Python
    python_path = r"C:\Users\Aluno\AppData\Local\Programs\Python\Python312\python.exe"
    
    # Caminho para o script Python que você quer executar
    script_path = r"C:\Users\Aluno\Documents\Test_tcc\test_terminal.py"
    
    # Executa o script com o interpretador Python
    subprocess.run([python_path, script_path])

def executar_script(request):
    # Inicia o script em uma thread separada
    thread = threading.Thread(target=executar_script_async)
    thread.start()

    # Retorna uma resposta imediata ao usuário
    return HttpResponse("O script foi iniciado e está sendo executado em segundo plano.")

