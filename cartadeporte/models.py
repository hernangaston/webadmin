from django.db import models
from django.contrib.auth.models import User
from empresa import Empresa
from intermediario import Intermediario
from remitentecomercial import RemitenteComercial
from corredor import Corredor
from mat import MercadoATermino
from destinatario import Destinatario
from destino import Destino
from intermediarioflete import IntermediarioFlete
from transportista import Transportista
from chofer import Chofer

class Empresa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    numero = models.CharField(max_length=255)
    ctg = models.CharField(max_length=255)
    renspa = models.CharField(max_length=255)
    fecha = models.DateField()
    titular = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    intermediario = models.ForeignKey(Intermediario, on_delete=models.CASCADE, null=True)
    remitente_comercial = models.ForeignKey(RemitenteComercial, on_delete=models.CASCADE, null=True)
    corredor_comprador = models.ForeignKey(Corredor, on_delete=models.CASCADE, null=True)
    mercado_a_termino = models.ForeignKey(MercadoATermino, on_delete=models.CASCADE, null=True)
    corredor_vendedor = models.ForeignKey(Corredor, on_delete=models.CASCADE, null=True)
    entregador = models.ForeignKey(Corredor, on_delete=models.CASCADE, null=True)
    destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE, null=True)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, null=True)
    intermediario_flete = models.ForeignKey(IntermediarioFlete, on_delete=models.CASCADE, null=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE, null=True)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE, null=True)
    grano = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    cosecha = models.CharField(max_length=255)
    contrato = models.CharField(max_length=255) #aca enlazamos con los ctos. de compra vta.
    pesada_en_destino = models.BooleanField()
    kgs_estimados = models.BooleanField()
    declaracion_calidad = models.BooleanField()
    conforme = models.BooleanField()
    condicional = models.BooleanField()
    peso_bruto = models.CharField(max_length=255)
    peso_tara = models.CharField(max_length=255)
    peso_neto = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255)
    #-----------------PROCEDENCIA-----------------------
    direccion_procedencia = models.CharField(max_length=255)
    localidad_procedencia = models.CharField(max_length=255)
    provincia_procedencia = models.CharField(max_length=255)
    kilometros = models.CharField(max_length=255)
    tarifa = models.CharField(max_length=255)
    tarifa_referencia = models.CharField(max_length=255)
    declaracion_juarada_nombre = models.CharField(max_length=255)
    declaracion_juarada_dni = models.CharField(max_length=255)


    def __str__(self):
        return self.nombre
    #funcion para devolver el nombre de usuario que se agrega al serializer
    #def nombreUser(self):
      #  return self.user.nombre