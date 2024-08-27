
from django.contrib import admin
from django.urls import path
from geenfy import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage_View, name="homepage"),
    path('login', views.Login_View, name="login"),
    path('novaturma', views.NovaTurma_View, name="novaturma"),
    path('cadastro', views.Cadastro_View, name="cadastro"),




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

