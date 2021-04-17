from django.urls import path
from .views import indexDocumentos,alimentos,normativasAgua,normativasPlagas,caa,codex

urlpatterns = [
    path('', indexDocumentos, name='documentos'),
    path('documentos/caa/', caa, name='caa'),
    path('documentos/codex/', codex, name='codex'),
    path('documentos/alimentos/', alimentos, name='alimentos'),
    path('documentos/normativasAgua/', normativasAgua, name='normativasAgua'),
    path('documentos/normativasPlagas/', normativasPlagas, name='normativasPlagas'),
]