from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'promedio/<pk>/',
        views.PromedioView.as_view(),
        name='promedio'
    ),
    path(
        'prestamo/',
        views.RegistrarPrestamo.as_view(),
        name='prestamo'
    ),
    path(
        'prestamo/validacion/',
        views.RegistrarPrestamo2.as_view(),
        name='prestamo-validacion'
    ),
    path(
        'prestamo/varios/',
        views.RegistrarPrestamoMultiple.as_view(),
        name='prestamo-varios'
    ),
]
