
from django.urls import path, include
from . import views
urlpatterns = [
    path('agregarZona/', views.agregarZona, name='agregarZona'),
    path('agregarMedico/', views.agregarMedico, name='agregarMedico'),
    path('detalle_zona/<int:id>/', views.detalle_zona, name="detalle_zona"),
    path('crear_paciente/<int:zona_id>/', views.crear_paciente, name="crear_paciente"),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('asignarMedico/<int:id>', views.asignarMedico, name="asignarMedico"),
    # path('editar_paciente/<int:paciente_id>', views, name="editar_paciente")
    path('perfil/', views.verPerfil, name="perfil"),
    path('llamar/<int:id>', views.llamar, name="llamar"),
]
