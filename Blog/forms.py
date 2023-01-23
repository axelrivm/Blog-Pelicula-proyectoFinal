from django import forms
from django.forms import fields
from distutils.command import upload
from django.db import models
from Blog.models import *

class PeliFormulario(forms.ModelForm):
     class Meta:
        model = Pelicula
        fields = '__all__'
    


    