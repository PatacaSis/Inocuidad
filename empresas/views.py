from django.shortcuts import render
from .models import Empresa

def empresas(request):
    empresas = Empresa.objects.all()
    
    return render(request, 'empresas/empresas.html', {'empresas':empresas})

