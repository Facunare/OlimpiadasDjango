
from django.urls import path, include
from . import views
urlpatterns = [
    path('agregarZona/', views.agregarZona, name='agregarZona'),
    path('detalle_zona/<int:id>/', views.detalle_zona, name="detalle_zona"),
    path('crear_paciente/<int:zona_id>/', views.crear_paciente, name="crear_paciente"),
]
