from django import forms
from django.forms import ModelForm
from anotacion.models import Anotacion
from .models import Receta

class CardAnotacion_form(ModelForm):
    
    class Meta:
        model = Anotacion
        fields = ['descripcion']

#from anotacion.models import models
class AnotacionForm(forms.ModelForm):
    class Meta:
        model = Anotacion
        fields = [
            'descripcion',
        ]
        labels = {
            'descripcion': 'Descripción',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form_control', 'cols': 15, 'rows': 3}),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'detalle_receta',
        ]
        labels = {
            'detalle_receta': 'Detalle de la Receta',
        }
        widgets = {
            'detalle_receta': forms.Textarea(attrs={'class': 'form_control', 'cols': 60, 'rows': 8}),
        }

class recetaOffForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'detalle_receta'
            ]
        labels = {
            'detalle_receta': 'Descripcion:'
        }
        widgets = {
            'detalle_receta': forms.Textarea(attrs={'class':'form-control'})
        }
'''
class receta2Form(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'fecha',
            'detalle_receta',
            'paciente',
            ]
            '''