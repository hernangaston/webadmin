from django.urls import path, include
from rest_framework import routers
from .viewsets import EmpresasViewSet, UserAuthViewSet
from .views import UserListView



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'empresas', EmpresasViewSet)
router.register(r'auth', UserAuthViewSet)


urlempresa = [
    path('api/', include(router.urls)),
    path('users/', UserListView.as_view(), name="users")
]