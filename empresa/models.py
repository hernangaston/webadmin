from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
   
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    cuit = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    #funcion para devolver el nombre de usuario que se agrega al serializer
    def nombreUser(self):
        return self.user.nombre