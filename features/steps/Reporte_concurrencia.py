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
from django.db.models import Sum, Count

@given('Se han registrado citas')
def step_impl(context):
    paciente=Paciente.objects.create(
        nombre = 'Henry',
        apellido = 'Leon',
        telefono = '12345678',
        telefono_emergencia = '12345679',
        correo = 'henrisco@gmail.com',
        fecha_nacimiento = '2020-12-12',
        direccion = 'zona 6',
        descripccion = 'Joven guapo :3',
        sexo = 'MASCULINO',
    )

    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()  
    pass
    
    

@when('Cuando se pulse el boton generar reporte concurrencia')
def step_impl(context):
    #Accion que realiza el sistema o el usuario
    #Se genera y renderiza el pdf
    template =  get_template('citas/concurrencia.html')
    div=Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('-total').count()
    prom=0
    if div!=0:
        prom=Cita.objects.all().annotate(total=Count('estado')).order_by('-total').count()/ div
        
    data = {
             'Citas':Cita.objects.all(),
             'Total':Cita.objects.count(),
             'Fecha_concurrido':Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('-total')[:1],
             'Citas_atendidas': Cita.objects.filter(estado='ATENDIDA').annotate(total=Count('estado')).order_by('-total').count(),
             'Citas_pendientes': Cita.objects.filter(estado='PENDIENTE').annotate(total=Count('estado')).order_by('-total').count() ,
             'Citas_canceladas' : Cita.objects.filter(estado='CANCELADA').annotate(total=Count('estado')).order_by('-total').count(),
             'Promedio_citas' :prom,
             'Menos_concurrido':Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('total')[:1],
        }
    pdf = render_to_pdf('citas/concurrencia.html', data)
    assert pdf.status_code == 200
    

@then('Se visualiza el pdf generado del reporte de concurrencia')
def step_impl(context):
    #Se observan los resultados
    #t=Template('examen/listado_examenes.html')
    client = Client()
    pdf = render_to_pdf('citas/concurrencia.html')
    response = HttpResponse(pdf, content_type='application/pdf')
    
    assert response.status_code == 200
    
    

