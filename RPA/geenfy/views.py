from django.shortcuts import render
from .models import Homepage, Login, NovaTurma
from .forms import FormLogin, FormNovaTurma

def Homepage_View (request):
    context = {}

    dados_homepage = Homepage.objects.all()
    context["dados_homepage"] = dados_homepage
    return render(request, 'homepage.html', context)

def Login_View(request):
    context = {}
    dados_login = Login.objects.all()
    context["dados_login"] = dados_login

    return render(request, "login.html", context)

def NovaTurma_View(request):
    form = FormNovaTurma()
    context = {
        'dados_NovaTurma': NovaTurma.objects.all(),
        'form': form
    }
#configurar upload de arquivos
    return render(request, "novaTurma.html", context )
