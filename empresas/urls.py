from django.urls import path, include
from .views import empresas,AuditoriaListado,AuditoriaNueva,AuditoriaDetalle,DatosEmpresa,menuEmpresa,NuevaEmpresa

urlpatterns = [
    path('', empresas, name='empresas'),
    path('nueva/', NuevaEmpresa.as_view(), name='nuevaempresa'),
    path('menu/<int:pk>/', menuEmpresa, name='menu'),
    path('datos/<int:pk>/', DatosEmpresa.as_view(), name = 'datos'),
    path('auditorias/', AuditoriaListado.as_view(), name='auditorias'),
    path('auditoria-nueva/', AuditoriaNueva.as_view(), name='auditoria-nueva'),
    path('auditoria/<int:pk>/', AuditoriaDetalle.as_view(), name = 'auditoriadet'),
] 