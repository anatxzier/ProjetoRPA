from django.urls import path
from . import views

# URLs para as views do aplicativo, associando caminhos a funções específicas
urlpatterns = [
    path ('', views.Homepage_View, name="home"),
    path('login', views.Login_View, name="login"),
    path('logout', views.logout, name="logout"),
    path('novaturma', views.NovaTurma_View, name="novaturma"),
    path('cadastro', views.Cadastro_View, name="cadastro"),
    path('storage', views.Storage_View, name="storage"),
    path('processo', views.Processo_View, name="processo"),
    path('funcionarios', views.Funcionario_View, name="funcionarios"),
    path('perfil', views.Perfil_View, name='perfil'),
    path('cadinfo', views.Cadastro_Info_View, name='cadinfo'),
    path('editarperfil', views.Editar_Perfil_View, name='editarperfil'),
    path('excluir_funcionario', views.excluir_funcionario, name='excluir_funcionario'),
    path('excluir_file', views.excluir_file, name='excluir_file'),
    path('executar-script', views.executar_script, name='executar_script')
]
