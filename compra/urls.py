from django.urls import path
from .views import (
    CompraView,
    CompraViewId,
    CompraViewFecha,
    CompraViewProveedor,
    CompraViewValorMinimo,
    CompraViewValorMaximo
)

urlpatterns = [
    path('compra/', CompraView.as_view(), name='compra'),
    path('compra/<int:id>', CompraViewId.as_view()),
    path('compra/fecha/<str:fecha>', CompraViewFecha.as_view()),
    path('compra/proveedor/<int:proveedor>', CompraViewProveedor.as_view()),
    path('compra/valormin/<int:valor>', CompraViewValorMinimo.as_view()),
    path('compra/valormax/<int:valor>', CompraViewValorMaximo.as_view()),
]