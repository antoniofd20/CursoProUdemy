from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView,
)
# Importar models
from .models import Prueba
# Importamos formularios
from .forms import PruebaForm

# Create your views here.

class PruebaView(TemplateView):
    #Mando a llamar el template que quiero
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    template_name = "home/listas.html"
    context_object_name = 'ListaNumeros'
    queryset = ['0', '10', '20', '30']

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    #fields = ['titulo', 'subtitulo', 'cantidad']
    form_class = PruebaForm
    seccess_url = '/'
