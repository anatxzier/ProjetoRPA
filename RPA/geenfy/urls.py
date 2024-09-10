from django.urls import path
from . import views

urlpatterns = [
    path ('', views.Homepage_View, name="home"),
    path('login', views.Login_View, name="login"),
    path('novaturma', views.NovaTurma_View, name="novaturma"),
    path('cadastro', views.Cadastro_View, name="cadastro"),
    path('lixeira', views.Lixeira_View, name="lixeira"),
    path('processo', views.Processo_View, name="processo"),
    path('funcionarios', views.Funcionario_View, name="funcionarios"),
]