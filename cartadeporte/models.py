from django.db import models
from django.contrib.auth.models import User
from empresa.models import Empresa
from intermediario.models import Intermediario
from remitentecomercial.models import RemitenteComercial
from corredor.models import Corredor
from mat.models import MercadoATermino
from destinatario.models import Destinatario
from destino.models import Destino
from intermediarioflete.models import IntermediarioFlete
from transportista.models import Transportista
from chofer.models import Chofer
from entregador.models import Entregador

class CartaDePorte(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    numero = models.CharField(max_length=255, null=True, blank=True)
    ctg = models.CharField(max_length=255, null=True, blank=True)
    renspa = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    titular = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    intermediario = models.ForeignKey(Intermediario, on_delete=models.CASCADE, null=True, blank=True)
    remitente_comercial = models.ForeignKey(RemitenteComercial, on_delete=models.CASCADE, null=True, blank=True)
    corredor_comprador = models.ForeignKey(Corredor, on_delete=models.CASCADE, null=True, blank=True, related_name='corredorC')
    mercado_a_termino = models.ForeignKey(MercadoATermino, on_delete=models.CASCADE, null=True, blank=True)
    corredor_vendedor = models.ForeignKey(Corredor, on_delete=models.CASCADE, null=True, blank=True, related_name='corredorV')
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE, null=True, blank=True)
    destinatario = models.ForeignKey(Destinatario, on_delete=models.CASCADE, null=True, blank=True)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, null=True, blank=True)
    intermediario_flete = models.ForeignKey(IntermediarioFlete, on_delete=models.CASCADE, null=True, blank=True)
    transportista = models.ForeignKey(Transportista, on_delete=models.CASCADE, null=True, blank=True)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE, null=True, blank=True)
    grano = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    cosecha = models.CharField(max_length=255, null=True, blank=True)
    contrato = models.CharField(max_length=255, null=True, blank=True) #aca enlazamos con los ctos. de compra vta.
    pesada_en_destino = models.BooleanField(null=True, blank=True)
    kgs_estimados = models.BooleanField(null=True, blank=True)
    declaracion_calidad = models.BooleanField(null=True, blank=True)
    conforme = models.BooleanField(null=True, blank=True)
    condicional = models.BooleanField(null=True, blank=True)
    peso_bruto = models.CharField(max_length=255, null=True, blank=True)
    peso_tara = models.CharField(max_length=255, null=True, blank=True)
    peso_neto = models.CharField(max_length=255, null=True, blank=True)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    #-----------------PROCEDENCIA-----------------------
    direccion_procedencia = models.CharField(max_length=255, null=True, blank=True)
    localidad_procedencia = models.CharField(max_length=255, null=True, blank=True)
    provincia_procedencia = models.CharField(max_length=255, null=True, blank=True)
    kilometros = models.CharField(max_length=255, null=True, blank=True)
    tarifa = models.CharField(max_length=255, null=True, blank=True)
    tarifa_referencia = models.CharField(max_length=255, null=True, blank=True)
    declaracion_juarada_nombre = models.CharField(max_length=255, null=True, blank=True)
    declaracion_juarada_dni = models.CharField(max_length=255, null=True, blank=True)
    docfile = models.FileField(upload_to='cp_nuevas', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.numero
    #funcion para devolver el nombre de usuario que se agrega al serializer
    def nombreUser(self):
        return self.user.nombre
    
    def nombreChofer(self):
        return self.chofer.nombre
    
    def localidadDestino(self):
        return self.destino.localidad