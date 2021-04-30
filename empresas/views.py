from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import AuditoriaForm,AguaForm
from .models import Empresa,Auditoria,Agua



# ------------------Datos generales--------------------------

def empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas/empresas.html', {'empresas':empresas})

def menuEmpresa(request, id):
    return render(request, 'empresas/menu.html')

class NuevaEmpresa(CreateView):
    model = Empresa
    form_class = 'EmpresaForm'
    
class DatosEmpresa(DetailView):
    model = Empresa
    template_name = 'empresas/datosEmpresa.html'

# ------------------Auditoriaa--------------------------

class AuditoriaListado(ListView):
    model = Auditoria
    template_name = 'empresas/auditorias.html'
    queryset = Auditoria.objects.filter(estado=True)

class AuditoriaNueva(CreateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'empresas/agua.html'
    success_url = '/empresas/auditorias/'

class AuditoriaDetalle(DetailView):
    model = Auditoria
    template_name = 'empresas/auditoriaDetalle.html'

class AuditoriaModificar(UpdateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'empresas/auditoria_nueva.html'
    success_url = '/empresas/auditorias/'

class AuditoriaDelete(DeleteView):
    model = Auditoria

    def post(self,request, pk,*args,**kwargs):
        object = Auditoria.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('auditorias')


# ------------------Controles de Agua--------------------------

class ControlAguaListado(ListView):
    model = Agua
    template_name = 'empresas/agua_listado.html'
    queryset = Agua.objects.filter(estado=True)

class ControlAguaNueva(CreateView):
    model = Agua
    form_class = AguaForm
    template_name = 'empresas/agua_nuevo_control.html'
    success_url = '/empresas/agua/'

class ControlAguaDetalle(DetailView):
    model = Agua
    template_name = 'empresas/agua_detalle.html'

class ControlAguaModificar(UpdateView):
    model = Agua
    form_class = AguaForm
    template_name = 'empresas/agua_nuevo_control.html'
    success_url = '/empresas/agua/'

class ControlAguaDelete(DeleteView):
    model = Agua

    def post(self,request, pk,*args,**kwargs):
        object = Agua.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('agua')

