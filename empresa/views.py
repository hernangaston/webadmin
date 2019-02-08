from django.shortcuts import render
from django.views.generic import View, ListView, TemplateView, CreateView
from .models import Empresa


# Create your views here.
class ViewEmpresa(ListView):
    template_name="index.html"
    model = Empresa

class CreateEmpresa(CreateView):
    template_name = "crear_empresa.html"
    model = Empresa
    fields = '__all__'
