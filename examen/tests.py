from django.test import TestCase
from cita.models import Cita
from .models import Examen
from users.models import Paciente
from datetime import datetime, timedelta, date
from django.urls import reverse, resolve
from .views import ExaminationCreate,ExaminationListView

class Examination_Create(TestCase):
    def setUp(self):
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")
        paciente=Paciente.objects.create(
            nombre = 'Henry',
            apellido = 'León',
            telefono = '12345678',
            telefono_emergencia = '12345679',
            correo = 'henrisco@gmail.com',
            fecha_nacimiento = '1995-12-12',
            direccion = 'zona 6',
            descripccion = 'Joven guapo :3',
            sexo = 'MASCULINO',
            )
        cita = Cita(fecha = fecha, fecha_cita = fecha, hora_cita=hora, estado='Pendiente', comentario='Test', paciente=paciente).save()

        Examen(descripcion='Fractura en el pie', cita=cita, fecha=fecha).save()
        self.response = self.client.get('/crear_examen/1')

    def test_examamination_model(self):
        examen = Examen.objects.all()[0]
        self.assertEquals(str(examen), "Fractura en el pie")

    def test_examination_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_examination_create_url_resolves_create_recetasview(self):
        view = resolve('/crear_examen/1')
        self.assertEqual(
            view.func.__name__,
            ExaminationCreate.as_view().__name__
        )

    def test_examination_url_create(self):
        response = self.client.get(reverse('crear_examen', kwargs={'pk': '1'}))
        self.assertEqual(response.status_code,200)

    def test_exams_list(self):
        view = resolve('/listado_examenes/')
        self.assertEqual(
            view.func.__name__,
            ExaminationListView.__name__
        )

    def test_list_exams_status(self):
        response = self.client.get(reverse('ExaminationListView'))
        self.assertEqual(response.status_code,200)

class ModificarExamen(TestCase):
    def test_modificar_examen(self):
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

        Examen(descripcion='Examen de Sangre', cita_id=cita, fecha='2020-09-23').save()

        getExamen = Examen.objects.all()[0]

        getExamen.descripcion = "Examen de la vista" #modificando examen
        getExamen.save()

        self.assertEqual(getExamen.descripcion,'Examen de la vista')

class EliminarExamen(TestCase):
    def test_eliminar_examen(self):
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
        #Creando examen
        exam = Examen(descripcion='Examen de Sangre', cita_id=cita, fecha='2020-09-23').save()
        #self.assertEqual(Examen.objects.all(),1) #Verificando que si exista un examen
        #Eliminando examen
        Examen.objects.all().delete()
        #self.assertEqual(Examen.objects.all(),0) #Verificando que se haya eliminado el examen