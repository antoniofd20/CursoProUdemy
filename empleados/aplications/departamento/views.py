from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from aplications.persona.models import Empleado
from .models import Departamento
from django.urls import reverse_lazy

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name='lista'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('persona_app:inicio')

    def form_valid(self, form):
        """Crear instancia de una clave foranea"""
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name'],
        )
        depa.save()

        """Para recuperar los datos que se ingresan en el formulario"""
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        """"Para registar en el modelo empleado con la ORM de Django
        La función create es la que me permite hacer esto"""
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento=depa,
        )
    
        
