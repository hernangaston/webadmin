from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Empresa


# Create your views here.
class ViewEmpresa(TemplateView):
    model = Empresa
    queryset = Empresa.objects.all()
