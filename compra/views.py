from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializer import CompraEntrada
from django.db import connection


class CompraView(APIView):

    @swagger_auto_schema(
        operation_description="Guardar compra",
        request_body=CompraEntrada,
    )
    def post(self, request):
        fecha_compra = request.data.get('fecha_compra')
        valor_total = request.data.get('valor_total')
        proveedor = request.data.get('proveedor')

        if fecha_compra != '' and valor_total != '' and proveedor != '':
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO compra (fecha_compra, valor_total, proveedor_id) VALUES (%s,%s,%s)",
                    [fecha_compra, valor_total, proveedor]
                )

            return Response({
                "mensaje": "Compra guardada correctamente"
            })

    @swagger_auto_schema(
        operation_description="Mostrar compras",
    )
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT compra.id,
                       compra.fecha_compra,
                       compra.valor_total,
                       proveedor.nombre
                FROM compra
                INNER JOIN proveedor
                ON compra.proveedor_id = proveedor.id
            """)

            datos = cursor.fetchall()

            compras = []

            for fila in datos:
                compras.append({
                    "id": fila[0],
                    "fecha_compra": fila[1],
                    "valor_total": fila[2],
                    "proveedor": fila[3]
                })

        return Response(compras)


class CompraViewId(APIView):

    @swagger_auto_schema(
        operation_description="Buscar compra por id",
    )
    def get(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT compra.id,
                       compra.fecha_compra,
                       compra.valor_total,
                       proveedor.nombre
                FROM compra
                INNER JOIN proveedor
                ON compra.proveedor_id = proveedor.id
                WHERE compra.id=%s
            """, [id])

            respuesta = cursor.fetchone()

            dato = {
                "id": respuesta[0],
                "fecha_compra": respuesta[1],
                "valor_total": respuesta[2],
                "proveedor": respuesta[3]
            }

        return Response(dato)

    @swagger_auto_schema(
        operation_description="Eliminar compra",
    )
    def delete(self, request, id):
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM compra WHERE id=%s",
                [id]
            )

        return Response({
            "mensaje": "Compra eliminada"
        })

    @swagger_auto_schema(
        operation_description="Actualizar compra",
        request_body=CompraEntrada,
    )
    def put(self, request, id):
        fecha_compra = request.data.get("fecha_compra")
        valor_total = request.data.get("valor_total")
        proveedor = request.data.get("proveedor")

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE compra
                SET fecha_compra=%s,
                    valor_total=%s,
                    proveedor_id=%s
                WHERE id=%s
            """, [fecha_compra, valor_total, proveedor, id])

        return Response({
            "mensaje": "Compra actualizada correctamente"
        })


class CompraViewFecha(APIView):

    @swagger_auto_schema(
        operation_description="Buscar compras por fecha",
    )
    def get(self, request, fecha):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT compra.id,
                       compra.fecha_compra,
                       compra.valor_total,
                       proveedor.nombre
                FROM compra
                INNER JOIN proveedor
                ON compra.proveedor_id = proveedor.id
                WHERE compra.fecha_compra=%s
            """, [fecha])

            datos = cursor.fetchall()

            compras = []

            for fila in datos:
                compras.append({
                    "id": fila[0],
                    "fecha_compra": fila[1],
                    "valor_total": fila[2],
                    "proveedor": fila[3]
                })

        return Response(compras)


class CompraViewProveedor(APIView):

    @swagger_auto_schema(
        operation_description="Buscar compras por proveedor",
    )
    def get(self, request, proveedor):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT compra.id,
                       compra.fecha_compra,
                       compra.valor_total,
                       proveedor.nombre
                FROM compra
                INNER JOIN proveedor
                ON compra.proveedor_id = proveedor.id
                WHERE proveedor.id=%s
            """, [proveedor])

            datos = cursor.fetchall()

            compras = []

            for fila in datos:
                compras.append({
                    "id": fila[0],
                    "fecha_compra": fila[1],
                    "valor_total": fila[2],
                    "proveedor": fila[3]
                })

        return Response(compras)


class CompraViewValorMinimo(APIView):

    @swagger_auto_schema(
        operation_description="Buscar compras por valor mínimo",
    )
    def get(self, request, valor):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT compra.id,
                       compra.fecha_compra,
                       compra.valor_total,
                       proveedor.nombre
                FROM compra
                INNER JOIN proveedor
                ON compra.proveedor_id = proveedor.id
                WHERE compra.valor_total >= %s
            """, [valor])

            datos = cursor.fetchall()

            compras = []

            for fila in datos:
                compras.append({
                    "id": fila[0],
                    "fecha_compra": fila[1],
                    "valor_total": fila[2],
                    "proveedor": fila[3]
                })

        return Response(compras)


class CompraViewValorMaximo(APIView):

    @swagger_auto_schema(
        operation_description="Buscar compras por valor máximo",
    )
    def get(self, request, valor):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT compra.id,
                       compra.fecha_compra,
                       compra.valor_total,
                       proveedor.nombre
                FROM compra
                INNER JOIN proveedor
                ON compra.proveedor_id = proveedor.id
                WHERE compra.valor_total <= %s
            """, [valor])

            datos = cursor.fetchall()

            compras = []

            for fila in datos:
                compras.append({
                    "id": fila[0],
                    "fecha_compra": fila[1],
                    "valor_total": fila[2],
                    "proveedor": fila[3]
                })

        return Response(compras)