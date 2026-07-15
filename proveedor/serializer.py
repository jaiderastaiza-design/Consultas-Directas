from rest_framework import serializers

class ProveedorEntrada(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    telefono = serializers.CharField(max_length=20)
    correo = serializers.EmailField()


class ProveedorSalida(serializers.Serializer):
    mensaje = serializers.CharField(max_length=100)