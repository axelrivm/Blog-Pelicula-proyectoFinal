from django.db import models
from django.contrib.auth.models import User


<<<<<<< HEAD
class Avatar(models.Model):
    
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='avatar')

    def __str__(self):
        return f'{self.user.username} Avatar'
=======

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField
    userName = models.CharField(max_length=30)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatar")
    user= models.ForeignKey(User, on_delete=models.CASCADE)

>>>>>>> 8278c2b0ebc7ec4f09613d7e7cad083a6bcf4a9f

    