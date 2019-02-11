from django.urls import path, include
from rest_framework import routers
from .viewsets import EmpresaViewSet, UserViewSet
from .views import ViewEmpresas, CreateEmpresa, ModificarEmpresa


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'users', UserViewSet)

urlempresa = [
    path('api/', include(router.urls)),
    path('', ViewEmpresas.as_view()),
    path('create/', CreateEmpresa.as_view()),
    path('modificar/<int:pk>', ModificarEmpresa.as_view()),
]