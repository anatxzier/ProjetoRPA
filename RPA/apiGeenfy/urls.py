from django.urls import path
from .views import RodarScriptAPIView

urlpatterns = [
    path('rodar-script/', RodarScriptAPIView.as_view(), name='rodar_script'),
]