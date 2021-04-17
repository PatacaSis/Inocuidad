from django.contrib import admin
from .models import Normativa,TematicaDocumental,Alimento,temasNormas,CodAliArg,Codex

class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('tipo','nombre','caa')

admin.site.register(Alimento,AlimentoAdmin)
admin.site.register(CodAliArg)
admin.site.register(Codex)
admin.site.register(Normativa)
admin.site.register(temasNormas)
admin.site.register(TematicaDocumental)
