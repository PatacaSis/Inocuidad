from django.urls import path, include
from .views import empresas,Auditoria,DatosEmpresa

urlpatterns = [
    path('', empresas, name='empresas'),
    path('datos/<int:pk>/', DatosEmpresa.as_view(), name = 'datos'),
    path('auditoria/', Auditoria.as_view(), name='auditoria'),
] 