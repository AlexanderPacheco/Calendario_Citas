from users.models import Paciente
from cita.models import Cita
from datetime import datetime, timedelta, date
from users.views import g_get_data, g_get_labels

@given('Se han atendido citas')
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
    
    

@when('Cuando se pulse el boton generar reporte de dias concurridos')
def step_impl(context):
    dias = [0,0,0,0,0,0,0]
        #self.assertEquals(g_get_data(0), [dias])
    assert [dias] != g_get_data(0)
    #assert 1 == 1
      
    

@then('Se visualiza reporte grafico')
def step_impl(context):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    assert g_get_labels(0) == dias
    #assert 1 == 1
    
    
    

