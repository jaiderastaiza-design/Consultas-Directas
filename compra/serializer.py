from rest_framework import serializers

class CompraEntrada(serializers.Serializer):
    fecha_compra = serializers.DateField()
    valor_total = serializers.DecimalField(max_digits=10, decimal_places=2)
    proveedor = serializers.IntegerField()


class CompraSalida(serializers.Serializer):
    mensaje = serializers.CharField(max_length=100)