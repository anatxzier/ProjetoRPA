from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Usuario 

@receiver(post_save, sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created:
        # Cria um novo registro em Usuario quando um novo usuário é criado
        Usuario.objects.create(
            user=instance,
            login_IHX='',  # Inicia com um valor padrão ou vazio
            senha_IHX='', 
            login_CAF='',  
            senha_CAF='',   
        )

