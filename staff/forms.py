from django import forms
from .models import Vendedor, Chofer
import re

# --- Validaciones reutilizables ---
def validar_solo_letras(valor):
    if not valor.isalpha():
        raise forms.ValidationError('Este campo debe contener solo letras.')

def validar_solo_numeros(valor):
    if not re.match(r'^\d+$', valor):
        raise forms.ValidationError('El número de teléfono debe contener solo números.')

# --- Formulario Base ---
class BaseStaffForm(forms.ModelForm):
    # Aplicamos validaciones a los campos heredados
    nombre = forms.CharField(validators=[validar_solo_letras])
    apellido = forms.CharField(validators=[validar_solo_letras])
    telefono = forms.CharField(validators=[validar_solo_numeros])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asignamos clases de Bootstrap a todos los campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Personalizamos el widget de fecha
        self.fields['fecha_alta'].widget = forms.DateInput(
            format='%Y-%m-%d',
            attrs={'class': 'form-control', 'type': 'date'}
        )

    class Meta:
        abstract = True # No es un formulario que se usará directamente
        fields = ['nombre', 'apellido', 'email', 'direccion', 'telefono', 'fecha_alta']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
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