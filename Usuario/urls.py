from django.urls import path
from Usuario.views import *
from Blog import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', ingreso, name="login"),
    path('register/', register, name="register"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', views.inicio),
]
