from django.db import models

class Homepage(models.Model):
    titulo = models.CharField(max_length=55)
    texto = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="imgHome/")

    def __str__(self):
        return self.titulo

