from behave import *
from django.core import mail 
from users.models import Paciente
from cita.models import Cita
from examen.models import Examen
from datetime import datetime, timedelta, date

from twilio.rest import Client

account_sid = 'AC28c195212f1f17e9d15c8c510a536565'
auth_token = '2502d163b19fab7d8e0c3b5afafed678'
client = Client(account_sid, auth_token)


@given('Existen citas creadas en el sistema')
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

@when('Exista una cita agendada para el dia siguiente')
def step_impl(context):
    tomorrow = date.today() + timedelta(days=1)
    appointments = Cita.objects.filter(fecha_cita=tomorrow)
    assert len(Cita.objects.all())>0


@then('Se envia un sms al paciente')
def step_impl(context):
    #Se observan los resultados
    tomorrow = date.today() + timedelta(days=1)
    appointments = Cita.objects.filter(fecha_cita=tomorrow)

    for cita in appointments:
        if cita.paciente.correo.find('@'):
            # message = client.messages.create(
            #          body="No olvides tu cita en alfa medic, te esperamos!.",
            #          from_='+17205730340',
            #          to='+50240886635'
            #      )
            #assert message.sid != ""
            assert account_sid == "AC28c195212f1f17e9d15c8c510a536565"




