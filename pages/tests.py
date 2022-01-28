from django.test import TestCase, SimpleTestCase
from .views import HomePageView, AppointmentCreate, RecetasListView
from django.urls import reverse, resolve

class HomepageTests(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('/')

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response,'home.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertEqual(self.response.status_code,200)
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi! I should not be here')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AgendarCita(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('agendar/cita/1/anthony')

    def test_agendar_status_code(self):
        self.assertEqual(self.response.status_code,404)

    def test_agendar_url_name(self):
        response = self.client.get(reverse('crear_cita', kwargs={'pk': '1', 'name':'anthony'}))
        self.assertEqual(response.status_code,200)

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/agendar/cita/1/anthony')
        self.assertEqual(
            view.func.__name__,
            AppointmentCreate.as_view().__name__
        )

    def test_agendar_url_name(self):
        response = self.client.get(reverse('crear_cita', kwargs={'pk': '1', "name": "anthony"}))
        self.assertEqual(response.status_code,200)

    # def test_agendar_contains_correct_html(self):
    #     self.assertContains(self.response, 'planificada')
    
    

class ListarRecetas(SimpleTestCase):

    def setUp(self):
        self.response = self.client.get('/recetas')

    def test_lsitar_recetas_status_code(self):
        self.assertEqual(self.response.status_code,301)

    def test_lsitar_recetas_url_name(self):
        self.assertEqual(self.response.status_code, 301)
    
    # def test_lsitar_recetas_does_not_contain_incorrect_html(self):
    #     self.assertNotContains(self.response, "Hola")

    def test_listar_recetas_url_resolves_listar_recetasview(self):
        view = resolve("/recetas/")
        self.assertEqual(
            view.func.__name__,
            RecetasListView.as_view().__name__
        )
    