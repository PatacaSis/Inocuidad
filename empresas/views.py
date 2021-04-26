from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import ListView,CreateView
from .forms import AuditoriaForm
from .models import Empresa,Auditoria

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


class AuditoriaListado(ListView):
    model = Auditoria
    template_name = 'empresas/auditorias.html'
    queryset = Auditoria.objects.all()

class AuditoriaNueva(CreateView):
    model = Auditoria
    form_class = AuditoriaForm
    template_name = 'empresas/auditoria_nueva.html'

class AuditoriaDetalle(DetailView):
    model = Auditoria
    template_name = 'empresas/auditoriaDetalle.html'




