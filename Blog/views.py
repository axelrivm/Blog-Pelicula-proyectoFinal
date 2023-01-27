from django.shortcuts import render, redirect
from Blog.models import *
from django.http import HttpResponse
from Blog.forms import PeliFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def inicio(request):
    if request.method == "POST":
        return redirect('inicio')
    else:
        peliculas = Pelicula.objects.all()
        return render (request, 'main/inicio.html', {"peliculas": peliculas})
    


@login_required
def crearPeli(request):
    if request.method=="POST":
        formulario= PeliFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info= formulario.cleaned_data
            nombre= info["nombre"]
            sinopsis= info["sinopsis"]
            año= info["año"]
            imagen= info["imagen"]
            pelicula= Pelicula(nombre=nombre, sinopsis=sinopsis, año=año, imagen=imagen)
            pelicula.save()
            pelis = Pelicula.objects.all()
            return redirect('listarPeli')
        else:
            return render (request, 'main/altaPeli.html',{"form": formulario, "mensaje": "Informacion no valida"})
    else:
        formulario = PeliFormulario()
        return render (request, 'main/altaPeli.html', {"form": formulario})

def about(request):
    return render (request, 'main/about.html')

@login_required
def modificarPeli(request, id):
    pelicula = Pelicula.objects.get(id=id)
    if request.method=="POST":
        form = PeliFormulario(request.POST, request.FILES)
        if form.is_valid():
            info= form.cleaned_data 
            pelicula.nombre= info["nombre"]
            pelicula.sinopsis= info["sinopsis"]
            pelicula.año= info["año"]
            pelicula.imagen= info["imagen"]
            pelicula.save()
            pelis= Pelicula.objects.all()
            return redirect('listarPeli')
        pass
    else:
        formulario = PeliFormulario(initial={"nombre": pelicula.nombre, "sinopsis": pelicula.sinopsis, "año": pelicula.año, "imagen": pelicula.imagen})
        return render (request, 'main/modificar.html', {"form": formulario, "pelicula": pelicula})


def verPeliDetalle(request, id):
    if Pelicula.objects.filter(id=id):
        pelicula = Pelicula.objects.get(id=id)
        return render (request, 'main/verPeliDetalle.html', {"peli": pelicula})
    else:
        return render (request, 'main/inicio.html')
        
 
@login_required
def eliminarPeli(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    peliculas = Pelicula.objects.all()
    return redirect('listarPeli')


def verPeli(request):
    if "nombre" in request.GET:
        name = request.GET['nombre']
        peliculas = Pelicula.objects.filter(nombre__icontains=name)
        #peliculas = Pelicula.objects.all()
        #return HttpResponse(f"Devuelto{request.GET['nombre']}")
        return render (request, 'main/verPeli.html', {"peliculas": peliculas})
    else:
        
        peliculas = Pelicula.objects.all()
        return redirect('listarPeli')

def listarPeli(request):
    if request.method == "POST":
        return redirect('listarPeli')
    else:
        peliculas = Pelicula.objects.all()
        return render (request, 'main/lista.html', {"peliculas": peliculas})





    