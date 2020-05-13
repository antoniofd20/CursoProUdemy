from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'libros/',
        views.ListaLibros.as_view(),
        name='libros'
    ),
    path(
        'libros-trg/',
        views.ListaLibrosTrg.as_view(),
        name='libros-trg'
    ),
    path(
        'libros-categoria/',
        views.ListLibrosCategoria.as_view(),
        name='libros-categoria'
    ),
    path(
        'detalle/<pk>/',
        views.LibroDetailView.as_view(),
        name='detalle'
    ),
    path(
        'categorias/',
        views.ListCategoriasLibros.as_view(),
        name='categorias'
    )
]
