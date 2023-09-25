from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Zona)
admin.site.register(models.Paciente)
admin.site.register(models.Medico)