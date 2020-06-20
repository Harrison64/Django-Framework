from django.contrib import admin
from .models import departamento, trabajador, cliente, ventas

admin.site.register(departamento)
admin.site.register(trabajador)
admin.site.register(cliente)
admin.site.register(ventas)