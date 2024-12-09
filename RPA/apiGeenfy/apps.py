from django.apps import AppConfig # Importa a classe base para configuração de aplicativos no Django.


class ApigeenfyConfig(AppConfig): # Classe de configuração para o aplicativo 'apiGeenfy'.
    default_auto_field = 'django.db.models.BigAutoField' # Define o tipo padrão de chave primária para os modelos do aplicativo.
    name = 'apiGeenfy' # Nome do aplicativo que será usado nas configurações do projeto.
