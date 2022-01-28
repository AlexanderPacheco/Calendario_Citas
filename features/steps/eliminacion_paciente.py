from behave import *
from users.models import Paciente

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
    
    

@when('Cuando se pulse el boton eliminar')
def step_impl(context):
    #Accion que realiza el sistema o el usuario
    #Se elimina un paciente
    paciente = Paciente.objects.get(correo='pedrogracia@gmail.com')
    assert paciente.delete()[0]== 1
      
    

@then('Se elimina el paciente')
def step_impl(context):
    #Se observan los resultados
    paciente = Paciente.objects.all()
    assert paciente.count() == 1
    
    
    

