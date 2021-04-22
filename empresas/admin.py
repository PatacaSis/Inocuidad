from django.contrib import admin
from .models import Empresa,Producto,GrupoTecnologico,Auditoria,Pais


class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ('empresa','fecha','motivo','estado')

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero',)

class GrupoTecnologicoAdmin(admin.ModelAdmin):
    list_display = ('numero','descripcion')

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre', 'codigo')

admin.site.register(Auditoria,AuditoriaAdmin)
admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(GrupoTecnologico,GrupoTecnologicoAdmin)
admin.site.register(Pais)
admin.site.register(Producto,ProductosAdmin)
