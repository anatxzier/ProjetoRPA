from django.shortcuts import render
from .models import Homepage, Login
from .forms import FormLogin

def Homepage_View (request):
    context = {}

    dados_homepage = Homepage.objects.all()
    context["dados_homepage"] = dados_homepage
    return render(request, 'homepage.html', context)

def login(request):
    context = {}
    dados_login = Login.objects.all()
    context["dados_login"] = dados_login

    return render(request, "login.html", context)