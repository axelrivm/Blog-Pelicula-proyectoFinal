from django.http import HttpResponse
from django.shortcuts import render, redirect

from Blog.forms import PeliFormulario
from Blog.models import *
from Blog.views import *


#Vista del index, donde se pasan los comentarios, productos y modificaciones del inicio (titulo, imagen, descripcion)
def inicio(request):    
    return render(request, 'index.html')
    