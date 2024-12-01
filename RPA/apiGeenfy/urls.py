from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import In_progress_fileViewSet, Finished_FileViewSet, ErrorLogViewSet

router = DefaultRouter()
router.register(r'documentos', In_progress_fileViewSet)
router.register(r'concluido', Finished_FileViewSet)
router.register(r'erro', ErrorLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]