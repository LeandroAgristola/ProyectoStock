from django.db import models
from django.utils.text import slugify

#Modelos para categorias 

class Category(models.Model):
    """
    Modelo para categorías de productos.
    - Utiliza una relación recursiva para crear subcategorías.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    # Relación recursiva para subcategorías
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="Categoría Padre"
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#Modelos para productos

class Product(models.Model):
    """
    Modelo para productos.
    - Relacionado con una categoría.
    - Añadidos los campos 'code' y 'stock' para un inventario adecuado.
    """
    code = models.CharField(max_length=50, unique=True, verbose_name="Código del Producto", blank=True, null=True)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, verbose_name="Descripción")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="products",
        verbose_name="Subcategoría"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Última modificación")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name

#Modelos para combos    

class Combo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    special_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def calculated_price(self):
        """Si no tiene precio especial, devolver suma de productos"""
        total = sum(item.product.price * item.quantity for item in self.items.all())
        return self.special_price if self.special_price else total

    def max_available_stock(self):
        """La cantidad máxima de combos disponibles depende del stock mínimo de sus productos"""
        stocks = []
        for item in self.items.all():
            if item.product.stock is None:
                continue
            if item.product.stock == 0:
                return 0
            stocks.append(item.product.stock // item.quantity)
        return min(stocks) if stocks else 0


class ComboItem(models.Model):
    combo = models.ForeignKey(Combo, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"