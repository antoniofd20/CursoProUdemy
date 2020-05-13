from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    # Vista de inicio
    path(
        '', 
        views.InicioView.as_view(),
        name='inicio'
    ),
    # Lista de los empleados
    path(
        'lista-empelados/', 
        views.ListAllEmpleados.as_view(), 
        name='lista-empelados'
    ),
    path(
        'lista-empelados-admin/', 
        views.ListEmpleadoAdmin.as_view(), 
        name='lista-admin'
    ),
    #Ver la vista ****
    path(
        'listar-por-departamento/<short_name>/', 
        views.ListByArea.as_view(),
        name='lista-por-departamento'
        ),
    path('listar-por-trabajo/<job>/', views.ListByJob.as_view()),
    path('buscar-empleado/', views.ListaEmpleadosByKword.as_view()),
    path('habilidades/', views.ListHabilidadesEmpleado.as_view()),

    #obligatorio el pk en detailview
    path('ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='ver-empleado'
        ),

    #Create view
    path(
        'add-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='add'),

    #Update view
    path(
        'editar-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='editar-empleado'
        ),

    #Delete View
    path(
        'eliminar-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name="eliminar-empleado"
        ),
]