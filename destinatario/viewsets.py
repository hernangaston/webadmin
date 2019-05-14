from rest_framework import viewsets
from .models import Destinatario
from .serializers import DestinatarioSerializer

# ViewSets define the view behavior.
class DestinatarioViewSet(viewsets.ModelViewSet):
    queryset = Destinatario.objects.all()
    serializer_class = DestinatarioSerializer


    