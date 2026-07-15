from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializer import ProveedorEntrada
from django.db import connection


class ProveedorView(APIView):

    @swagger_auto_schema(
        operation_description="Guardar proveedor",
        request_body=ProveedorEntrada,
    )
    def post(self, request):
        nombre = request.data.get('nombre')
        telefono = request.data.get('telefono')
        correo = request.data.get('correo')

        if nombre != '' and telefono != '' and correo != '':
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO proveedor (nombre, telefono, correo) VALUES (%s, %s, %s)",
                    [nombre, telefono, correo]
                )

            return Response({
                "mensaje": "Proveedor guardado correctamente"
            })

    @swagger_auto_schema(
        operation_description="Mostrar proveedores",
    )
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM proveedor")
            datos = cursor.fetchall()

            proveedores = []

            for fila in datos:
                proveedores.append({
                    "id": fila[0],
                    "nombre": fila[1],
                    "telefono": fila[2],
                    "correo": fila[3]
                })

        return Response(proveedores)


class ProveedorViewId(APIView):

    @swagger_auto_schema(
        operation_description="Buscar proveedor por id",
    )
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM proveedor WHERE id=%s",
                [id]
            )

            respuesta = cursor.fetchone()

            dato = {
                "id": respuesta[0],
                "nombre": respuesta[1],
                "telefono": respuesta[2],
                "correo": respuesta[3]
            }

        return Response(dato)

    @swagger_auto_schema(
        operation_description="Eliminar proveedor",
    )
    def delete(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM proveedor WHERE id=%s",
                [id]
            )

        return Response({
            "mensaje": "Proveedor eliminado"
        })

    @swagger_auto_schema(
        operation_description="Actualizar proveedor",
        request_body=ProveedorEntrada,
    )
    def put(self, request, id):
        nombre = request.data.get("nombre")
        telefono = request.data.get("telefono")
        correo = request.data.get("correo")

        with connection.cursor() as cursor:
            cursor.execute(
                "UPDATE proveedor SET nombre=%s, telefono=%s, correo=%s WHERE id=%s",
                [nombre, telefono, correo, id]
            )

        return Response({
            "mensaje": "Proveedor actualizado correctamente"
        })


class ProveedorViewNombre(APIView):

    @swagger_auto_schema(
        operation_description="Buscar proveedor por nombre",
    )
    def get(self, request, nombre):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM proveedor WHERE nombre=%s",
                [nombre]
            )

            datos = cursor.fetchall()

            proveedores = []

            for fila in datos:
                proveedores.append({
                    "id": fila[0],
                    "nombre": fila[1],
                    "telefono": fila[2],
                    "correo": fila[3]
                })

        return Response(proveedores)