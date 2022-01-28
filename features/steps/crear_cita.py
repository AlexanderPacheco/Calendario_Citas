from behave import *
from users.models import Paciente
from cita.models import Cita
from datetime import datetime, timedelta, date
'''
@given('Existen pacientes registrados')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos pacientes en la BD
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
    pass
 '''   
    

@when('Cuando se pulse el boton agendar cita')
def step_impl(context):
    #Accion que realiza el sistema o el usuario
    #Se elimina un paciente
    paciente = Paciente.objects.get(correo='pedrogracia@gmail.com')
    cita = Cita(
        fecha_cita="1996-11-7",
        hora_cita="15:30",
        estado="PENDIENTE",
        comentario="Prueba BDD",
        paciente=paciente
    )
    cita.save()
    assert len(Cita.objects.all())==1
    
      
    

@then('Se crea una nueva cita para el paciente')
def step_impl(context):
    #Se observan los resultados
    cita = Cita.objects.all()
    assert cita[0].paciente.correo == 'pedrogracia@gmail.com'
    
    
    

