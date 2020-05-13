from django.db import models

# Managers
from .managers import AutorManager

class Persona(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=20
    )
    edad = models.PositiveIntegerField()

    class Meta: 
        abstract = True

    def __str__(self):
        return self.nombre + ' ' + self.apellidos

class Autor(Persona):
    seudonimo = models.CharField(
        'Seudonimo',
        max_length=30,
        blank=True
    )

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    """ Utilizamos el manager que hemos creado """
    objects = AutorManager()
