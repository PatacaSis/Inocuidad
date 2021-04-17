from django.shortcuts import render
from .models import TematicaDocumental,Alimento,Normativa,CodAliArg,Codex

def indexDocumentos(request):
    tiposDoc = TematicaDocumental.objects.all()
    return render(request, 'documentacion/tipos.html', {'tiposDoc':tiposDoc})

def alimentos(request):
    alimentos = Alimento.objects.all()
    return render(request, 'documentacion/alimentos.html', {'alimentos':alimentos})

def normativasAgua(request):
    normativasAgua = Normativa.objects.filter(tema__tema__exact='Agua')
    return render(request, 'documentacion/normativasAgua.html',{'normativasAgua':normativasAgua})

def normativasExpo(request):
    normativasExpo = Normativa.objects.filter(tema__tema__exact='Exportacion')
    return render(request, 'documentacion/normativasExpo.html',{'normativasExpo':normativasExpo})

def normativasHACCP(request):
    normativasHACCP = Normativa.objects.filter(tema__tema__exact='HACCP')
    return render(request, 'documentacion/normativasHACCP.html',{'normativasHACCP':normativasHACCP})

def normativasInstalaciones(request):
    normativasInstalaciones = Normativa.objects.filter(tema__tema__exact='Instalaciones Industriales')
    return render(request, 'documentacion/normativasInstalaciones.html',{'normativasInstalaciones':normativasInstalaciones})

def normativasPlagas(request):
    normativasPlagas = Normativa.objects.filter(tema__tema__exact='Plagas')
    return render(request, 'documentacion/normativasPlagas.html',{'normativasPlagas':normativasPlagas})

def normativasRotulacion(request):
    normativasRotulacion = Normativa.objects.filter(tema__tema__exact='Rotulacion')
    return render(request, 'documentacion/normativasRotulacion.html',{'normativasRotulacion':normativasRotulacion})

def caa(request):
    capitulos = CodAliArg.objects.all()
    return render(request,'documentacion/caa.html', {'capitulos':capitulos})

def codex(request):
    identi = Codex.objects.all()
    return render(request,'documentacion/codex.html', {'identi':identi})
