from django.db import models
from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from distutils.command import upload

class crearUsuario(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class editarUsuario(UserChangeForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget= forms.PasswordInput)
    first_name= forms.CharField(label="Modificar NOMBRE")
    last_name= forms.CharField(label="Modificar APELLIDO")

    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class avatarImagen(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        help_texts = {k:"" for k in fields}

