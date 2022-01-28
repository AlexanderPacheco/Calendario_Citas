from django.shortcuts import render,redirect
from .models import Paciente
from cita.models import Cita,Receta
from anotacion.models import Anotacion
from examen.models import Examen
from .forms import pacienteForm
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf 
import datetime

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def listado_pacientes(request):
#     pacientes=Paciente.objects.all()
#     contexto = {'paciente':pacientes}
#     return render(request, 'users/listado_pacientes.html',contexto)

def listado_pacientes(request):
    if request.user.is_authenticated:    
        pacientes=Paciente.objects.all()
        data={
            'lista_pacientes':pacientes
        }
        return render(request, 'users/listado_pacientes.html',data)
    else:
        return redirect('notFound')

def modificar_paciente(request,correo): #con este parametro correo haces la busqueda en la bd y obtenes
    if request.user.is_authenticated:
        paciente = Paciente.objects.get(correo=correo) # el paciente que va a modificar
        if request.method == 'GET':
            form = pacienteForm(instance=paciente)
        else:
            form = pacienteForm(request.POST,instance=paciente)
            if form.is_valid():
                form.save()
            return redirect('listado_pacientes')
        return render(request,'paciente/ingresar_paciente.html', {'form': form})
        #return render(request,'home.html')  #aca cambiale el home.html por la pagina de modificar
    else:
        return redirect('notFound')

def ingresar_paciente(request):
    if request.user.is_authenticated:
        if request.user.is_authenticated:

            form = pacienteForm(request.POST)
            #if request.method == 'POST':
            if form.is_valid():
                form.save()
                #return redirect('pages:listado_pacientes')
                pacientes=Paciente.objects.all()
                data={
                    'lista_pacientes':pacientes
                }
                return render(request, 'users/listado_pacientes.html',data)

            else:
                form = pacienteForm()
            return render(request, 'paciente/ingresar_paciente.html', {'form': form})

        else:
            return redirect('listado_pacientes')        
    else:
        return redirect('notFound') 
        #form = pacienteForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form = pacienteForm()
    # context = {
    #     'form': form
    # }
    # return render(request, "paciente/ingresar_paciente.html", context)


def notFound(request):
    return render(request, 'notFound.html')


def detalle_paciente(request, correo):
    if request.user.is_authenticated:
        paciente = Paciente.objects.get(correo=correo)
        if request.method == 'GET':
            form = pacienteForm(instance=paciente)
        return render(request,'paciente/detalle_paciente.html',{'form':form})
    else:
        return redirect('notFound') 
        
class reporte_historial_clinico(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:    
            template =  get_template('paciente/reporte_pacientes.html')
            data = {
                'Pacientes':Paciente.objects.all(),
                'Citas':Cita.objects.all(),
                'Anotaciones':Anotacion.objects.all(),
                'Recetas':Receta.objects.all(),
                'Examenes':Examen.objects.all(),
            }
            pdf = render_to_pdf('paciente/reporte_pacientes.html', data)
            return HttpResponse(pdf, content_type='application/pdf')
        else:
            return redirect('notFound') 

def reporte_historial_clinicoPaciente(request,id):
    if request.user.is_authenticated:
        template =  get_template('paciente/reporte_paciente.html')
        paciente = Paciente.objects.get(pk=id)
        citas = Cita.objects.filter(paciente=paciente)
        data = {
            'Pacientes':paciente,
            'Citas':citas,
            'Anotaciones':Anotacion.objects.all(),
            'Recetas':Receta.objects.all(),
            'Examenes':Examen.objects.all(),
        }
        pdf = render_to_pdf('paciente/reporte_paciente.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return redirect('notFound')

def g_get_labels(val):
    if val == 0:
        return ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    elif val == 1:
        return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    else:
        return ["ERROR"]

def g_get_data(val):
    citas = Cita.objects.all()
    cantidad_citas = len(citas)
    if val == 0:
        dias = [0,0,0,0,0,0,0]
        dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
        'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}

        for i in range(cantidad_citas):
            anho = citas[i].fecha_cita.year
            mes =  citas[i].fecha_cita.month
            dia= citas[i].fecha_cita.day
            fecha = datetime.date(anho, mes, dia)

            #dias[i] = dicdias[fecha.strftime('%A').upper()]
            if dicdias[fecha.strftime('%A').upper()] == "Lunes":
                dias[0] = dias[0] + 1
            elif dicdias[fecha.strftime('%A').upper()] == "Martes":
                dias[1] = dias[1] + 1
            elif dicdias[fecha.strftime('%A').upper()] == "Miercoles":
                dias[2] = dias[2] + 1
            elif dicdias[fecha.strftime('%A').upper()] == "Jueves":
                dias[3] = dias[3] + 1
            elif dicdias[fecha.strftime('%A').upper()] == "Viernes":
                dias[4] = dias[4] + 1
            elif dicdias[fecha.strftime('%A').upper()] == "Sabado":
                dias[5] = dias[5] + 1
            else:
                dias[6] = dias[6] + 1

        print(dias)
        return [dias]
    elif val == 1:
        meses = [0,0,0,0,0,0,0,0,0,0,0,0]

        for i in range(cantidad_citas):
            anho = citas[i].fecha_cita.year
            mes =  citas[i].fecha_cita.month
            dia= citas[i].fecha_cita.day
            fecha = datetime.date(anho, mes, dia)

            if mes == 1:
                meses[0] = meses[0] + 1
            elif mes == 2:
                meses[1] = meses[1] + 1
            elif mes == 3:
                meses[2] = meses[2] + 1
            elif mes == 4:
                meses[3] = meses[3] + 1
            elif mes == 5:
                meses[4] = meses[4] + 1
            elif mes == 6:
                meses[5] = meses[5] + 1
            elif mes == 7:
                meses[6] = meses[6] + 1
            elif mes == 8:
                meses[7] = meses[7] + 1
            elif mes == 9:
                meses[8] = meses[8] + 1
            elif mes == 10:
                meses[9] = meses[9] + 1
            elif mes == 11:
                meses[10] = meses[10] + 1
            elif mes == 12:
                meses[11] = meses[11] + 1

        print(meses)
        return [meses]
    return 0


class LineChartJSONView(LoginRequiredMixin,BaseLineChartView):
    login_url = '/notFound'
    def get_labels(self):
        return g_get_labels(0)
        #return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        return ["Total de citas"]

    def get_data(self):
        return g_get_data(0)

class LineChartMonthJSONView(LoginRequiredMixin,BaseLineChartView):
    login_url = '/notFound'
    def get_labels(self):
        return g_get_labels(1)
        #return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        return ["Total de citas"]

    def get_data(self):
        return g_get_data(1)


line_chart = TemplateView.as_view(template_name='users/graphic.html')
line_chart_json = LineChartJSONView.as_view()
line_chart_month = TemplateView.as_view(template_name='users/graphic2.html')
line_chart_month_json = LineChartMonthJSONView.as_view()