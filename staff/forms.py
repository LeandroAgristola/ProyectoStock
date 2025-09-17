# staff/forms.py

from django import forms
from .models import Vendedor, Chofer
import re

# --- Validaciones reutilizables ---
def validar_solo_letras(valor):
    if not valor.isalpha():
        raise forms.ValidationError('Este campo debe contener solo letras.')

def validar_solo_numeros(valor):
    if not re.match(r'^\d+$', valor):
        raise forms.ValidationError('Este campo debe contener solo números.')

# --- Formulario Base ---
class BaseStaffForm(forms.ModelForm):
    nombre = forms.CharField(validators=[validar_solo_letras])
    apellido = forms.CharField(validators=[validar_solo_letras])
    telefono = forms.CharField(validators=[validar_solo_numeros])
    dni = forms.CharField(validators=[validar_solo_numeros]) # Validación para DNI

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        self.fields['fecha_alta'].widget = forms.DateInput(
            format='%Y-%m-%d',
            attrs={'class': 'form-control', 'type': 'date'}
        )

    class Meta:
        abstract = True
        # Añadimos 'dni' a la lista de campos
        fields = ['nombre', 'apellido', 'dni', 'email', 'direccion', 'telefono', 'fecha_alta']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Solo números, sin puntos'}),
            'email': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Teléfono'}),
        }

# --- Formularios Específicos ---
class VendedorForm(BaseStaffForm):
    class Meta(BaseStaffForm.Meta):
        model = Vendedor

class ChoferForm(BaseStaffForm):
    class Meta(BaseStaffForm.Meta):
        model = Chofer