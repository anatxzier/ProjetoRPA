from django.db.models.signals import post_save # Importa os sinais do Django para ser capaz de reagir a eventos específicos (como salvar um objeto)
from django.dispatch import receiver
from django.contrib.auth.models import User # Importa o modelo User, que é o modelo de usuários padrão do Django
from .models import Usuario # Importa o modelo Usuario, que provavelmente foi definido para armazenar informações adicionais de usuários

# Recebe o sinal post_save quando um objeto do modelo User é salvo
@receiver(post_save, sender=User)
def create_usuario(sender, instance, created, **kwargs):
    if created: # Verifica se o usuário foi criado, não apenas salvo
        # Cria um novo registro em Usuario quando um novo usuário é criado
        Usuario.objects.create(
            user=instance, # Associa o objeto User recém-criado ao campo 'user' do modelo Usuario
            login_IHX='',  # Inicia com um valor padrão ou vazio
            senha_IHX='', 
            login_CAF='',  
            senha_CAF='',   
        )

