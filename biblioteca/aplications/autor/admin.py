from django.contrib import admin
#Se importa mi modelo
from .models import Autor
# Register your models here.
admin.site.register(Autor)