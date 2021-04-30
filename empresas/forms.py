from django import forms
from .models import Empresa,Auditoria,Agua

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'

class AuditoriaForm(forms.ModelForm):
    class Meta:
        model = Auditoria
        exclude = ['estado']

class AguaForm(forms.ModelForm):
    class Meta:
        model = Agua
        exclude = ['estado']