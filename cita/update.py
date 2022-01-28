from cita.models import Cita
from datetime import date, timedelta
from django.core.mail import send_mail
from twilio.rest import Client

account_sid = 'AC28c195212f1f17e9d15c8c510a536565'
auth_token = 'ba4135215f92ff3c5a1c6a1eb59168a5'
client = Client(account_sid, auth_token)

def update_somthing():
    tomorrow = date.today() + timedelta(days=1)
    appointments = Cita.objects.filter(fecha_cita=tomorrow)

    for cita in appointments:
        if cita.paciente.correo.find('@'):
            body = """¡Hola! 
                Te recordamos que la cita en CLINICA es mañana {0} a las {1} horas 
                has indicado que el motivo de la cita es ***{2}***. 
                Recuerda ser puntual en tu cita para no tener
                    inconvenientes con las citas siguientes a la tuya. 
                ¡Esperamos verte pronto!""".format( 
                    cita.fecha_cita,
                    cita.hora_cita,
                    cita.comentario
                )
            
            send_mail("Cita agendada",body,
            'medsistemnotify@gmail.com',[cita.paciente.correo],fail_silently=True)
        else:
            print("No es un email valido")
    print("Tarea hola")


def sms_remminder():
    today = date.today()
    appointments = Cita.objects.filter(fecha_cita=today)

    for cita in appointments:
        if cita.paciente.correo.find('@'):
            message = client.messages.create(
                     body="No olvides tu cita en alfa medic, te esperamos!.",
                     from_='+15017122661',
                     to='+50240886635'
                 )
            print(message.sid)
    
