
from django.urls import path, include
from . import views
urlpatterns = [
    path('agregarZona/', views.agregarZona, name='agregarZona'),
    path('agregarMedico/', views.agregarMedico, name='agregarMedico'),
    path('detalle_zona/<int:id>/', views.detalle_zona, name="detalle_zona"),
    path('crear_paciente/<int:zona_id>/', views.crear_paciente, name="crear_paciente"),
    path('pacientes/', views.pacientes, name="pacientes"),
    path('asignarMedico/<int:id>', views.asignarMedico, name="asignarMedico"),
    path('perfil/', views.verPerfil, name="perfil"),
    path('llamar/<int:id>/<int:type>', views.llamar, name="llamar"),
    path('generarReporte/<int:id>', views.generarReporte, name="generarReporte"),
    path('editar_paciente/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('verReportes/', views.verReportes, name='verReportes'),
    path('agregarPaciente/', views.agregarPaciente, name='agregarPaciente'),
    path('exportarReportes/', views.exportarReporte, name='exportarReportes'),
    path('exportarIdReportes/<int:id>', views.exportarIdReporte, name='exportarIdReportes'),
    path('eliminarPaciente/<int:id>', views.eliminarPaciente, name='eliminarPaciente'),
    path('removerZona/<int:id>', views.removerZona, name='removerZona'),
     
]
