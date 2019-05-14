from rest_framework import viewsets
from .models import RemitenteComercial
from .serializers import RemitenteComercialSerializer

# ViewSets define the view behavior.
class RemitenteComercialViewSet(viewsets.ModelViewSet):
    queryset = RemitenteComercial.objects.all()
    serializer_class = RemitenteComercialSerializer


    