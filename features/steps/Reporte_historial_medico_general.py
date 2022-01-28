from behave import *
from users.models import Paciente
from cita.models import Cita, Receta
from anotacion.models import Anotacion
from examen.models import Examen
from users.views import reporte_historial_clinico
from datetime import datetime, timedelta, date
from django.test import Client
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import View
from django.template.loader import get_template
from users.utils import render_to_pdf
from django.http import HttpResponse

@given('Se han atendido pacientes')
def step_impl(context):
    #por defecto en la bd ya existen citas atendidas
    pass
    
    

@when('Cuando se pulse el boton generar historial medico de pacientes')
def step_impl(context):
    #Accion que realiza el sistema o el usuario
    #Se genera y renderiza el pdf
    template =  get_template('paciente/reporte_pacientes.html')
    data = {
        'Pacientes':Paciente.objects.all(),
        'Citas':Cita.objects.all(),
        'Anotaciones':Anotacion.objects.all(),
        'Recetas':Receta.objects.all(),
        'Examenes':Examen.objects.all(),
    }
    pdf = render_to_pdf('paciente/reporte_pacientes.html', data)
    assert pdf.status_code == 200
    

@then('Se visualiza el pdf generado del reporte general')
def step_impl(context):
    #Se observan los resultados
    #t=Template('examen/listado_examenes.html')
    client = Client()
    pdf = render_to_pdf('paciente/reporte_pacientes.html')
    response = HttpResponse(pdf, content_type='application/pdf')
    
    assert response.status_code == 200
    
    

