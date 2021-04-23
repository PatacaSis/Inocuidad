from django.urls import path, include
from .views import empresas,Auditoria,DatosEmpresa,menuEmpresa

urlpatterns = [
    path('', empresas, name='empresas'),
    path('menu/<int:pk>/', menuEmpresa, name='menu'),
    path('datos/<int:pk>/', DatosEmpresa.as_view(), name = 'datos'),
    path('auditoria/', Auditoria.as_view(), name='auditoria'),
] 