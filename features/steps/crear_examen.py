from behave import *
from users.models import Paciente
from cita.models import Cita
from examen.models import Examen
from datetime import datetime, timedelta, date

@given('Existen citas creadass')
def step_impl(context):
    #ponemos el sistema en un estado inicial.
    #Ingresamos Citas en la BD
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

@when('Cuando se pulse el boton generar examen clinico')
def step_impl(context):
    cita= Cita.objects.all()[0]
    Examen(cita=cita, descripcion='Radiografía').save()
    
    assert len(Examen.objects.all())==1

@then('Se crea un nuevo examen para la cita del paciente asociado')
def step_impl(context):
    #Se observan los resultados
    examen = Examen.objects.all()
    
    assert examen[0].descripcion == "Radiografía"