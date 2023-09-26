from django.contrib import admin
from . import models

# Registramos todas las tablas en el Admin panel

admin.site.register(models.Zona)
admin.site.register(models.Paciente)
admin.site.register(models.Medico)
admin.site.register(models.Perfil)
admin.site.register(models.Llamado)
admin.site.register(models.Reporte)
