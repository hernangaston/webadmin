from django.db import models

class Entregador(models.Model):
    nombre = models.CharField(max_length=255)
    cuit = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    #funcion para devolver el nombre de usuario que se agrega al serializer
    #def nombreUser(self):
      #  return self.user.nombre