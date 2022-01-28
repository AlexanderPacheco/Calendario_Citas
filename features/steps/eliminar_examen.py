from behave import *
from datetime import datetime, timedelta, date
from examen.models import Examen
from users.models import Paciente
from cita.models import Cita
from django.test import TestCase

@given('Existen examenes registrados2')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos examenes en la BD
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    paciente=Paciente.objects.create(
        nombre = 'Jhon',
        apellido = 'Nieve',
        telefono = '48484848',
        telefono_emergencia = '48484849',
        correo = 'jhon@gmail.com',
        fecha_nacimiento = '2020-12-12',
        direccion = 'El norte castillo negro',
        descripccion = 'Guardian',
        sexo = 'MASCULINO',
    )
    cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()

    Examen(descripcion='Examen de Sangre', cita_id=cita, fecha='2020-09-23').save()

    assert len(Examen.objects.all())==1
    
    

@when('Cuando se pulse el boton eliminar examen2')
def step_impl(context):
    #Simula que se selecciono un examen
    assert len(Examen.objects.all())==1
      
    

@then('Se elimina el examen2')
def step_impl(context):
    #Modificamos examen y guardamos
    getExam = Examen.objects.all()[0]
    getExam.delete() #Eliminando Examen
    assert len(Examen.objects.all())==0
    
    
