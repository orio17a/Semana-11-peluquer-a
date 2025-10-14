from django.shortcuts import render


#---------------------------------- LOGIN y demas en uso ----------------------------------
#from del registro
from .forms import CustomUserCreationForm 
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect

##para poner mensajes
from django.contrib import messages

##############################################################################
from .models import Cliente, Empleado, Servicios, Turnos

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})

def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

def lista_servicios(request):
    servicios = Servicios.objects.all()
    return render(request, 'servicios/servicios.html', {'servicios': servicios})

def lista_turnos(request):
    turnos = Turnos.objects.all()
    return render(request, 'turnos/turnos.html', {'turnos': turnos})

def coloracion (request):
    return render(request, 'coloracion/coloracion.html')

def corte (request):
    return render(request, 'corte/corte.html')

def tratamiento (request):
    return render(request, 'tratamiento/tratamiento.html')

def home(request):
    return render(request, "index/index.html")

##############################################################################


#---------------------------------- LOGIN y demas en uso ----------------------------------

##Registro Usuario

def register(request):
    #
    if request.method == 'POST':
        form = CustomUserCreationForm (request.POST)
        if form.is_valid():
            usuario = form.save() #guarda el usuario
            
            nombre_usuario = form.cleaned_data.get('username')   #nuevo esto manda mensajes
            messages.success(request, f'Nueva Cuenta creada para: {nombre_usuario}')
            
            login(request, usuario)   #logea al usuario
            return redirect('home')   #redirecciona a la pagina principal
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}') ##msg es una llave para mostrar al usuario en caso de error
    #
    form = CustomUserCreationForm ()
    return render(request, 'registro/registro.html', {"form":form}) #recomendable aca utilizar el mismo nombre en la variable


##para cerrar sesion
def logout_request(request):
    logout(request)
    messages.info(request, "Has cerrado sesion exitosamente")
    return redirect('home')


##para iniciar sesion
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=nombre_usuario, password=contrasena)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {nombre_usuario}')
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contrasena incorrecta')
        else:
            messages.error(request, 'Usuario o contrasena incorrecta')
    
    form = AuthenticationForm() #esto es para que aparezca el formulario vacio
    return render(request, 'login/Login.html', {'form':form})

#---------------------------------- LOGIN y demas en uso ----------------------------------