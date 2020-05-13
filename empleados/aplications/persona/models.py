from django.db import models
# Importamos a departamento
from aplications.departamento.models import Departamento
# De aplicacion de terceros
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    JOB_CHOICES =(
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    # Modelo para tabla empleado
    # Nombres
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', 
        max_length=120,
        blank=True
        )
    # Solo podrá escojer entre algunas opciones con choices
    # Al pasarle la lista de posibles trabajos tendrá una longitud maxima de 1
    job = models.CharField('Cargo', max_length=1, choices=JOB_CHOICES)
    # Para hacer una clave foranea solo hay que importar y crear de la siguiente forma
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Para un campo de imagen 
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)

    hoja_vida = RichTextField(blank=True)

    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['last_name', 'first_name'] #Ordenar -----importante


    def __str__(self):
        return self.last_name + ' ' + self.first_name