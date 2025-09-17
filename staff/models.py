from django.db import models
from django.utils import timezone

class BaseStaff(models.Model):
    """
    Modelo base abstracto con campos comunes para Vendedores y Choferes.
    """
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15, unique=True, verbose_name="DNI") 
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    # Fechas y estado
    fecha_alta = models.DateField(default=timezone.now)
    fecha_baja = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        abstract = True # Indicamos que es un modelo abstracto

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Vendedor(BaseStaff):
    """
    Modelo para los vendedores. Hereda todos los campos de BaseStaff.
    Aquí puedes agregar campos específicos para vendedores en el futuro.
    """
    # Ejemplo a futuro: models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pass 

class Chofer(BaseStaff):
    """
    Modelo para los choferes. Hereda todos los campos de BaseStaff.
    Aquí puedes agregar campos específicos para choferes en el futuro.
    """
    # Ejemplo a futuro: models.CharField(max_length=10, help_text="Licencia de conducir")
    pass