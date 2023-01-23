
from django.shortcuts import render, redirect

from django.shortcuts import render

from .models import User
from Usuario.forms import crearUsuario, editarUsuario
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def ingreso(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info= form.cleaned_data
            name=info["username"]
            password=info["password"]
            usuario= authenticate(username=name, password=password)
            if usuario is not None:
                login(request, usuario)
                return render(request, "main/inicio.html", {"mensaje":f"Usuario {usuario} ingresado correctamente"})
            else:
                return render(request, "main/login.html", {"form": form, "mensaje": "Error al ingresar el usuario"})
        else:
            return render(request, "main/login.html", {"form": form, "mensaje": "Error al ingresar el usuario"})
    else:
        form=AuthenticationForm()
        return render(request, "main/login.html", {"form": form})

def register(request):
    if request.method=="POST":
        form = crearUsuario(request.POST)
        if form.is_valid():
            username= form.cleaned_data
            form.save()
            return render(request, "main/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "main/register.html", {"form": form, "mensaje": "Error al crear el usuario"})
        
    else:
        form = crearUsuario()
        return render(request, "main/register.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario=request.user
    
    if request.method=="POST":
        form= editarUsuario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save()
            return render(request, "main/inicio.html", {"mensaje":f"Usuario {usuario} modificado correctamente"})
        else:
            return render(request, "main/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    else:
        form = editarUsuario(instance=usuario)
        return render(request, "main/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})


def listarPerfiles(request):
    if request.method == "POST":
        return redirect('listarPerfil')
    else:
        usuarios = User.objects.all()
        return render (request, 'main/lista.html', {"usuarios": usuarios})





    
