from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor
# Create your views here.


class ListAutores(ListView):
    template_name = 'autor/lista_autores.html'
    context_object_name = 'lista_autores'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        """ Manager listar_autores """
        #return Autor.objects.buscar_autor(palabra_clave)
        #return Autor.objects.buscar_autor2(palabra_clave)
        #return Autor.objects.buscar_autor3(palabra_clave)
        return Autor.objects.buscar_autor(palabra_clave)
   
