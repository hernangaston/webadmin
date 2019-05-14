from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .viewsets import DestinatarioViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'list', DestinatarioViewSet)

app_name = 'destinatario'
urldestinatario = [
    path('api/', include(router.urls)),
]