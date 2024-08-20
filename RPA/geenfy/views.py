from django.shortcuts import render
from .models import Homepage, Login, NovaTurma
from .forms import FormLogin

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
    context = {}
    dados_NovaTurma = NovaTurma.objects.all()
    context["dados_NovaTurma"] = dados_NovaTurma

    return render(request, "NovaTurma.html", context)
