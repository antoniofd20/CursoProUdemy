from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view(), name='prueba'),
    path('lista/', views.PruebaListView.as_view(), name='lista'),
    path('lista_prueba/', views.ListarPrueba.as_view(), name='lista_prueba'),
    path('add/', views.PruebaCreateView.as_view(), name='add'),
]