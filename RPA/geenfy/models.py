from django.db import models  # Importa o módulo models do Django para criar as classes de modelo.
from django.contrib.auth.models import User  # Importa o modelo User, para associar um usuário do Django a um modelo.
from django.contrib.auth.models import AbstractUser  # Importa o AbstractUser, que pode ser usado para customizar o modelo de usuário.

# Definição de status para arquivos em progresso
PENDING = 'Pendente'
IN_PROGRESS = 'Em Progresso'
STATUS_CHOICES = [
    (PENDING, 'Pendente'), 
    (IN_PROGRESS, 'Em Progresso'),    
]

# Modelo Homepage - Define a estrutura da página inicial
class Homepage(models.Model):
    titulo = models.CharField(max_length=55)  # Título da homepage.
    texto = models.CharField(max_length=200)  # Texto descritivo da homepage.
    imagem = models.ImageField(upload_to="imgHome/")  # Imagem para a homepage.

    def __str__(self):  # Representação da instância como string (título da homepage).
        return self.titulo

# Modelo Login - Define o login com imagem
class Login(models.Model):
    titulo = models.CharField(max_length=55)  # Título da seção de login.
    imgLogin = models.ImageField(upload_to="imgLogin/")  # Imagem para a seção de login.

    def __str__(self):  # Representação da instância como string (título do login).
        return self.titulo
    
# Modelo NovaTurma - Define a página de criação de novas turmas
class NovaTurma(models.Model):
    titulo = models.CharField(max_length=55)  # Título da página de nova turma.
    texto = models.CharField(max_length=100)  # Texto explicativo sobre a nova turma.
    imgNovaTurma = models.ImageField(upload_to="imgNovaTurma/")  # Imagem para a página de nova turma.

    def __str__(self):  # Representação da instância como string (título da nova turma).
        return self.titulo

# Modelo Cadastro - Define a página de cadastro
class Cadastro(models.Model):
    titulo = models.CharField(max_length=55)  # Título da página de cadastro.
    imgCadastro = models.ImageField(upload_to="imgCadastro/")  # Imagem para a página de cadastro.

# Modelo Storage - Representa armazenamento de dados com um título
class Storage(models.Model):
    titulo = models.CharField(max_length=55)  # Título para o armazenamento.

# Modelo Processo - Representa um processo com um título
class Processo(models.Model):
    titulo = models.CharField(max_length=55)  # Título do processo.

# Modelo Usuario - Define a relação com o modelo User do Django e informações adicionais de login
class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relaciona com o modelo User.
    login_IHX = models.CharField(max_length=30)  # Login IHX.
    senha_IHX = models.CharField(max_length=30)  # Senha IHX.
    login_CAF = models.CharField(max_length=30)  # Login CAF.
    senha_CAF = models.CharField(max_length=30)  # Senha CAF.

# Modelo In_progress_file - Representa arquivos que estão em progresso
class In_progress_file(models.Model):
    turma =  models.CharField(max_length=20)  # Nome da turma.
    arquivo_inprogress = models.FileField(upload_to='in_progress_files/')  # Arquivo em progresso.
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=PENDING)  # Status do arquivo (Pendente ou Em Progresso).
    upload_time = models.DateTimeField(auto_now_add=True)  # Data e hora de upload.

# Modelo Finished_file - Representa arquivos que foram finalizados
class Finished_file(models.Model):
    turma =  models.CharField(max_length=20)  # Nome da turma.
    arquivo_fineshed = models.FileField(upload_to='finished_files/')  # Arquivo finalizado.
    upload_time = models.DateTimeField(auto_now_add=True)  # Data e hora de upload.

# Modelo Funcionario - Define informações sobre funcionários
class Funcionario(models.Model):
    titulo = models.CharField(max_length=55)  # Título para a seção de funcionários.
    imgFuncionarios = models.ImageField(upload_to="imgFuncionarios/")  # Imagem para a seção de funcionários.

# Modelo Perfil - Representa o perfil de um usuário ou página
class Perfil(models.Model):
    titulo = models.CharField(max_length=55)  # Título para a seção de perfil.
    imgPerfil = models.ImageField(upload_to="imgPerfil/")  # Imagem para o perfil.

# Modelo PerfilEditar - Representa uma seção de edição de perfil
class PerfilEditar(models.Model):
    titulo = models.CharField(max_length=55)  # Título para a edição do perfil.
    imgPerfil = models.ImageField(upload_to="imgPerfilEditar/")  # Imagem para a edição do perfil.

# Modelo Cadastro_Info - Define informações adicionais de cadastro
class Cadastro_Info(models.Model):
    titulo = models.CharField(max_length=55)  # Título para a seção de informações de cadastro.
    imgInfo = models.ImageField(upload_to="imgInfo/")  # Imagem para informações de cadastro.

# Modelo ErrorLog - Para armazenar logs de erro
class ErrorLog(models.Model):
    mensagem = models.TextField()  # Mensagem de erro.
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data e hora da criação do log de erro.
