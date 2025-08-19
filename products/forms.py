from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    """
    Formulario para crear/editar productos.
    """
    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'category', 'price', 'stock', 'available']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CategoryForm(forms.ModelForm):
    """
    Formulario para crear/editar categorías de productos.
    """
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
