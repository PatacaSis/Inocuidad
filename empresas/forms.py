from django import forms
from .models import Empresa,Auditoria

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        fields = '__all__'