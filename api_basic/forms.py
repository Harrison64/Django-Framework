from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import departamento, trabajador, cliente, ventas

class departamentoForm(forms.ModelForm):
    class Meta:
        model = departamento
        fields = ['dep_cod', 'dep_nom', 'dep_tel', 'dep_ubica', 'dep_mod']

class trabajadorForm(forms.ModelForm):
    class Meta:
        model = trabajador
        fields = [
            'tra_cod', 'tra_nom', 'tra_apell', 'tra_tel', 'tra_cargo', 'tra_sal'
        ]

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = [
            'cli_cod', 'cli_nom', 'cli_apell', 'cli_tel'
        ]

class ventasForm(forms.ModelForm):
    class Meta:
        model = ventas
        fields = [
            'ven_codp', 'ven_nom', 'ven_descrip', 'ven_costo'
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']