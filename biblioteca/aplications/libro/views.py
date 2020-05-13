from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Libro, Categoria

# Create your views here.

class ListaLibros(ListView):
    template_name = 'libro/lista_libros.html'
    context_object_name = 'libros'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')

        """ Capturamos las fechas """
        f1 = self.request.GET.get("fecha1", '')
        f2 = self.request.GET.get("fecha2", '')

        """ Manager listar_autores """
        #return Libro.objects.listar_libros()
        #return Libro.objects.buscar_libros(palabra_clave)

        if f1 and f2:
            return Libro.objects.buscar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.objects.buscar_libros(palabra_clave)

class ListaLibrosTrg(ListView): # Filtro con trigram
    template_name = 'libro/lista_libros.html'
    context_object_name = 'libros'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')

        return Libro.objects.listar_libros_trg(palabra_clave)

class ListLibrosCategoria(ListView):
    context_object_name = 'categorias'
    template_name = 'libro/lista_categoria.html'

    def get_queryset(self):
        categoria = self.request.GET.get("categoria", '')

        if categoria:
            return Libro.objects.listarLibro_categoria(categoria)
        else:
            return Libro.objects.listarLibro_categoria('0')

class ListCategoriaDeAutor(ListView):

    def get_queryset(self):
        return Categoria.objects.categoria_por_autor('1')


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"

class ListCategoriasLibros(ListView):
    context_object_name = 'categorias'
    template_name = 'libro/lista_categorias.html'

    def get_queryset(self):
        return Categoria.objects.listar_categoria_libros()
