from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioReadOnlyModelViewSet, DocumentoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioReadOnlyModelViewSet)
router.register(r'documentos', DocumentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]