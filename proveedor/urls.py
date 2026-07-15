from django.urls import path
from .views import ProveedorView, ProveedorViewId, ProveedorViewNombre

urlpatterns = [
    path('proveedor/', ProveedorView.as_view(), name='proveedor'),
    path('proveedor/<int:id>', ProveedorViewId.as_view()),
    path('proveedor/nombre/<str:nombre>', ProveedorViewNombre.as_view()),
]
