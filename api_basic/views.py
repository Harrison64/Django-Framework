from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import generics


from .models import departamento, trabajador, cliente, ventas
from .forms import departamentoForm, trabajadorForm, clienteForm, ventasForm, CreateUserForm

from .serializers import departamentoSerializer, trabajadorSerializer, clienteSerializer, ventasSerializer


class departamentolist(generics.ListCreateAPIView):
    queryset = departamento.objects.all()
    serializer_class = departamentoSerializer

class trabajadorlist(generics.ListCreateAPIView):
    queryset = trabajador.objects.all()
    serializer_class = trabajadorSerializer

class clientelist(generics.ListCreateAPIView):
    queryset = cliente.objects.all()
    serializer_class = clienteSerializer

class ventaslist(generics.ListCreateAPIView):
    queryset = ventas.objects.all()
    serializer_class = ventasSerializer

@login_required(login_url='login')
def Home(request):
    return render(request,'index.html')

@login_required(login_url='login')
def crearDepartamento(request):
    if request.method == 'POST':
        departamento_form = departamentoForm(request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect('index')
    else:
        departamento_form = departamentoForm()
    return render(request,'api_basic/crear_departamento.html',{'departamento_form':departamento_form})

@login_required(login_url='login')
def listarDepartamento(request):
    departamentos = departamento.objects.all()
    return render(request,'api_basic/listar_departamento.html',{'departamentos':departamentos})

@login_required(login_url='login')
def crearTrabajador(request):
    if request.method == 'POST':
        trabajador_form = trabajadorForm(request.POST)
        if trabajador_form.is_valid():
            trabajador_form.save()
            return redirect('index')
    else:
        trabajador_form = trabajadorForm()
    return render(request,'api_basic/crear_trabajador.html',{'trabajador_form':trabajador_form})

@login_required(login_url='login')
def listarTrabajador(request):
    trabajadores = trabajador.objects.all()
    return render(request,'api_basic/listar_trabajador.html',{'trabajadores':trabajadores})

@login_required(login_url='login')
def crearCliente(request):
    if request.method == 'POST':
        cliente_form = clienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('index')
    else:
        cliente_form = clienteForm()
    return render(request,'api_basic/crear_cliente.html',{'cliente_form':cliente_form})

@login_required(login_url='login')
def listarCliente(request):
    clientes = cliente.objects.all()
    return render(request,'api_basic/listar_cliente.html',{'clientes':clientes})

@login_required(login_url='login')
def crearVentas(request):
    if request.method == 'POST':
        ventas_form = ventasForm(request.POST)
        if ventas_form.is_valid():
            ventas_form.save()
            return redirect('index')
    else:
        ventas_form = ventasForm()
    return render(request,'api_basic/crear_ventas.html',{'ventas_form':ventas_form})

@login_required(login_url='login')
def listarVentas(request):
    venta = ventas.objects.all()
    return render(request,'api_basic/listar_ventas.html',{'venta':venta})

def regUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                messages.success(request, 'Esta cuenta fue creada por ' + user)
                form.save()
                return redirect ('login')

        context = {'form':form}
        return render(request, 'cuentas/registro.html', context)

def logUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Nombre de usuario o contraseña incorrecta')
                
        context = {}
        return render(request, 'cuentas/login.html', context)

def logouUsuario(request):
    logout(request)
    return redirect('login')