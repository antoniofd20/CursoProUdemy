from django.db import models
from django.db.models import Q

# Create your models here.
class Persona(models.Model):

    full_name = models.CharField('Nombres', max_length=50)
    pais = models.CharField('País', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)

    class Meta:

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

        """ Si nosotros no queremos que se guarde con un
        nombre determinado en la base de datos, sino con
        el nombre que nosotros queramos es con lo siguiente"""
        db_table = 'persona' #Con este nombre aparece en la db

        """ Hacer que no se repita una combinacion """
        unique_together = ['pais', 'apelativo']

        """ Validaciones simples """
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
        abstract = True # Persona si es un modelo pero no es necesario que lo cree
        # dentro de la base de datos 

    def __str__(self):

        return self.full_name

class Empleados(Persona): # Herencia de persona
    empleo = models.CharField('Empleo', max_length=30)

class Cliente(Persona):
    email = models.EmailField('Email')
