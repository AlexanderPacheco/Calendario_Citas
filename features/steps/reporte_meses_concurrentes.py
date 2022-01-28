from users.models import Paciente
from cita.models import Cita
from datetime import datetime, timedelta, date
from users.views import g_get_data, g_get_labels

@given('Se han atendido citass')
def step_impl(context):
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
    
    

@when('Cuando se pulse el boton generar reporte de meses concurridos')
def step_impl(context):
    dias = [0,0,0,0,0,0,0,0,0,0,0,0]
    assert [dias] != g_get_data(1)
    #assert 1 == 1
      
    

@then('Se visualiza el reporte grafico')
def step_impl(context):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    assert g_get_labels(1) == meses
    #assert 1 == 1
    
    
    

