from django.urls import path, include
from .views import empresas

urlpatterns = [
    path('', empresas, name='empresas')
] 