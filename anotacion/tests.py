from django.test import TestCase
from anotacion.models import Anotacion
from cita.models import Cita
from datetime import datetime
from anotacion.models import Anotacion
from django.urls import reverse

# Create your tests here.

class ListaAnotacionesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create 13 anotaciones for tests
        number_of_anotaciones = 13
        for anotacion_num in range(number_of_anotaciones):
            Anotacion.objects.create(descripcion='Ejemplo anotacion %s' % anotacion_num)
            
    def test_view_url_exists_at_desired_location(self): 
        #Verifica que la url exista
        resp = self.client.get('/listado_anotaciones') 
        self.assertEqual(resp.status_code, 301) 
class AnnotationViewTest(TestCase):
    '''
    def setUp(self):
        #Create a meeting
        test_meeting = Cita.objects.create(fecha=datetime.now(), fecha_cita=datetime.now(), hora_cita=datetime.time(),
            estado='Pendiente', comentario='Hacre examen', paciente=1001)
        #test_meeting.save()

#         #Create a annotation
#         test_annotation = Anotacion.objects.create(id_cita=test_meeting.pk, descripcion='Tiene fiebre', fecha_hora=datetime.now())
#         #test_annotation.save()
#     '''
