
from django.contrib import admin
from django.urls import path
from geenfy import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage_View, name="homepage")
]
