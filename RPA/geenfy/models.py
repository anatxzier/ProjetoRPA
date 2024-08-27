from django.db import models

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