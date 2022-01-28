from django import forms
from django.forms import ModelForm
from anotacion.models import Anotacion

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

