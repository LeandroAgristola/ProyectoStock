from django import forms
from .models import Product, Category

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
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Alta → disponible = True
        if not self.instance.pk:
            self.fields['available'].initial = True

        # Cuando se edita, setear automáticamente el padre y filtrar subcategorías
        if self.instance.pk and self.instance.category:
            if self.instance.category.parent:
                parent = self.instance.category.parent
                self.fields['parent_category'].initial = parent
                self.fields['category'].queryset = Category.objects.filter(parent=parent)
            else:
                # Si la categoría elegida es padre, que aparezca vacía en subcategorías
                self.fields['category'].queryset = Category.objects.none()
        else:
            # En alta inicial, sin padre, no mostrar subcategorías
            self.fields['category'].queryset = Category.objects.none()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']  # solo nombre
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }