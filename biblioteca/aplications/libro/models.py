from django.db import models
from django.db.models.signals import post_save

# apps de terceros
from PIL import Image

# from local apps
from aplications.autor.models import Autor

# Se importa el manager que creamos
from .managers import LibroManager, CategoriaManager

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(
        max_length=30
    )

    objects = CategoriaManager()

    def __str__(self):
        return str(self.id) + '-' + self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(
        Autor
    )
    titulo = models.CharField(
        max_length=50
    )
    fecha = models.DateField(
        'Fecha de lanzamiento'
    )
    portada = models.ImageField(
        upload_to='img/portadas'
    )
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)

    # Aquí esta el manager agregado
    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro' #Para cambiar nombre en el admin
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']

    def __str__(self):
        return str(self.id) + '-' + self.titulo


def optimizar_img(sender, instance, **kwargs):
    print(" ================== ")
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)

post_save.connect(optimizar_img, sender=Libro )