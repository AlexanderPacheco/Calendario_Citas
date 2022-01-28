from django.test import TestCase,SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from users.models import Paciente
from datetime import datetime
from .views import *

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will',
            email='will@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupTests(TestCase): # new

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()
                         [0].username, self.username)
        self.assertEqual(get_user_model().objects.all()
                         [0].email, self.email)


class CreatePatient(TestCase):
    def test_create_patient2(self):
        test_Paciente = Paciente.objects.create(nombre='Francisco', apellido='Hernández', telefono=12345678, telefono_emergencia=12345678,
        correo='henriscoh1995@gmail.com', fecha_nacimiento='1995-12-12', direccion='zona 6', sexo='masculino')

        self.assertEqual(test_Paciente.nombre, 'Francisco')
        self.assertEqual(test_Paciente.apellido, 'Hernández')
        self.assertEqual(test_Paciente.telefono, 12345678)
        self.assertEqual(test_Paciente.telefono_emergencia, 12345678)
        self.assertEqual(test_Paciente.correo, 'henriscoh1995@gmail.com')
        self.assertEqual(test_Paciente.fecha_nacimiento, '1995-12-12')
        self.assertEqual(test_Paciente.direccion, 'zona 6')
        self.assertEqual(test_Paciente.sexo, 'masculino')
                
    
    def test_create_patient(self):
        test_Paciente = Paciente.objects.create(nombre='Henry', apellido='Leon', telefono=12345678, telefono_emergencia=12345678,
        correo='henriscoh1995@gmail.com', fecha_nacimiento='1995-12-12', direccion='zona 6', descripccion='sin enfermedades', sexo='masculino')

        self.assertEqual(test_Paciente.nombre, 'Henry')
        self.assertEqual(test_Paciente.apellido, 'Leon')

class EditPatient(TestCase):
    def test_edit_patient(self):
        test_Paciente = Paciente.objects.create(nombre='Francisco', apellido='Hernández', telefono=12345678, telefono_emergencia=12345678,
        correo='henriscoh1995@gmail.com', fecha_nacimiento='1995-12-12', direccion='zona 6', sexo='masculino')

        paciente = Paciente.objects.get(correo=test_Paciente.correo)

        paciente.nombre = "Franciscox"
        paciente.apellido = "Hernandezx"

        paciente.save()

        self.assertEqual(paciente.nombre, 'Franciscox')
        self.assertEqual(paciente.apellido, 'Hernandezx')
        self.assertEqual(paciente.telefono, '12345678')
        self.assertEqual(paciente.telefono_emergencia, '12345678')
        self.assertEqual(paciente.correo, 'henriscoh1995@gmail.com')
        self.assertEqual(paciente.direccion, 'zona 6')
        self.assertEqual(paciente.sexo, 'masculino')

class PatientHistory(TestCase):
    def test_Historial_clinico(self):
        view = resolve('/historial_clinico/')
        self.assertEqual(
            view.func.__name__,
            reporte_historial_clinico.__name__
        )

    def test_Historial_clinico_satus(self):
        response = self.client.get(reverse('reporte_historial_clinico'))
        self.assertEqual(response.status_code,302)

class PatientHistoryPaciente(TestCase):
    

    def test_Historial_clinicoPaciente_satus(self):
        test_Paciente = Paciente.objects.create(nombre='Francisco', apellido='Hernández', telefono=12345678, telefono_emergencia=12345678,
        correo='henriscoh1995@gmail.com', fecha_nacimiento='1995-12-12', direccion='zona 6', sexo='masculino') 
        paciente = Paciente.objects.get(pk=test_Paciente.pk)
        response = self.client.get('/historial_clinicoPaciente/{0}'.format(paciente.pk))
        #response = self.client.get('/modificar_pasajero/{0}'.format(pasajero.pk))
        self.assertEqual(response.status_code,302)


class GraphicReport(TestCase):
    def test_general_graphic_report(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.assertEquals(g_get_labels(0), dias)
        
    def test_general_logic_graphic_report(self):
        dias = [0,0,0,0,0,0,0]
        self.assertEquals(g_get_data(0), [dias])
        self.assertEquals(g_get_data(9), 0)

    def test_general_graphic_report2(self):
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        self.assertEquals(g_get_labels(1), meses)
        
    def test_general_logic_graphic_report2(self):
        meses = [0,0,0,0,0,0,0,0,0,0,0,0]
        self.assertEquals(g_get_data(1), [meses])
        self.assertEquals(g_get_data(9), 0)

