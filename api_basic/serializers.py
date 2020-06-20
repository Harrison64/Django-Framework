from rest_framework import serializers
from .models import departamento
from .models import trabajador
from .models import cliente
from .models import ventas

#Serializador para departamentos
class departamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = departamento
        fields = (
            'id',
            'dep_cod',
            'dep_nom',
            'dep_tel',
            'dep_ubica',
            'dep_mod',
        )

#Serializador para trabajadores
class trabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = trabajador
        fields = (
           'id',
           'tra_cod',
           'tra_nom',
           'tra_apell',
           'tra_tel',
           'tra_cargo',
           'tra_sal', 
        )

#Serializador para clientes
class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = (
           'id',
           'cli_cod',
           'cli_nom',
           'cli_apell',
           'cli_tel',
        )

#Serializador para ventas
class ventasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ventas
        fields = (
           'id',
           'ven_codp',
           'ven_nom',
           'ven_descrip', 
           'ven_costo', 
        ) 