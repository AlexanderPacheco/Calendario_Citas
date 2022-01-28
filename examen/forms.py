from django import forms
from django.forms import ModelForm
from .models import Examen

class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = [
            'descripcion',
        ]
        labels = {
            'descripcion': 'Descripción del examen a realizarse',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form_control', 'cols': 15, 'rows': 3}),
        }