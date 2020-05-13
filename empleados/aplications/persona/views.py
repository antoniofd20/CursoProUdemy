from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)
from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """Vista que carga la pantalla de inicio"""
    template_name = 'inicio.html'


# 1- Listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    """ Lista de todos los empleados de la empresa """
    template_name = 'persona/lista_all.html'
    """Realizar paginaciones RECOMENDADO ?page=1 """
    ordering = 'first_name'
    context_object_name='lista'
    paginate_by = 5

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            last_name__icontains=palabra_clave,
        )
        return lista

class ListEmpleadoAdmin(ListView):
    template_name = 'persona/lista_editar.html'
    ordering = 'first_name'
    context_object_name='lista'
    paginate_by = 5
    model = Empleado
    

# 2- Listar todos los empleados que pertenecen a un area de la empresa}
class ListByArea(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/lista_departamento.html'
    context_object_name='lista'

    """ Con queryset en vez de model podemos obtener un solo atributo de los registros de nuestro modelo,
    ideal para usar en un filtro como lo haremos a continuación
    Empleado.objects.filter nos ayuda para hacer un filtro OJO, se tiene que escribir tal cual """

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
        departamento__short_name = area
        )
        return lista

# 3- Listar todos los empleados por trabajo    
class ListByJob(ListView):
    """ Lista empleados de un area """
    
    template_name = 'persona/lista_trabajo.html'

    def get_queryset(self):
        area = self.kwargs['job']
        """
        JOB_CHOICES =(
            ('0', 'CONTADOR'),
            ('1', 'ADMINISTRADOR'),
            ('2', 'ECONOMISTA'),
            ('3', 'OTRO'),
        )
        """
        lista = Empleado.objects.filter(
            job = area
        )
        return lista

# 4- Listar todos los empleados por palabra clave
""" IMPORTANTE este es el filtro mas usado, funciona por medio de un formulario """
class ListaEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave """
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

# 5- Listar habilidades de un empleado
""" Listar atributos de muchos a muchos """
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    """def get_queryset(self):
        nombre = self.request.GET.get("kword",'')
        
        empleado = Empleado.objects.get(first_name='Raymundo')
        return empleado.habilidades.all()"""

    def queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(first_name=palabra_clave)
        lista = empleado.habilidades.all()
        if lista:
            return lista
        else:
            lista = ['No hay habilidades que mostrar']
            return lista
        #return lista


class EmpleadoDetailView(DetailView):
    template_name = "persona/detail_empleado.html"
    model = Empleado



#Formulario para crear un nuevo empleado ¡Importante!
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado 
    #fields = ('__all__')
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:lista-empelados')

    #Validar los datos del formulario y crear el full name
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = "persona/updateview.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades'
    ]
    success_url = reverse_lazy('persona_app:lista-empelados')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:lista-admin')
