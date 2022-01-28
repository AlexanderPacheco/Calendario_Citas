from django.shortcuts import render
from .models import Cita, Receta
from .forms import recetaOffForm
from django.contrib import messages
from django.shortcuts import redirect
from users.models import Paciente
from .forms import RecetaForm
from datetime import datetime 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf 
from django.db.models import Sum, Count
from django.contrib.auth.mixins import LoginRequiredMixin

def appointment_update(request, pk):
    if request.user.is_authenticated:
        query = request.POST
        if Cita.objects.filter(id=pk).exists():
            try:
                cita = Cita.objects.get(id=pk)
                cita.fecha_cita=query['fecha_cita']
                cita.hora_cita=query['hora_cita']
                cita.comentario=query['comentario']
                cita.save()
            except:
                messages.add_message(request, messages.ERROR, 
                'ERROR: Ha ocurrido un error al actualizar la cita, intenta de nuevo.')
            else:
                messages.add_message(request, messages.INFO, 
                '¡Hemos guardado tus cambios!')
                
        return redirect('citas')
    else:
        return redirect('notFound')


def appointment_create(request, pk):
    if request.user.is_authenticated:
        query = request.POST
        try:
            cita = Cita(
                fecha_cita=query['fecha_cita'],
                hora_cita=query['hora_cita'],
                comentario=query['comentario'],
                paciente=Paciente.objects.get(id=pk),
            )
            cita.save()
            send_mail(
                'Receta',
                "{0}, para el dia {1} a la hora {2}".format(
                    cita.comentario,
                    cita.fecha_cita,
                    cita.hora_cita
                ),
                'medsistemnotify@gmail.com',
                [cita.paciente.correo],
                fail_silently=False,
            )
        except:
            messages.add_message(request, messages.ERROR, 
            'ERROR: Ha ocurrido un error al crear la cita, intenta de nuevo.')
        else:
            messages.add_message(request, messages.INFO, 
            '¡Hemos guardado tus cambios!')
            
                
        return redirect('crear_cita', pk=pk, name=Paciente.objects.get(id=pk).nombre)
    else:
        return redirect('notFound') 

def appointment_delete(request, pk):
    if request.user.is_authenticated:    
        query = request.POST
        if Cita.objects.filter(id=pk).exists():
            try:
                cita = Cita.objects.get(id=pk)
                cita.delete()
            except:
                messages.add_message(request, messages.ERROR, 
                'ERROR: Ha ocurrido un error al eliminar la cita, intenta de nuevo.')
            else:
                messages.add_message(request, messages.INFO, 
                '¡Se ha eliminado la cita!')
                
        return redirect('citas')
    else:
        return redirect('notFound')

def appointment_serve(request, pk):
    if request.user.is_authenticated:    
        query = request.POST
        if Cita.objects.filter(id=pk).exists():
            try:
                cita = Cita.objects.get(id=pk)
                cita.estado="ATENDIDA"
                cita.save()
            except:
                messages.add_message(request, messages.ERROR, 
                'ERROR: Ha ocurrido un error al atender la cita, intenta de nuevo.')
            else:
                messages.add_message(request, messages.INFO, 
                '¡Se ha atendido la cita!')
                
        return redirect('citas')
    else:
        return redirect('notFound') 


def RecetaCreate(request, id):
    if request.user.is_authenticated:    
        form = RecetaForm(request.POST)
        
        if form.is_valid():
            receta = form.save(commit=False)
            #fecha = datetime.now()
            cita = Cita.objects.get(id=id)
            receta.cita = cita
            receta.save()
            
            send_mail(
                'Receta',
                receta.detalle_receta,
                'medsistemnotify@gmail.com',
                [receta.cita.paciente.correo],
                fail_silently=False,
            )
        return HttpResponseRedirect('/citas/'+id)
    else:
        return redirect('notFound')


def ingresar_receta_off(request,id):
    if request.user.is_authenticated:
        form = recetaOffForm(request.POST)

        if form.is_valid():
            receta = form.save(commit=False)
            
            paciente = Paciente.objects.get(pk=id)
            receta.paciente = paciente
            receta.save()
            #form.save()
            return redirect('listado_pacientes')
        else:
            form = recetaOffForm()
        return render(request, 'citas/crear_receta_off.html', {'form': form})
    else:
        return redirect('notFound')


def eliminar_receta(request,id):
    if request.user.is_authenticated:
        receta = Receta.objects.get(pk=id)
        receta.delete()
        return redirect('recetas')
    else:
        return redirect('notFound') 
'''
def get_recetas_paciente(request,id):
	paciente = Paciente.objects.get(pk = id)
    recetas = Receta.objects.get(paciente = paciente)

    if request.method == 'GET':
        form = receta2Form(instance=recetas)
    else:
        form = pasajeroForm(request.POST,instance=pasajero)
        if form.is_valid():
            form.save()
        return redirect('recetas')
    return redirect('listado_pacientes')'''

def modificar_receta(request,id):
    if request.user.is_authenticated:
        recet = Receta.objects.get(pk=id)
        if request.method == 'GET':
            form = RecetaForm(instance=recet)
        else:
            form = RecetaForm(request.POST,instance=recet)
            if form.is_valid():
                form.save()
            return redirect('recetas')
        return render(request,'citas/crear_receta_off.html', {'form': form})
    else:
        return redirect('notFound')

class reporte_concurrencia_clinica(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:    
            template =  get_template('citas/concurrencia.html')
            print(Cita.objects.all().annotate(total=Count('estado')).order_by('-total').count())
            print(Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('-total').count())
            div=Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('-total').count()
            prom=0
            if div!=0:
                prom=Cita.objects.all().annotate(total=Count('estado')).order_by('-total').count()/ div
            data = {
                'Citas':Cita.objects.all(),
                'Total':Cita.objects.count(),
                'Fecha_concurrido':Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('-total')[:1],
                'Citas_atendidas': Cita.objects.filter(estado='ATENDIDA').annotate(total=Count('estado')).order_by('-total').count(),
                'Citas_pendientes': Cita.objects.filter(estado='PENDIENTE').annotate(total=Count('estado')).order_by('-total').count() ,
                'Citas_canceladas' : Cita.objects.filter(estado='CANCELADA').annotate(total=Count('estado')).order_by('-total').count(),
                'Promedio_citas' :prom,
                'Menos_concurrido':Cita.objects.all().values('fecha_cita').annotate(total=Count('fecha_cita')).order_by('total')[:1],
            }
            pdf = render_to_pdf('citas/concurrencia.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            return redirect('notFound')     