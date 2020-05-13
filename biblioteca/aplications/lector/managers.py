from django.db import models

from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower
import datetime

class PrestamoManager(models.Manager):
    """Procedimiento para prestamo"""

    def libro_promedio_edades(self, id_libro):
        resultado = self.filter(
            libro__id=id_libro
        ).aggregate(
            promedio_edad=Avg('lector__edad')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values( #Regresa un diccionario
            'libro', #Cuantas veces he prestado determinado libro
            'lector' #Cuantas veces lo he prestado a determinado lector
        ).annotate( #Regresa una lista (QuerySet)
            num_prestados=Count('libro'),
            titulo=Lower('libro__titulo'), #Aqui podemos mostrar cualquier dato del modelo libro
        )

        for r in resultado:
            print('===========')
            print(r, r['num_prestados']) #Se ingresa asi por que es un diccionario, en una lista seria r.num_prestados
        return resultado
