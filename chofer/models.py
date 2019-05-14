from django.db import models
from transportista.models import Transportista


class Chofer(models.Model):
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cuit = models.CharField(max_length=255)
    patente_chasis = models.CharField(max_length=255)
    patente_acoplado = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.apellido, self.nombre)
    # funcion para devolver el nombre de usuario que se agrega al serializer
    # def nombreUser(self):
      #  return self.user.nombre
