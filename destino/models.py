from django.db import models
from destinatario import Destinatario

class Destino(models.Model):
    destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=255)
    cuit = models.CharField(max_length=255)
    codigo_de_planta = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    localidad = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    #funcion para devolver el nombre de usuario que se agrega al serializer
    #def nombreUser(self):
      #  return self.user.nombre