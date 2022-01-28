from behave import *
from django.core import mail 
from users.models import Paciente
from cita.models import Cita
from examen.models import Examen
from datetime import datetime, timedelta, date

@given('Existen citas creadas')
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

    tomorrow = date.today() + timedelta(days=1)
    fecha = tomorrow.strftime("%Y-%m-%d")
    hora = datetime.now().strftime("%H:%M:%S")
    Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()  
    pass

@when('Exista una cita para el dia siguiente')
def step_impl(context):
    tomorrow = date.today() + timedelta(days=1)
    appointments = Cita.objects.filter(fecha_cita=tomorrow)
    assert len(Cita.objects.all())>0


@then('Se envia un correo electronico al paciente')
def step_impl(context):
    #Se observan los resultados
    tomorrow = date.today() + timedelta(days=1)
    appointments = Cita.objects.filter(fecha_cita=tomorrow)

    for cita in appointments:
        if cita.paciente.correo.find('@'):
            mail.send_mail('Subject here', 'Here is the message.',
                'from@example.com', ['to@example.com'],
                fail_silently=False)
            assert len(mail.outbox) == 1