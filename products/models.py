from django.db import models
from django.utils.text import slugify

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
        on_delete=models.SET_NULL,
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
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="Categoría"
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