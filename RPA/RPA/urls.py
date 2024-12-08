from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Define a lista de URLs do projeto
urlpatterns = [
    path('admin/', admin.site.urls), # URL para acessar o painel administrativo do Django.
    path('', include('geenfy.urls')), # Inclui as URLs definidas no aplicativo 'geenfy' para a rota principal.
    path('api/', include('apiGeenfy.urls')) # Inclui as URLs do aplicativo 'apiGeenfy' na rota 'api/'.
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Adiciona suporte para servir arquivos estáticos e de mídia durante o desenvolvimento.

