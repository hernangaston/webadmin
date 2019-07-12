from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.exceptions import ParseError



from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CartaDePorte
from .renderers import CartaDePorteJSONRenderer
from .serializers import CartaDePorteSerializer, CartaDePorteListSerializer

from django.http import HttpResponse
import os
import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.colors import Color, red
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from corredor.models import Corredor
from mat.models import MercadoATermino
from entregador.models import Entregador
from destinatario.models import Destinatario
from destino.models import Destino
from intermediarioflete.models import IntermediarioFlete
from transportista.models import Transportista
from chofer.models import Chofer
from intermediario.models import Intermediario
from remitentecomercial.models import RemitenteComercial



class IndexView(TemplateView):
    template_name = "index.html"

class CartaViewSet(viewsets.ModelViewSet):
    permissions_classes = (IsAuthenticated,)
    queryset = CartaDePorte.objects.all()
    serializer_class = CartaDePorteSerializer
    lookup_field = 'id'

class CartaDePorteListApiView(ListAPIView):
    model = CartaDePorte
    queryset = CartaDePorte.objects.all()
    permissions_classes = (AllowAny, )
    renderer_classes = (CartaDePorteJSONRenderer, )
    serializer_class = CartaDePorteListSerializer


class CartaDePorteRetrieveApiView(RetrieveAPIView):
    permissions_classes = (AllowAny, )
    renderer_classes = (CartaDePorteJSONRenderer, )
    serializer_class = CartaDePorteSerializer

    def retrieve(self, request, cartadeporte, *args, **kwargs):
        cartadeporte = CartaDePorte.objects.get(id=cartadeporte.id)
        serializer = self.serializer_class(cartadeporte)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CartaDePorteListView(ListView):
    template_name = 'cp_list.html'
    model = CartaDePorte

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# ------CLASE PARA GENERAR EL PDF ----------------------------------------------
class GeneratePDF(UpdateView):
        # queryset = PacienteIapos.objects.all()
        # model = PacienteIapos
        # form_class = FormularioPaciente
        # template_name = 'paciente/paciente_form.html'
        # success_url = reverse_lazy('pacientes:pacientes')

    def get(self, request, *args, **kwargs):
        cp = CartaDePorte.objects.get(pk=self.kwargs['pk'])
        pdfCp(cp)
        # Create the HttpResponse object with the appropriate PDF headers.
        # with open("static/"+paciente.nombre+paciente.apellido+".pdf", "rb") as pdf:
        pdf = open("media/CP" + cp.numero + ".pdf", "rb")
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="' + \
            'CP' + cp.numero + '.pdf"'
        pdf.closed
        os.remove("media/cp_nuevas/" + cp.numero + ".pdf")
        return response
# ------Subir el archivo que viene por post--------------------


class UploadFile(APIView):
    parser_class = (FileUploadParser, MultiPartParser)

    def post(self, request, filename, format=None):
        print(request.data)
        #pdf_recibido = request.data['file']

        nuevoPdf = CartaDePorte()

        nuevoPdf.numero = request.data['numero']
        nuevoPdf.fecha = request.data['fecha']
        nuevoPdf.ctg = request.data['ctg']
        nuevoPdf.renspa = request.data['renspa']
        if request.data['intermediario']:
            nuevoPdf.intermediario = Intermediario.objects.get(pk=request.data['intermediario'])
        if request.data['remitente_comercial']:
            nuevoPdf.remitente_comercial = RemitenteComercial.objects.get(pk=request.data['remitente_comercial'])
        if request.data['conforme'] == 'true':
            nuevoPdf.conforme = True
        else:
            nuevoPdf.conforme = False
        if request.data['corredor_comprador']:
            nuevoPdf.corredor_comprador = Corredor.objects.get(pk=request.data['corredor_comprador'])
        if request.data['mercado_a_termino']:
            nuevoPdf.mercado_a_termino = MercadoATermino.objects.get(pk=request.data['mercado_a_termino'])
        if request.data['corredor_vendedor']:
            nuevoPdf.corredor_vendedor = Corredor.objects.get(pk=request.data['corredor_vendedor'])
        if request.data['entregador']:
            nuevoPdf.entregador = Entregador.objects.get(pk=request.data['entregador'])
        if request.data['destinatario']:
            nuevoPdf.destinatario = Destinatario.objects.get(pk=request.data['destinatario'])
        if request.data['destino']:
            nuevoPdf.destino = Destino.objects.get(pk=request.data['destino'])
        if request.data['intermediario_flete']:
            nuevoPdf.intermediario_flete = IntermediarioFlete.objects.get(pk=request.data['intermediario_flete'])
        if request.data['transportista']:
            nuevoPdf.transportista = Transportista.objects.get(pk=request.data['transportista'])
        if request.data['chofer']:
            nuevoPdf.chofer = Chofer.objects.get(pk=request.data['chofer'])
        nuevoPdf.grano = request.data['grano']
        if request.data['tipo'] != '':
            nuevoPdf.tipo = request.data['tipo']
        else:
            nuevoPdf.tipo = '' 
        nuevoPdf.cosecha = request.data['cosecha']
        if request.data['contrato'] != '':
            nuevoPdf.contrato = request.data['contrato']
        else:
            nuevoPdf.contrato = ''
        if request.data['pesada_en_destino'] == 'true':
            nuevoPdf.pesada_en_destino = True
        else:
            nuevoPdf.pesada_en_destino = False
        if request.data['kgs_estimados'] == 'true':
            nuevoPdf.kgs_estimados = True
        else:
            nuevoPdf.kgs_estimados = False
        if request.data['declaracion_calidad'] == 'true':
            nuevoPdf.declaracion_calidad = True
        else:
            nuevoPdf.declaracion_calidad = False
        if request.data['condicional'] == 'true':
            nuevoPdf.condicional = True
        else:
            nuevoPdf.condicional = False
        nuevoPdf.peso_bruto = request.data['peso_bruto']
        nuevoPdf.peso_tara = request.data['peso_tara']
        nuevoPdf.peso_neto = request.data['peso_neto']
        if request.data['observaciones'] != '':
            nuevoPdf.observaciones = request.data['observaciones']
        else:
            nuevoPdf.observaciones = ''
        nuevoPdf.direccion_procedencia = request.data['direccion_procedencia']
        nuevoPdf.localidad_procedencia = request.data['localidad_procedencia']
        nuevoPdf.provincia_procedencia = request.data['provincia_procedencia']
        nuevoPdf.kilometros = request.data['kilometros']
        nuevoPdf.tarifa = request.data['tarifa']
        nuevoPdf.tarifa_referencia = request.data['tarifa']
        nuevoPdf.declaracion_juarada_nombre = request.data['declaracion_juarada_nombre']
        nuevoPdf.declaracion_juarada_dni = request.data['declaracion_juarada_dni']
        nuevoPdf.docfile = request.data['docfile']
        #nuevoPdf.docfile = pdf_recibido


        nuevoPdf.save()
        return Response(status=204)

class CartaDePorteCreate(APIView):
    parser_class = (FileUploadParser, MultiPartParser)

    def post(self, request):
        data_recived = request.data
        print(data_recived)
        print(data_recived['docfile'])
        data = CartaDePorte()
        data.save()
        return Response(status=200)




# -------funcion para rellenar la cp preimpresa ------------------------------
def pdfCp(data):
    if(data.ctg):
        ctg = str(data.ctg)
    else:
        ctg = ''
    if(data.renspa):
        renspa = str(data.renspa)
    else:
        renspa = ''
    fecha = str(data.fecha.strftime("%d  %m  %Y"))
    if(data.intermediario):
        intermediario = str(data.intermediario)
        cuit_intermediario = str(data.intermediario.cuit)
    else:
        intermediario = ''
        cuit_intermediario = ''
    if(data.remitente_comercial):
        remitente_comercial = str(data.remitente_comercial)
        cuit_remitente_comercial = str(data.remitente_comercial.cuit)
    else:
        remitente_comercial = ''
        cuit_remitente_comercial = ''
    if(data.corredor_comprador):
        corredor_comprador = str(data.corredor_comprador)
        cuit_corredor_comprador = str(data.corredor_comprador.cuit)
    else:
        corredor_comprador = ''
        cuit_corredor_comprador = ''
    if(data.mercado_a_termino):
        mercado_a_termino = str(data.mercado_a_termino)
        cuit_mercado_a_termino = str(data.mercado_a_termino.cuit)
    else:
        mercado_a_termino = ''
        cuit_mercado_a_termino = ''
    if(data.corredor_vendedor):
        corredor_vendedor = str(data.corredor_vendedor)
        cuit_corredor_vendedor = str(data.corredor_vendedor.cuit)
    else:
        corredor_vendedor = ''
        cuit_corredor_vendedor = ''
    if(data.entregador):
        entregador = str(data.entregador)
        cuit_entregador = str(data.entregador.cuit)
    else:
        entregador = ''
        cuit_entregador = ''
    if(data.destinatario):
        cuit_destinatario = str(data.destinatario.cuit)
        destinatario = str(data.destinatario)
    else:
        cuit_destinatario = ''
        destinatario = ''
    if(data.destino):
        destino = str(data.destino)
        cuit_destino = str(data.destino.cuit)
    else:
        destino = ''
        cuit_destino = ''
    if(data.intermediario_flete):
        intermediario_flete = str(data.intermediario_flete)
        cuit_intermediario_flete = str(data.intermediario_flete.cuit)
    else:
        intermediario_flete = ''
        cuit_intermediario_flete = ''
    if(data.transportista):
        transportista = str(data.transportista)
        cuit_transportista = str(data.transportista.cuit)
    else:
        transportista = ''
        cuit_transportista = ''
    if(data.chofer):
        chofer = str(data.chofer)
        cuit_chofer = str(data.chofer.cuit)
    else:
        chofer = ''
        cuit_chofer = ''
    grano = str(data.grano)
    if(data.tipo):
        tipo = str(data.tipo)
    else:
        tipo = ''
    if(data.cosecha):
        cosecha = str(data.cosecha)
    else:
        cosecha = ''
    if(data.contrato):
        contrato = str(data.contrato)
    else:
        contrato = ''
    if data.pesada_en_destino:
        pesada_en_destino = 'X'
    else:
        pesada_en_destino = ''
    if data.kgs_estimados:
        kgs_estimados = 'SI'
    else:
        kgs_estimados = ''
    if data.declaracion_calidad:
        declaracion_calidad = 'X'
    else:
        declaracion_calidad = ''

    if data.conforme:
        conforme = 'X'
    else:
        conforme = ''
    if data.condicional:
        condicional = 'X'
    else:
        condicional = ''
    if(data.peso_bruto):
        peso_bruto = str(data.peso_bruto)
    else:
        peso_bruto = ''
    if(data.peso_tara):
        peso_tara = str(data.peso_tara)
    else:
        peso_tara = ''
    if(data.peso_neto):
        peso_neto = str(data.peso_neto)
    else:
        peso_neto = ''
    if(data.observaciones):
        observaciones = str(data.observaciones)
    else:
        observaciones = ''
    if(data.direccion_procedencia):
        direccion_procedencia = str(data.direccion_procedencia)
    else:
        direccion_procedencia = ''
    if(data.localidad_procedencia):
        localidad_procedencia = str(data.localidad_procedencia)
    else:
        localidad_procedencia = ''
    provincia_procedencia = str(data.provincia_procedencia)
    cod_planta_destino = " "
    direccion_destino = str(data.destino.direccion)
    localidad_destino = str(data.destino.localidad)
    provincia_destino = str(data.destino.provincia)
    pagador_flete = "AGROEQUITY S.A."
    camion = str(data.chofer.patente_chasis)
    acoplado = str(data.chofer.patente_acoplado)
    if(data.kilometros):
        kilometros = str(data.kilometros)
    else:
        kilometros = ''
    if(data.tarifa):
        tarifa = str(data.tarifa)
    else:
        tarifa = ''
    if(data.tarifa_referencia):
        tarifa_referencia = str(data.tarifa_referencia)
    else:
        tarifa_referencia = ''
    declaracion_juarada_nombre = str(data.declaracion_juarada_nombre)
    if(data.declaracion_juarada_dni):
        declaracion_juarada_dni = str(data.declaracion_juarada_dni)
    else:
        declaracion_juarada_dni = ''
    # --------------pagina1---------------
    packet = io.BytesIO()
    # crear un nuevo pdf con Reportlab
    can = canvas.Canvas(packet, pagesize=A4)  # seria tamanio A4
    can.setFont("Helvetica", 9)
    can.drawString(190, 747, ctg)
    can.drawString(300, 747, renspa)
    can.drawString(510, 760, fecha)
    can.drawString(185, 683, intermediario)
    can.drawString(473, 683, cuit_intermediario)
    can.drawString(185, 663, remitente_comercial)
    can.drawString(473, 663, cuit_remitente_comercial)
    can.drawString(185, 643, corredor_comprador)
    can.drawString(473, 643, cuit_corredor_comprador)
    can.drawString(185, 623, mercado_a_termino)
    can.drawString(473, 623, cuit_mercado_a_termino)
    can.drawString(185, 603, corredor_vendedor)
    can.drawString(473, 603, cuit_corredor_vendedor)
    can.drawString(185, 583, entregador)
    can.drawString(473, 583, cuit_entregador)
    can.drawString(185, 563, destinatario)
    can.drawString(473, 563, cuit_destinatario)
    can.drawString(185, 543, destino)
    can.drawString(473, 543, cuit_destino)
    can.drawString(185, 523, intermediario_flete)
    can.drawString(473, 523, cuit_intermediario_flete)
    can.drawString(185, 503, transportista)
    can.drawString(473, 503, cuit_transportista)
    can.drawString(185, 483, chofer)
    can.drawString(473, 483, cuit_chofer)
    can.drawString(140, 460, grano)
    can.drawString(240, 460, tipo)
    can.drawString(360, 460, cosecha)
    can.drawString(498, 460, contrato)
    can.drawString(133, 431, pesada_en_destino)
    can.drawString(129, 412, kgs_estimados)
    can.drawString(258, 445, declaracion_calidad)
    can.drawString(258, 428, conforme)
    can.drawString(258, 411, condicional)
    can.drawString(360, 445, peso_bruto)
    can.drawString(360, 428, peso_tara)
    can.drawString(360, 409, peso_neto)
    can.drawString(410, 435, observaciones)
    can.drawString(110, 372, direccion_procedencia)
    can.drawString(430, 380, localidad_procedencia)
    can.drawString(430, 367, provincia_procedencia)
    can.drawString(95, 347, cod_planta_destino)
    can.drawString(73, 330, direccion_destino)
    can.drawString(365, 347, localidad_destino)
    can.drawString(365, 330, provincia_destino)
    can.drawString(355, 310, pagador_flete)
    can.drawString(95, 295, camion)
    can.drawString(95, 277, acoplado)
    can.drawString(95, 262, kilometros)
    can.drawString(243, 262, tarifa)
    can.drawString(243, 277, tarifa_referencia)
    can.drawString(300, 17, declaracion_juarada_nombre)
    can.drawString(460, 17, declaracion_juarada_dni)
    can.showPage()
    can.save()

    # mover el archivo al comiezo dela pila de ejecucion
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # --------------pagina2---------------
    packet2 = io.BytesIO()
    # crear un nuevo pdf con Reportlab
    can2 = canvas.Canvas(packet2, pagesize=A4)  # seria tamanio A4
    can2.setFont("Helvetica", 9)
    can2.drawString(190, 747, ctg)
    can2.drawString(300, 747, renspa)
    can2.drawString(510, 760, fecha)
    can2.drawString(185, 683, intermediario)
    can2.drawString(473, 683, cuit_intermediario)
    can2.drawString(185, 663, remitente_comercial)
    can2.drawString(473, 663, cuit_remitente_comercial)
    can2.drawString(185, 643, corredor_comprador)
    can2.drawString(473, 643, cuit_corredor_comprador)
    can2.drawString(185, 623, mercado_a_termino)
    can2.drawString(473, 623, cuit_mercado_a_termino)
    can2.drawString(185, 603, corredor_vendedor)
    can2.drawString(473, 603, cuit_corredor_vendedor)
    can2.drawString(185, 583, entregador)
    can2.drawString(473, 583, cuit_entregador)
    can2.drawString(185, 563, destinatario)
    can2.drawString(473, 563, cuit_destinatario)
    can2.drawString(185, 543, destino)
    can2.drawString(473, 543, cuit_destino)
    can2.drawString(185, 523, intermediario_flete)
    can2.drawString(473, 523, cuit_intermediario_flete)
    can2.drawString(185, 503, transportista)
    can2.drawString(473, 503, cuit_transportista)
    can2.drawString(185, 483, chofer)
    can2.drawString(473, 483, cuit_chofer)
    can2.drawString(140, 460, grano)
    can2.drawString(240, 460, tipo)
    can2.drawString(360, 460, cosecha)
    can2.drawString(498, 460, contrato)
    can2.drawString(133, 431, pesada_en_destino)
    can2.drawString(129, 412, kgs_estimados)
    can2.drawString(258, 445, declaracion_calidad)
    can2.drawString(258, 428, conforme)
    can2.drawString(258, 411, condicional)
    can2.drawString(360, 445, peso_bruto)
    can2.drawString(360, 428, peso_tara)
    can2.drawString(360, 409, peso_neto)
    can2.drawString(410, 435, observaciones)
    can2.drawString(110, 372, direccion_procedencia)
    can2.drawString(430, 380, localidad_procedencia)
    can2.drawString(430, 367, provincia_procedencia)
    can2.drawString(95, 347, cod_planta_destino)
    can2.drawString(73, 330, direccion_destino)
    can2.drawString(365, 347, localidad_destino)
    can2.drawString(365, 330, provincia_destino)
    can2.drawString(355, 310, pagador_flete)
    can2.drawString(95, 295, camion)
    can2.drawString(95, 277, acoplado)
    can2.drawString(95, 262, kilometros)
    can2.drawString(243, 262, tarifa)
    can2.drawString(243, 277, tarifa_referencia)
    can2.drawString(300, 17, declaracion_juarada_nombre)
    can2.drawString(460, 17, declaracion_juarada_dni)
    can2.showPage()
    can2.save()

    # mover el archivo al comiezo dela pila de ejecucion
    packet2.seek(0)
    new_pdf2 = PdfFileReader(packet2)

    # --------------pagina3---------------
    packet3 = io.BytesIO()
    # crear un nuevo pdf con Reportlab
    can3 = canvas.Canvas(packet3, pagesize=A4)  # seria tamanio A4
    can3.setFont("Helvetica", 9)
    can3.drawString(190, 747, ctg)
    can3.drawString(300, 747, renspa)
    can3.drawString(510, 760, fecha)
    can3.drawString(185, 683, intermediario)
    can3.drawString(473, 683, cuit_intermediario)
    can3.drawString(185, 663, remitente_comercial)
    can3.drawString(473, 663, cuit_remitente_comercial)
    can3.drawString(185, 643, corredor_comprador)
    can3.drawString(473, 643, cuit_corredor_comprador)
    can3.drawString(185, 623, mercado_a_termino)
    can3.drawString(473, 623, cuit_mercado_a_termino)
    can3.drawString(185, 603, corredor_vendedor)
    can3.drawString(473, 603, cuit_corredor_vendedor)
    can3.drawString(185, 583, entregador)
    can3.drawString(473, 583, cuit_entregador)
    can3.drawString(185, 563, destinatario)
    can3.drawString(473, 563, cuit_destinatario)
    can3.drawString(185, 543, destino)
    can3.drawString(473, 543, cuit_destino)
    can3.drawString(185, 523, intermediario_flete)
    can3.drawString(473, 523, cuit_intermediario_flete)
    can3.drawString(185, 503, transportista)
    can3.drawString(473, 503, cuit_transportista)
    can3.drawString(185, 483, chofer)
    can3.drawString(473, 483, cuit_chofer)
    can3.drawString(140, 460, grano)
    can3.drawString(240, 460, tipo)
    can3.drawString(360, 460, cosecha)
    can3.drawString(498, 460, contrato)
    can3.drawString(133, 431, pesada_en_destino)
    can3.drawString(129, 412, kgs_estimados)
    can3.drawString(258, 445, declaracion_calidad)
    can3.drawString(258, 428, conforme)
    can3.drawString(258, 411, condicional)
    can3.drawString(360, 445, peso_bruto)
    can3.drawString(360, 428, peso_tara)
    can3.drawString(360, 409, peso_neto)
    can3.drawString(410, 435, observaciones)
    can3.drawString(110, 372, direccion_procedencia)
    can3.drawString(430, 380, localidad_procedencia)
    can3.drawString(430, 367, provincia_procedencia)
    can3.drawString(95, 347, cod_planta_destino)
    can3.drawString(73, 330, direccion_destino)
    can3.drawString(365, 347, localidad_destino)
    can3.drawString(365, 330, provincia_destino)
    can3.drawString(355, 310, pagador_flete)
    can3.drawString(95, 295, camion)
    can3.drawString(95, 277, acoplado)
    can3.drawString(95, 262, kilometros)
    can3.drawString(243, 262, tarifa)
    can3.drawString(243, 277, tarifa_referencia)
    can3.drawString(300, 17, declaracion_juarada_nombre)
    can3.drawString(460, 17, declaracion_juarada_dni)
    can3.showPage()
    can3.save()

    # mover el archivo al comiezo dela pila de ejecucion
    packet3.seek(0)
    new_pdf3 = PdfFileReader(packet3)

    # --------------pagina4---------------
    packet4 = io.BytesIO()
    # crear un nuevo pdf con Reportlab
    can4 = canvas.Canvas(packet4, pagesize=A4)  # seria tamanio A4
    can4.setFont("Helvetica", 9)
    can4.drawString(190, 747, ctg)
    can4.drawString(300, 747, renspa)
    can4.drawString(510, 760, fecha)
    can4.drawString(185, 683, intermediario)
    can4.drawString(473, 683, cuit_intermediario)
    can4.drawString(185, 663, remitente_comercial)
    can4.drawString(473, 663, cuit_remitente_comercial)
    can4.drawString(185, 643, corredor_comprador)
    can4.drawString(473, 643, cuit_corredor_comprador)
    can4.drawString(185, 623, mercado_a_termino)
    can4.drawString(473, 623, cuit_mercado_a_termino)
    can4.drawString(185, 603, corredor_vendedor)
    can4.drawString(473, 603, cuit_corredor_vendedor)
    can4.drawString(185, 583, entregador)
    can4.drawString(473, 583, cuit_entregador)
    can4.drawString(185, 563, destinatario)
    can4.drawString(473, 563, cuit_destinatario)
    can4.drawString(185, 543, destino)
    can4.drawString(473, 543, cuit_destino)
    can4.drawString(185, 523, intermediario_flete)
    can4.drawString(473, 523, cuit_intermediario_flete)
    can4.drawString(185, 503, transportista)
    can4.drawString(473, 503, cuit_transportista)
    can4.drawString(185, 483, chofer)
    can4.drawString(473, 483, cuit_chofer)
    can4.drawString(140, 460, grano)
    can4.drawString(240, 460, tipo)
    can4.drawString(360, 460, cosecha)
    can4.drawString(498, 460, contrato)
    can4.drawString(133, 431, pesada_en_destino)
    can4.drawString(129, 412, kgs_estimados)
    can4.drawString(258, 445, declaracion_calidad)
    can4.drawString(258, 428, conforme)
    can4.drawString(258, 411, condicional)
    can4.drawString(360, 445, peso_bruto)
    can4.drawString(360, 428, peso_tara)
    can4.drawString(360, 409, peso_neto)
    can4.drawString(410, 435, observaciones)
    can4.drawString(110, 372, direccion_procedencia)
    can4.drawString(430, 380, localidad_procedencia)
    can4.drawString(430, 367, provincia_procedencia)
    can4.drawString(95, 347, cod_planta_destino)
    can4.drawString(73, 330, direccion_destino)
    can4.drawString(365, 347, localidad_destino)
    can4.drawString(365, 330, provincia_destino)
    can4.drawString(355, 310, pagador_flete)
    can4.drawString(95, 295, camion)
    can4.drawString(95, 277, acoplado)
    can4.drawString(95, 262, kilometros)
    can4.drawString(243, 262, tarifa)
    can4.drawString(243, 277, tarifa_referencia)
    can4.drawString(300, 17, declaracion_juarada_nombre)
    can4.drawString(460, 17, declaracion_juarada_dni)
    can4.showPage()
    can4.save()

    # mover el archivo al comiezo dela pila de ejecucion
    packet4.seek(0)
    new_pdf3 = PdfFileReader(packet4)

    # leer pdf existente
    existing_pdf = PdfFileReader(
        open("media/cp_nuevas/" + data.numero + ".pdf", "rb"))
    output = PdfFileWriter()

    page = existing_pdf.getPage(0)
    page2 = existing_pdf.getPage(1)
    page3 = existing_pdf.getPage(2)
    page4 = existing_pdf.getPage(3)

    # unir el pdf creado con el existente
    page.mergePage(new_pdf.getPage(0))
    page2.mergePage(new_pdf2.getPage(0))
    page3.mergePage(new_pdf3.getPage(0))
    page4.mergePage(new_pdf3.getPage(0))

    output.addPage(page)
    output.addPage(page2)
    output.addPage(page3)
    output.addPage(page4)

    outputStream = open("media/CP" + data.numero + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()
