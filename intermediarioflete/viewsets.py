from rest_framework import viewsets
from .models import IntermediarioFlete
from .serializers import IntermediarioFleteSerializer

# ViewSets define the view behavior.
class IntermediarioFleteViewSet(viewsets.ModelViewSet):
    queryset = IntermediarioFlete.objects.all()
    serializer_class = IntermediarioFleteSerializer


    