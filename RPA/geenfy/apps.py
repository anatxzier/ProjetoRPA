from django.apps import AppConfig # Importa a classe AppConfig para configurar o aplicativo no Django.

# Configuração do aplicativo 'geenfy'
class GeenfyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # Define o tipo de campo de chave primária para os modelos.
    name = 'geenfy' # Define o nome do aplicativo, que deve coincidir com o diretório do aplicativo.

    # Método 'ready' é chamado quando o aplicativo é carregado
    def ready(self):
        import geenfy.signals # Importa sinais (signals) que são utilizados para adicionar lógica extra ou reagir a eventos específicos.
