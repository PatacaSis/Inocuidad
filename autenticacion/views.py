from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
# from .forms import UserRegisterForm


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             nombre_usuario = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             usuario = authenticate(username=nombre_usuario, password=password)
#             if usuario is not none:
#                 login(request, usuario)
#                 messages.success(request, F"Bienvenido a la plataforma {nombre_usuario}")
#                 return redirect("base/index")
#             else:
#                 message.error(request, "Los datos son incorrectos")
#         else:
#             message.error(request, "Los datos son incorrectos")



#     form = AuthenticationForm()

#     return render(request, 'autenticacion/login.html', {'form':form})

def index(request):
    return render(request, 'autenticacion/index.html', {})

def acceder(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                # messages.success(request, f"Bienvenido a la plataforma {nombre_usuario}")
                return redirect('index')
            else:
                message.error(request, "Los datos son incorrectos")
        else:
            message.error(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request, 'autenticacion/acceder.html', {'form':form })

class VistaRegistro(View):
    
    def get(self,request):
        form = UserCreationForm()
        return render(request, 'autenticacion/register.html', {'form':form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f"Bienvenido a la plataforma {nombre_usuario}")
            login(request, usuario)
            return redirect('index')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'autenticacion/register.html', {'form':form})

def salir(request):
    logout(request)
    messages.success(request, f"Tu sesion se ha cerrado correctamente")
    return redirect('acceder')





# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data('username')
#             messages.success(request, f"Usuario {username} creado")
#             return redirect('index')
#     else:
#         form = UserRegisterForm()

#     context = {'form':form}
#     return render(request, 'autenticacion/register.html', context)



