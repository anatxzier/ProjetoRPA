from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Homepage(models.Model):
    titulo = models.CharField(max_length=55)
    texto = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to="imgHome/")

    def __str__(self):
        return self.titulo
    

class Login(models.Model):
    titulo = models.CharField(max_length=55)
    imgLogin = models.ImageField(upload_to="imgLogin/")

    def __str__(self):
        return self.titulo
    
class NovaTurma(models.Model):
    titulo = models.CharField(max_length=55)
    texto = models.CharField(max_length=100)
    imgNovaTurma = models.ImageField(upload_to="imgNovaTurma/")

    def __str__(self):
        return self.titulo
    
class Cadastro(models.Model):
    titulo = models.CharField(max_length=55)
    imgCadastro = models.ImageField(upload_to="imgCadastro/")
    
class Lixeira(models.Model):
    titulo = models.CharField(max_length=55)

class Processo(models.Model):
    titulo = models.CharField(max_length=55)
    
class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_IHX = models.CharField(max_length=30)
    senha_IHX = models.CharField(max_length=20)
    login_CAF = models.CharField(max_length=30)
    senha_CAF = models.CharField(max_length=20)


class In_progress_file(models.Model):
    turma =  models.CharField(max_length=20)
    arquivo_inprogress = models.FileField(upload_to='in_progress_files/')
    upload_time = models.DateTimeField(auto_now_add=True)

class Finished_file(models.Model):
    turma =  models.CharField(max_length=20)
    arquivo_fineshed = models.FileField(upload_to='finished_files/')
    upload_time = models.DateTimeField(auto_now_add=True)

class Funcionario(models.Model):
    titulo = models.CharField(max_length=55)
    imgFuncionarios = models.ImageField(upload_to="imgFuncionarios/")

class Perfil(models.Model):
    titulo = models.CharField(max_length=55)
    imgPerfil = models.ImageField(upload_to="imgPerfil/")

class PerfilEditar(models.Model):
    titulo = models.CharField(max_length=55)
    imgPerfil = models.ImageField(upload_to="imgPerfilEditar/")

class Cadastro_Info(models.Model):
    titulo = models.CharField(max_length=55)
    imgInfo = models.ImageField(upload_to="imgInfo/")