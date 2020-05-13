from django.db import models

from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity
import datetime

""" Siempre que se crea un manager no olvides
    agregarlo en el modelo """
class LibroManager(models.Manager):
    """ Managers para el modelo libro """

    def listar_libros(self):
        return self.all()

    def listar_libros_trg(self, kword):

        if kword:
            resultado = self.filter(
                titulo__trigram_similar = kword,
            )
            return resultado

        else:
            return self.all()[:10]



    def buscar_libros(self, kword):
        resultado = self.filter( #Filtro sencillo
            titulo__icontains=kword,
        ).order_by('titulo') # Ordenar por el atributo que se desea

        return resultado

    def buscar_libros2(self, fecha1, fecha2):

        """ Se transforma a formato correcto """
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter( #Filtro sencillo
            fecha__range=(date1, date2),
        ).order_by('titulo') # Ordenar por el atributo que se desea
        print(date1)
        print(date2)
        return resultado

    def listarLibro_categoria(self, categoria):

        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        """Agregar un nuevo autor"""
        libro.autores.add(autor)
        """Eliminar un autor
        libro.autores.remove(autor)"""

        return libro

    def num_libros_prestados(self):
        resultado = self.annotate( #Regresa una lista (QuerySet)
            num_prestados=Count('libro')
        )

        for r in resultado:
            print('===========')
            print(r, r.num_prestados) #Se ingresa asi por que es un diccionario, en una lista seria r.num_prestados
        return resultado

    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado

class CategoriaManager(models.Manager):

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__id=autor
        ).distinct() # Para que no repita registros

    def listar_categoria_libros(self):
        """resultado = self.annotate(
            num_libros=Count('categoria_libro')
        ).order_by('id')
        for r in resultado:
            print("******")
            print(r, r.num_libros)"""
        return  self.annotate(
            num_libros=Count('categoria_libro')
        ).order_by('id')
