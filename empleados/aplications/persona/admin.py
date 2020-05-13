from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    # Me va a enlistar en tablas con lo que le indique
    list_display = (
        'last_name', 
        'first_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    #Funcion para que funcione el full_name
    def full_name(self, obj):
        #Toda la operacion que necesite
        return obj.first_name + ' ' + obj.last_name
    # Colocar un buscador y que lo haga por el parametro que queramos
    search_fields = (
        'last_name',
    )
    # Filtrar por el parametro que se desee
    list_filter =('job','habilidades',)

    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)