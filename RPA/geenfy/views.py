from django.shortcuts import render, redirect, get_object_or_404
from .models import Homepage, Login, NovaTurma, Cadastro, Lixeira, Processo, User
from .forms import FormLogin, FormNovaTurma, FormCadastro
from django.contrib.auth.models import User, Group

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.core.cache import cache

def Homepage_View (request):
    context = {}

    dados_homepage = Homepage.objects.all()
    context["dados_homepage"] = dados_homepage
    return render(request, 'homepage.html', context)

def Login_View(request):
    context = {}
    dados_login = Login.objects.all()
    context["dados_login"] = dados_login

    if request.method == "POST":
        form = FormLogin(request.POST)
        if form.is_valid():
                var_email = form.cleaned_data['email']
                var_senha = form.cleaned_data['senha']

                user = authenticate(email=var_email, senha=var_senha)
                
                if user is not None:
                    auth_login(request, user)
                    
                    return redirect('homepage')
                else:
                    form = FormLogin()
                    context['form'] = form
                    context['error'] = "Usuário ou senha incorretas"
                    return render(request, "login.html", context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FormLogin()
        context['form'] = form
        # Vou redenrizar o que foi criado no arquivo forms
        return render(request, "login.html", context)


def NovaTurma_View(request):
    form = FormNovaTurma()
    context = {
        'dados_NovaTurma': NovaTurma.objects.all(),
        'form': form
    }
    if request.method == 'POST':
        form = FormNovaTurma(request.POST, request.FILES)
        if form.is_valid():
            # Processa o arquivo (por exemplo, salvar ou manipular)
            pass
    else:
        form = FormNovaTurma()
#configurar upload de arquivos
    return render(request, "novaTurma.html", context )

#
#@group_required('Coordenador')
def Cadastro_View(request):
    cache.clear()
    context = {}
    dados_cadastro = Cadastro.objects.all()
    context["dados_cadastro"] = dados_cadastro

    if request.method == 'POST':
        form = FormCadastro(request.POST)
        if form.is_valid():
            
            try:
            
                var_first_name = form.cleaned_data['first_name']
                var_user = form.cleaned_data['user']
                var_email = form.cleaned_data['email']
                var_password = form.cleaned_data['password']
                

                if  User.objects.filter(username=var_user).exists():
                    context['error_message'] = 'Nome de usuario já existe, por favor tente novamente'
                    form = FormCadastro()
                    context['form'] = form
                    return render(request, "cadastro.html", context)
                else:
                    
                    user = User.objects.create_user(username=var_user, email=var_email, password=var_password)
                    user.first_name = var_first_name
                    user.save()
                    group = Group.objects.get(name='funcionario')
                    user.groups.add(group)
                    
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


def Lixeira_View(request):
    context = {}
    dados_lixeira = Lixeira.objects.all()
    form = FormNovaTurma()
    context = {
        'dados_NovaTurma': NovaTurma.objects.all(),
        'form': form
    }
    context["dados_lixeira"] = dados_lixeira

    return render(request, "lixeira.html", context)

def Processo_View(request):
    context = {}
    dados_processo = Processo.objects.all(),
    context ["dados_processo"] = dados_processo
    form = FormNovaTurma()
    context = {
        'dados_NovaTurma': NovaTurma.objects.all(),
        'form': form
    }

    return render(request, "processo.html", context)