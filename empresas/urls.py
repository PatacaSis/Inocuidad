from django.urls import path, include
from .views import *

urlpatterns = [
    path('', empresas, name='empresas'),
    path('nueva/', NuevaEmpresa.as_view(), name='nuevaempresa'),
    path('menu/<int:pk>/', menuEmpresa, name='menu'),
    path('datos/<int:pk>/', DatosEmpresa.as_view(), name = 'datos'),
    
    path('auditorias/', AuditoriaListado.as_view(), name='auditorias'),
    path('auditoria/nueva/', AuditoriaNueva.as_view(), name='auditoria-nueva'),
    path('auditoria/<int:pk>/', AuditoriaDetalle.as_view(), name = 'auditoriadet'),
    path('auditoria/<int:pk>/modificar', AuditoriaModificar.as_view(), name = 'auditoria-modificar'),
    path('auditoria/<int:pk>/eliminar', AuditoriaDelete.as_view(), name = 'auditoria-eliminar'),

    path('agua/', ControlAguaListado.as_view(), name='agua'),
    path('agua/nuevo-control/', ControlAguaNueva.as_view(), name='nuevo-control'),
    path('agua/<int:pk>/', ControlAguaDetalle.as_view(), name = 'agua-detalle'),
    path('agua/<int:pk>/modificar', ControlAguaModificar.as_view(), name = 'agua-modificar'),
    path('agua/<int:pk>/eliminar', ControlAguaDelete.as_view(), name = 'agua-eliminar'),
] 