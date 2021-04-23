from django.shortcuts import render
from django.views.generic.detail import DetailView,View
from django.views.generic import ListView
from .models import Empresa,Auditoria

def empresas(request):
    empresas = Empresa.objects.all()
    
    return render(request, 'empresas/empresas.html', {'empresas':empresas})

class Auditoria(ListView):
    model = Auditoria
    template_name = 'empresas/auditorias.html'
    queryset = Auditoria.objects.all()


def menuEmpresa(request, id):
    return render(request, 'empresas/menu.html')

class DatosEmpresa(DetailView):
    model = Empresa
    template_name = 'empresas/datosEmpresa.html'

