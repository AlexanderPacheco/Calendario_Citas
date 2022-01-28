from behave import *
from users.models import Paciente
from cita.models import Cita
from examen.models import Examen
from examen.views import ExaminationListView
from datetime import datetime, timedelta, date
from django.test import Client
from django.urls import reverse
from django.shortcuts import render

@given('Se han mandado a realizar examenes')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos Examenes en la BD
    
    user = Paciente(
            nombre = 'Juan',
            apellido = 'Perez',
            telefono = '12345678',
            telefono_emergencia = '12345679',
            correo = 'juanperez@gmail.com',
            fecha_nacimiento = '2020-12-12',
            direccion = 'direccion de domicilio',
            descripccion = 'Persona de la tercera edad con problemas de respiracion',
            sexo = 'MASCULINO',
            )
    user.save()
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    cita=Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=user).save()
    Examen(cita=cita, descripcion='Radiografía').save()
    user = Paciente(
            nombre = 'Pedro',
            apellido = 'Garcia',
            telefono = '12345789',
            telefono_emergencia = '12345159',
            correo = 'pedrogracia@gmail.com',
            fecha_nacimiento = '2020-12-11',
            direccion = 'direccion de domicilio',
            descripccion = 'Persona con alergia a paracetamol',
            sexo = 'MASCULINO',
            )
    user.save()
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    cita=Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=user).save()
    Examen(cita=cita, descripcion='Rayos X').save()
    pass
    
    

@when('Cuando se visite la pagina listado_examenes')
def step_impl(context):
    #Accion que realiza el sistema o el usuario
    #visita la pagina y obtiene el listado de pacientes
    Examenes=Examen.objects.all()
    data={
        'lista_examenes':Examenes
    }
    client = Client()
    response = render('GET', 'examen/listado_examenes.html',data)
    #response = client.get(reverse('ExaminationListView',data))
    #print(response.content)
    assert response.status_code == 200
      
    

@then('Se ven los examenes que se han realizado')
def step_impl(context):
    #Se observan los resultados
    #t=Template('examen/listado_examenes.html')
    client = Client()
    response = ExaminationListView('GET')
    assert response.status_code == 200
    
    

