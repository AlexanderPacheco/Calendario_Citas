from django.shortcuts import render
from cita.models import Cita
from .models import Examen
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ExaminationForm
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.template import Template, Context
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#def ExaminationCreate(request, pk):

#    return HttpResponseRedirect('/citas/'+pk)

class ExaminationCreate(DetailView):
    login_url = '/notFound'
    model = Cita
    context_object_name = 'cita'
    template_name = 'examen/examination_create_form.html'
    
    def get_form(self):
        form = self.form_class(instance=ExaminationForm)
        return form
    
    def get_context_data(self, **kwargs):
        context = super(ExaminationCreate, self).get_context_data(**kwargs)
        context.update({
            'examination_form': ExaminationForm
        })

        return context

def ExaminationActionCreate(request, pk):
    if request.user.is_authenticated:
        form = ExaminationForm(request.POST)
        print(pk)
        if form.is_valid():
            print("Si entro")
            examen = form.save(commit=False)
            #fecha = datetime.now()
            cita = Cita.objects.get(pk=pk)
            examen.cita = cita
            print(examen.descripcion)
            examen.save()

        return HttpResponseRedirect('/crear_examen/'+pk)
    else:
        return redirect('notFound')


def ExaminationListView(request):
    #if request.user.is_authenticated:
        Examenes=Examen.objects.all()
        data={
            'lista_examenes':Examenes
        }
        return render(request, 'examen/listado_examenes.html',data)
    #else:
        #return redirect('notFound') 



def ExaminationEdit(request, pk):
    if request.user.is_authenticated:
        examen = Examen.objects.get(pk=pk)

        data = {
            'form': ExaminationForm(instance=examen)
        }

        if request.method == 'POST':
            form = ExaminationForm(data=request.POST, instance=examen)
            if form.is_valid():
                form.save()
                data['mensaje'] = "Examen modificado correctamente"
                data['form'] = form
        return render(request, 'examen/modificar_examen.html',data)
    else:
        return redirect('notFound')    


def ExaminationDelete(request, pk):
    if request.user.is_authenticated:
        query = request.POST
        if Examen.objects.filter(id=pk).exists():
            try:
                exam = Examen.objects.get(id=pk)
                exam.delete()
            except:
                messages.add_message(request, messages.ERROR,'Error, no se pudo eliminar examen, vuelva a intentar')
            else:
                messages.add_message(request, messages.INFO,'¡Se ha eliminado el examen!')
                
        return redirect('/listado_examenes/')
    else:
        return redirect('notFound') 
'''
def ExaminationDelete(request,id):
    exam = Examen.objects.get(pk=id)
    exam.delete()
    return redirect(to="listado_examenes")
'''