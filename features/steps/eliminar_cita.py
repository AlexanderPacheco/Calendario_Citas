from behave import *
from users.models import Paciente
from datetime import datetime, timedelta, date
from cita.models import Cita
from django.test import TestCase

@given('Existen citas registradas')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos citas en la BD
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    paciente=Paciente.objects.create(
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
    Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()  
    pass
    
    

@when('Cuando se pulse el boton eliminar cita')
def step_impl(context):
    citas= Cita.objects.all()
    assert citas[0].delete()[0] == 1 
      
    

@then('Se elimina la cita')
def step_impl(context):
    #Se observan los resultados
    cita = Cita.objects.all()
    assert cita.count() == 0
    
    
    