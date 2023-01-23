from django.urls import path
from Usuario.views import *
from Blog import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', ingreso, name="login"),
    path('register/', register, name="register"),
<<<<<<< HEAD
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
=======
    path('editarPerfil', editarPerfil, name="editarPerfil"),
>>>>>>> 8278c2b0ebc7ec4f09613d7e7cad083a6bcf4a9f
    path('logout/', LogoutView.as_view(), name="logout"),
    path('', views.inicio),
]
