from django.urls import path
from .views import departamentolist, trabajadorlist, clientelist, ventaslist, crearDepartamento, listarDepartamento, listarTrabajador, crearTrabajador, crearCliente, listarCliente, crearVentas, listarVentas, logUsuario, regUsuario, Home, logouUsuario

urlpatterns = [
    path('departamento/', departamentolist.as_view(), name = 'departamento_list'),
    path('trabajador/', trabajadorlist.as_view(), name = 'trabajador_list'),
    path('cliente/', clientelist.as_view(), name = 'cliente_list'),
    path('ventas/', ventaslist.as_view(), name = 'ventas_list'),
    path('crear_departamento/', crearDepartamento, name = "crear_departamento"),
    path('listar_departamento/', listarDepartamento, name = 'listar_departamento'),
    path('listar_trabajador/', listarTrabajador, name = 'listar_trabajador'),
    path('crear_trabajador/', crearTrabajador, name = 'crear_trabajador'),
    path('crear_cliente/', crearCliente, name = 'crear_cliente'),
    path('listar_cliente/', listarCliente, name = 'listar_cliente'),
    path('crear_ventas/', crearVentas, name = 'crear_ventas'),
    path('listar_ventas/', listarVentas, name = 'listar_ventas'),
    path('login/', logUsuario, name = 'login'),
    path('logout/', logUsuario, name = 'logout'),
    path('registro/', regUsuario, name = 'registro'),
]