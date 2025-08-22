from django import forms
from django.forms import inlineformset_factory
from .models import Product, Category, Combo, ComboItem



class ProductForm(forms.ModelForm):
    parent_category = forms.ModelChoiceField(
        queryset=Category.objects.filter(parent__isnull=True),
        required=False,
        label="Categoría",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Product
        fields = ['code', 'name', 'description', 'parent_category', 'category', 'price', 'stock', 'available']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Alta → disponible = True
        if not self.instance.pk:
            self.fields['available'].initial = True

        # Si estamos en POST → usar el padre enviado para armar el queryset
        if 'parent_category' in self.data:
            try:
                parent_id = int(self.data.get('parent_category'))
                self.fields['category'].queryset = Category.objects.filter(parent_id=parent_id)
            except (ValueError, TypeError):
                self.fields['category'].queryset = Category.objects.none()
        elif self.instance.pk and self.instance.category:
            # Caso edición
            cat = self.instance.category
            if cat.parent:
                self.fields['parent_category'].initial = cat.parent
                self.fields['category'].queryset = Category.objects.filter(parent=cat.parent)
                self.fields['category'].initial = cat
            else:
                self.fields['parent_category'].initial = cat
                self.fields['category'].queryset = Category.objects.filter(parent=cat)
                self.fields['category'].initial = None
        else:
            # Alta vacía
            self.fields['category'].queryset = Category.objects.none()

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # solo nombre
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = ['name', 'description', 'special_price', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'special_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # que sea realmente opcional
        self.fields['special_price'].required = False  

    def clean_special_price(self):
        value = self.cleaned_data.get('special_price')
        # Si viene vacío → guardamos como None
        if value in ("", None):
            return None
        return value

class ComboItemForm(forms.ModelForm):
    class Meta:
        model = ComboItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

# Inline formset para relacionar Combo con ComboItems
ComboItemFormSet = inlineformset_factory(
    Combo, ComboItem,
    form=ComboItemForm,
    extra=1,          # cantidad de formularios vacíos iniciales
    can_delete=True   # permitir eliminar productos del combo
)