from django.contrib import admin
from .models import Empresa,Producto

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero','localidad')

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre', 'codigo')


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Producto,ProductosAdmin)
