from django import forms
from django.forms import ModelForm
from users.models import Paciente

#from anotacion.models import models
class pacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'telefono_emergencia',
            'correo',
            'fecha_nacimiento',
            'direccion',
            'descripccion',
            'sexo',
            ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Telefono',
            'telefono_emergencia': 'Telefono Emergencia',
            'correo': 'Correo',
            'fecha_nacimiento': 'Fecha De Nacimiento',
            'direccion': 'Direccion',
            'descripccion': 'Descripcion',
            'sexo': 'Sexo',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'telefono_emergencia': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'descripccion': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.Select(attrs={'class':'form-control'})
        }
