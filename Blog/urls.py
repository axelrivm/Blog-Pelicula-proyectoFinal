from django.urls import path, include
from Blog.views import *
from Usuario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crearPeli/', crearPeli, name = "crearPeli" ),
    path('modificarPeli/<id>', modificarPeli, name = "modificarPeli"),
    path('eliminarPeli/<id>', eliminarPeli, name = 'eliminarPeli'),
    path('listarPeli/', listarPeli, name = 'listarPeli'),
    path('verPeliDetalle/<id>', verPeliDetalle, name = 'verPeliDetalle'),
    path('verPeli/', verPeli, name = 'verPeli'),
    path('about/', about, name = 'about'),
    path('', inicio, name = 'inicio'),
    path('Usuario/', include('Usuario.urls')),
] + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
