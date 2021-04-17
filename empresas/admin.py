from django.contrib import admin
from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre','numero','localidad','productos')


admin.site.register(Empresa,EmpresaAdmin)
