from django.db import models

from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para el modelo autor """

    def listar_autores(self):
        return self.all()

    def buscar_autor(self, kword):
        resultado = self.filter( #Filtro sencillo
            nombre__icontains=kword
        ).order_by('nombre') # Ordenar por el atributo que se desea
        return resultado

    def buscar_autor2(self, kword):
        resultado = self.filter(
            # Sentencia OR de la siguiente manera.
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado

    def buscar_autor3(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude( # Hacer exclusiones y tambien se puede hacer un filtro sobre otro
            Q(edad=72) | Q(nacionalidad='España')
        )
        return resultado

    def buscar_autor4(self, kword):
        resultado = self.filter(
            # gt se usa para decir que sea mayor que y lt menor que.
            # Sentencia AND se usa solo con una coma
            edad__gt=40,
            edad__lt=80
        ).order_by('apellidos', 'nomnre')
        return resultado