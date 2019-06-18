from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from .models import CartaDePorte
from .serializers import CartaDePorteSerializer

# ViewSets define the view behavior. 
#  ESTA CLASE NOS PERMITE HACER CRUD SOBRE NUESTRO MODELO

class CartaDePorteViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = CartaDePorte.objects.all()
    serializer_class = CartaDePorteSerializer

    def create(self, request):
        #print(request.data)
        cp = CartaDePorteSerializer(data=request.data)
        if cp.is_valid():
            cp.save()
            print(cp)
            return Response(status=status.HTTP_201_CREATED)
   
