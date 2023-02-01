from django.db import models

# Create your models here.
class Pelicula(models.Model):
    nombre = models.CharField(max_length=30)
    sinopsis = models.CharField(max_length=150)
    año = models.IntegerField()
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} +  {str(self.sinopsis)} + {str(self.año)} "


class Categoria(models.Model):
    tipo = models.IntegerField()
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.tipo} +  {str(self.nombre)}"

class Genero(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre}"

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} +  {str(self.apellido)} + {str(self.nacimiento)}"