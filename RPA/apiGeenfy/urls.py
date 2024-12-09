from django.urls import path, include # Importa as funções para definir e incluir URLs.
from rest_framework.routers import DefaultRouter # Importa o roteador padrão do Django REST Framework.
from .views import In_progress_fileViewSet, Finished_FileViewSet, ErrorLogViewSet # Importa os ViewSets que definem a lógica das operações para os endpoints.

router = DefaultRouter() # Cria uma instância do roteador padrão
router.register(r'documentos', In_progress_fileViewSet) # Registra o ViewSet 'In_progress_fileViewSet' com a rota base 'documentos'.
router.register(r'concluido', Finished_FileViewSet) # Registra o ViewSet 'Finished_FileViewSet' com a rota base 'concluido'.
router.register(r'erro', ErrorLogViewSet) # Registra o ViewSet 'ErrorLogViewSet' com a rota base 'erro'.

# Define as URLs do aplicativo usando o roteador
urlpatterns = [
    path('', include(router.urls)), # Inclui todas as rotas registradas no roteador como parte das URLs do aplicativo.
]
