from django.test import TestCase, SimpleTestCase
from .models import Cita, Receta
from datetime import datetime, timedelta, date
from users.models import Paciente
from cita.models import Cita
from django.urls import reverse, resolve
from .views import Cita,reporte_concurrencia_clinica
from .forms import recetaOffForm
from datetime import datetime, timedelta, date
from django.core import mail
from random import seed
from random import randint
# seed random number generator


# Test sms notification

class SmsTest(TestCase):
    ''' Prueba el formato correcto para el envio de el mensaje de
    texto, las pruebas pasan luego de aplicar la conexion a twilio'''
    def setUp(self):
        self.citas = Cita.objects.all()

    def hay_citas_en_el_sistema(self):
        self.assertTrue(len(self.citas)>0)
    
    def pacientes_tienen_numero_telefonico(self):
        seed(1)
        self.assertRegex(self.citas(range(len(self.citas))), r'[0-9]+')

    def numero_tiene_formato_correcto_guatemala(self):
        self.assertEqual(len(self.citas(range(len(self.citas)))), 8)
        


class EmailTest(TestCase):
    
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')



'''
class test_url_receta_off(SimpleTestCase):

    def test_ingresar_pasajero(self):
        response = self.client.get('/ingresar_receta_off/')
        self.assertNotEqual(response.status_code, 404)'''

class test_isValidForm(TestCase):
    data={
            'fecha':'1996-02-17',
            'detalle_receta':'esto es una receta',
        }
    def test_valid_form(self):
        form = recetaOffForm(self.data)
        self.assertTrue(form.is_valid())

class test_eliminarReceta(TestCase):
    
    def test_eliminar(self):
        test_receta = Receta.objects.create(
            detalle_receta = "Descripcion de Receta"
            )

        receta = Receta.objects.get(pk=test_receta.pk)
        response = self.client.get('/eliminar_receta/{0}'.format(receta.pk))
        self.assertRedirects(response, '/notFound')

class EliminarRecetaTestCase(TestCase):
    def test_create_receta(self):
        now = datetime.now()
        #test_cista = Cita.objects.create(fecha=now, fecha_cita = now, estado = 'PENDIENTE',comentario ='Hello world')
        test_receta = Receta.objects.create(fecha=now, detalle_receta='Receta 222')
        #self.assertEqual(test_receta.detalle_receta,'Receta 222')   
        receta = Receta.objects.get(pk=test_receta.pk)
        self.assertEqual(receta.detalle_receta,'Receta 222')
        
        #pass
        #self.assertEqual(user.username, 'will')
        #self.assertEqual(user.email, 'will@email.com')
        #self.assertTrue(user.is_active)
        #self.assertFalse(user.is_staff)
        #self.assertFalse(user.is_superuser)
# # Create your tests here.
# '''
# class ModelCitaTest(TestCase):

#     def test_create_city(self):
#         fecha = datetime.now()
#         hora = datetime.time()
#         Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=1001).save()

#         citas = Cita.objects.all()
#         self.assertEqual(citas[0].fecha, fecha)
#         self.assertEqual(citas[0].fecha_cita, fecha)
#         self.assertEqual(citas[0].hora_cita, hora)
#         self.assertEqual(citas[0].comentario, 'prueba')
#         self.assertEqual(citas[0].paciente, 1001)
#         self.assertEqual(citas[0].estado, 'Pendiente')
# '''

class ModelCitaTest(TestCase):

    def test_cancel_cita(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
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
        Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()

        citas = Cita.objects.all()
        self.assertEqual(citas[0].comentario, 'prueba')
        self.assertEqual(citas[0].paciente, paciente)
        self.assertEqual(citas[0].estado, 'Pendiente')
        self.assertNotEqual(citas[0].delete()[0],0 )#Es 0 si no elimino nada
'''
class ModificarCita(TestCase):
    def test_modificar_cita(self):
        paciente = Paciente.objects.get(nombre='Lucia')
        test_cita = Cita.objects.create(fecha_cita='2020-09-25',hora_cita='06:30:00',estado='PENDIENTE',comentario='Editado1',paciente_id=paciente.id,fecha='2020-09-19 19:04:14.960231')

        getcita = Cita.objects.get(id=8)

        getcita.comentario = "Editado2"
        getcita.save()

        self.assertEqual(getcita.comentario,'Editado2')

        self.assertEqual(getcita.fecha_cita, '2020-09-25')
        self.assertEqual(getcita.hora_cita, '06:30:00')
        self.assertEqual(getcita.estado, 'PENDIENTE')
        self.assertEqual(getcita.comentario, 'Editado2')
        self.assertEqual(getcita.paciente_id, paciente.id)
        self.assertEqual(getcita.fecha, '2020-09-19 19:04:14.960231')
'''
        
class RecetaCreate(TestCase):
    
    def setUp(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
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
        cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()

        Receta(detalle_receta='Tiene dolor de garganta', cita=cita, fecha=fecha).save()
        #receta = Receta.objects.create(detalle_receta='Tiene dolor de garganta',)
        self.response = self.client.get('/crear_receta/6')

    def test_agendar_status_code(self):
        self.assertEqual(self.response.status_code,302)

    def test_crear_recete_url(self):
        response = self.client.get(reverse('crear_receta', kwargs={'id': '6'}))
        self.assertEqual(response.status_code,302)

    def test_crear_recetas_url_resolves_create_recetasview(self):
        view = resolve('/crear_receta/6')
        self.assertEqual(
            view.func.__name__,
            RecetaCreate.__name__
        )
    
    def test_crear_receta(self):
        receta = Receta.objects.all()[0]
        self.assertEqual(receta.detalle_receta, 'Tiene dolor de garganta')

class ModificarReceta(TestCase):
    def test_modificar_receta(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        paciente=Paciente.objects.create(
            nombre = 'Jhon',
            apellido = 'Nieve',
            telefono = '48484848',
            telefono_emergencia = '48484849',
            correo = 'jhon@gmail.com',
            fecha_nacimiento = '2020-12-12',
            direccion = 'El norte castillo negro',
            descripccion = 'Guardian',
            sexo = 'MASCULINO',
        )
        cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='prueba', paciente=paciente).save()

        Receta(detalle_receta='Tiene fiebre', cita=cita, fecha='2020-09-23').save()

        getreceta = Receta.objects.get(cita=cita)

        getreceta.detalle_receta = "Edicion" #Modificando receta
        getreceta.save()

        self.assertEqual(getreceta.detalle_receta,'Edicion')
        self.assertEqual(getreceta.cita, cita)


class CitasHistory(TestCase):
    def test_Dias_Concurridos_View(self):
        view = resolve('/concurrencia_citas/')
        self.assertEqual(
            view.func.__name__,
            reporte_concurrencia_clinica.__name__
        )

    def test_Dias_Concurridos_satus(self):
        response = self.client.get(reverse('reporte_concurrencia_clinica'))
        self.assertEqual(response.status_code,302)


