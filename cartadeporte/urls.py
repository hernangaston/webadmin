from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.views.generic import TemplateView
from .viewsets import CartaDePorteViewSet
from .views import CartaDePorteListApiView, CartaDePorteRetrieveApiView, CartaDePorteListView, \
     GeneratePDF, UploadFile, CartaDePorteCreate, CartaViewSet, IndexView

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cartas', CartaDePorteViewSet)

app_name = 'cartadeporte'
urlcp = [
    path('api/', include(router.urls)),
    path('carta/<pk>/', CartaDePorteRetrieveApiView.as_view()),
    path('cartaslist/', CartaDePorteListView.as_view(), name="cplist"),
    path('cartaslist/generarpdf/<int:pk>', GeneratePDF.as_view(), name="pdfcp"),
    url(r'^fileupload/(?P<filename>[^/]+)$', UploadFile.as_view()),
    path('create/', CartaDePorteCreate.as_view(), name="create"),
    path('', IndexView.as_view(), name="index"),
]