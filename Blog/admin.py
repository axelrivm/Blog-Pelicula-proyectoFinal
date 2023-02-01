from django.contrib import admin
from Blog.models import *
from Usuario.models import *
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Pelicula)
admin.site.register(Genero)
#admin.site.register(avatar)