from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    class Meta:
        db_table = "proveedor"

    def __str__(self):
        return self.nombre