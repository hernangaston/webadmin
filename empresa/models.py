from django.db import models


# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    cuit = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.nombre