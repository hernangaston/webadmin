from django.urls import path, include
from rest_framework import routers
from .viewsets import EmpresaViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'empresa', EmpresaViewSet)


urlempresa = [
    path('', include(router.urls)),
]