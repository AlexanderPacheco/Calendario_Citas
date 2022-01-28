from behave import *
from users.models import Paciente
from cita.models import Cita, Receta
from datetime import datetime, timedelta, date
'''
@given('Existen citas creadas')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos Citas en la BD
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

    fecha = datetime.now().strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()  
    pass
'''
@when('Cuando se pulse el boton agregar receta')
def step_impl(context):
    cita= Cita.objects.all()[0]
    Receta(detalle_receta='Tomar 2 pastillas de panadol cada 8 horas por 10 días', cita=cita).save()
    
    assert len(Receta.objects.all())==1

@then('Se crea una nueva receta para la cita')
def step_impl(context):
    #Se observan los resultados
    receta = Receta.objects.all()
    
    assert receta[0].detalle_receta == "Tomar 2 pastillas de panadol cada 8 horas por 10 días"

    