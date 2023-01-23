from django.db import models
from django import forms
<<<<<<< HEAD
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from distutils.command import upload
=======
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
>>>>>>> 8278c2b0ebc7ec4f09613d7e7cad083a6bcf4a9f

class crearUsuario(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)
<<<<<<< HEAD
    
=======

>>>>>>> 8278c2b0ebc7ec4f09613d7e7cad083a6bcf4a9f
    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

<<<<<<< HEAD
class editarUsuario(UserChangeForm):
=======
class editarUsuario(UserCreationForm):
>>>>>>> 8278c2b0ebc7ec4f09613d7e7cad083a6bcf4a9f

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)
    first_name= forms.CharField(label="Modificar NOMBRE")
    last_name= forms.CharField(label="Modificar APELLIDO")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
<<<<<<< HEAD
        help_texts = {k:"" for k in fields}

class avatarImagen(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['profile_image']
=======
        help_texts = {k:"" for k in fields}
>>>>>>> 8278c2b0ebc7ec4f09613d7e7cad083a6bcf4a9f
