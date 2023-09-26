
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
<<<<<<< HEAD
    path('exportarReportes/', views.exportarReporte, name='exportarReportes'),
    path('exportarIdReportes/<int:reportes_id>', views.exportarIdReporte, name='exportarIdReportes'),
=======
    path('agregarPaciente/', views.agregarPaciente, name='agregarPaciente'),
    path('exportarReportes/', views.exportarReporte, name='exportarReportes'),
    path('exportarIdReportes/<int:id>', views.exportarIdReporte, name='exportarIdReportes'),
>>>>>>> f7309f055de9bea0464e18778ea231af492d0b30
     
]
