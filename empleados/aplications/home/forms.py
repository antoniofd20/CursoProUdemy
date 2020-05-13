from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        """Agregar personalizacion a los formularios"""
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder ':'Ingrese texto'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs = {
                    'placeholder':'Ingrese texto'
                }
            ),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')

        return cantidad