# Primero se importan cosas de Python
from datetime import date  # Utilixar fechas ¡Importante investigar, sabados y mes!
# Despues de django
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.http import HttpResponseRedirect
# Por ultimo de mi aplicacion propia
from .models import Prestamo
from .forms import PrestamoForm, MultiplePrestamoForm


# Create your views here.

class PromedioView(ListView):
    template_name = 'lector/promedio.html'
    context_object_name = 'promedio'

    def get_queryset(self):
        id = self.request.GET.get("kword", '')
        return Prestamo.objects.libro_promedio_edades(id, 2)

class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        """ Registrar un prestamo con create """
        """ Crea una nueva instancia siempre (nuevo id) """
        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestamo = date.today(), #Se registra la fecha de hoy
        #     devuelto = False
        # )

        """ Registrar un prestamo con save """
        """ Se usa para actualizar un registro """
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(), #Se registra la fecha de hoy
            devuelto = False
        )
        prestamo.save()

        libro = form.cleaned_data['libro']
        libro.stok = libro.stok - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)


class RegistrarPrestamo2(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        """ Validar si el registro que se quiere hacer no existe ya """
        # created es una variable booleana
        # obj es donde esta el registro
        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults = {
                'fecha_prestamo': date.today()
            }
        )

        if created:
            return super(RegistrarPrestamo2, self).form_valid(form)
        else:
            return HttpResponseRedirect('/libros/') # Va la pagina http://127.0.0.1:8000/libros/
            #return HttpResponseRedirect('libros/') # Va la pagina http://127.0.0.1:8000prestamo/validacion/libros/


class RegistrarPrestamoMultiple(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self, form):
        
        prestamos = [] 

        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(), #Se registra la fecha de hoy
                devuelto = False
            )
            # Se crea un array de registros
            prestamos.append(prestamo)

        # bulk_create realiza varios registros a partir de una lista
        Prestamo.objects.bulk_create(
            prestamos
        )


        return super(RegistrarPrestamoMultiple, self).form_valid(form)
