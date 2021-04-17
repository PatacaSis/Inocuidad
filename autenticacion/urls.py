from django.urls import path
from .views import VistaRegistro, salir,acceder

urlpatterns = [
    path('register/', VistaRegistro.as_view(), name='register'),
    path('acceder/', acceder, name='acceder'),
    path('salir/', salir, name='salir'),
    # path('login/', LoginView.as_view(template_name='autenticacion/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='autenticacion/logout.html'), name='login')
]