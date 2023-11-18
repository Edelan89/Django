from django.urls import path
from .views import VRegistro, cerrar_sesion, logear

urlpatterns = [

    path('', VRegistro.as_view(), name = "Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name = "Autenticacion"),
    path('logear', logear, name = "logear"),
]
