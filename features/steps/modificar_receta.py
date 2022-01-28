from behave import *
from users.models import Paciente
from datetime import datetime, timedelta, date
from cita.models import Cita, Receta
from django.test import TestCase

@given('Existen recetas registradas1')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos receta en la BD
    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    paciente=Paciente.objects.create(
        nombre = 'Jose',
        apellido = 'Lopez',
        telefono = '48484848',
        telefono_emergencia = '48484849',
        correo = 'jose@gmail.com',
        fecha_nacimiento = '2020-09-25',
        direccion = 'direccion de domicilio',
        descripccion = 'Persona',
        sexo = 'MASCULINO',
    )
    cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba bdd', paciente=paciente).save()  

    Receta(detalle_receta='Tiene fiebre', cita=cita, fecha='2020-09-23').save()
    assert len(Receta.objects.all())==1
    
    

@when('Cuando pulse el boton modificar receta1')
def step_impl(context):
    #Simula que se selecciono una receta
    assert len(Receta.objects.all())==1
      
    

@then('Modifico mis campos y guardo1')
def step_impl(context):
    #Modificamos la receta y guardamos
    getreceta= Receta.objects.all()[0]
    getreceta.detalle_receta = "Edicion" #Modificando receta
    getreceta.save()
    assert getreceta.detalle_receta=='Edicion'
    
    
