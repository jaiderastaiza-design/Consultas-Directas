from django.db import models
from proveedor.models import Proveedor

class Compra(models.Model):
    fecha_compra = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = "compra"

    def __str__(self):
        return f"Compra {self.id}"