from django.shortcuts import render,redirect
from users.models import Paciente
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from anotacion.forms import AnotacionForm
from cita.models import Cita, Receta
from cita.forms import RecetaForm
from users.models import Paciente
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    template_name = 'home.html'

class AppointmentsListView(LoginRequiredMixin,ListView):
    model = Cita
    context_object_name = 'cita_list'
    template_name = 'citas/lista_citas.html'
    login_url = '/notFound'

    def get_queryset(self):
        filter_val = self.request.GET.get('q', 'give-default-value')
        print(filter_val)
        try:
            new_context = Cita.objects.filter(
                fecha_cita=filter_val,
            )
            return new_context
        except:
            new_context = Cita.objects.all()
            return new_context


class RecetasListView(LoginRequiredMixin,ListView):
    login_url = '/notFound'
    model = Receta
    context_object_name="recetas"
    template_name='recetas/lista_de_recetas.html'


class RecetasDetailView(LoginRequiredMixin,DetailView):
    login_url = '/notFound'
    model = Receta
    context_object_name="receta"
    template_name='recetas/detalle_receta.html'

class AppointmentDetailView(LoginRequiredMixin,DetailView):
    login_url = '/notFound'
    model = Cita
    context_object_name = 'cita'
    template_name = 'citas/cita_detail.html'
    
    def get_form(self):
        form = self.form_class(instance=AnotacionForm),
        form2 = self.form_class(isinstance=RecetaForm)
        return {form, form2}
    
    def get_context_data(self, **kwargs):
        context = super(AppointmentDetailView, self).get_context_data(**kwargs)
        context.update({
            'anotacion_form': AnotacionForm, # get the form instance
            'receta_form': RecetaForm
        })

        return context
    
class AppointmentUpdateView(LoginRequiredMixin,DetailView):
    login_url = '/notFound'
    model = Cita
    context_object_name = 'cita'
    template_name = 'citas/actualizar_cita.html'

class AppointmentCreate(TemplateView):
    template_name = 'citas/crear_cita.html'

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['id'] = kwargs['pk']
        context['name'] = kwargs['name']
        return context

class SearchResultsListView(LoginRequiredMixin,ListView):
    ''' Resultados de busqueda '''
    login_url = '/notFound'
    model = Paciente
    context_object_name = 'pacients'
    template_name = "search_result.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Paciente.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) |
            Q(correo__icontains=query) |
            Q(telefono__icontains=query) |
            Q(telefono_emergencia__icontains=query) |
            Q(correo__icontains=query) 
        )

    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)

        query = self.request.GET.get('q')
        context['citas'] =  Cita.objects.filter(
            Q(paciente__nombre__icontains=query) |
            Q(paciente__telefono__icontains=query) |
            Q(paciente__telefono_emergencia__icontains=query) |
            Q(comentario__icontains=query) |
            Q(paciente__correo__icontains=query) 
        )
        context['recetas'] =  Receta.objects.filter(
            Q(cita__paciente__nombre__icontains=query) |
            Q(detalle_receta__icontains=query)
        )

        return context

# def modificar_cita(request, pk):
#     query = request.POST
#     if Cita.objects.filter(id=pk).exists():
#         try:
#             cita = Cita.objects.get(id=pk)
#             cita.fecha_cita=query['fecha_cita']
#             cita.hora_cita=query['hora_cita']
#             cita.comentario=query['comentario']

#             cita.save()
#         except:
#             messages.add_message(request, messages.ERROR,'Error, No se pudo actualizar cita')
    
#         else:
#             messages.add_message(request, messages.INFO,'Se realizaron los cambios con exito!')
    
#     return redirect('citas/actualizar_cita.html',pk=pk)
            
    