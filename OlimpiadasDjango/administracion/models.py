from django.db import models

# Create your models here.

class Zona(models.Model):
    nombre_zona = models.CharField(max_length=50)
    cant_pacientes = models.IntegerField()
    
    
class Reporte(models.Model):
    tipo_reporte = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    
class Medico(models.Model):
    nombre_medico = models.CharField(max_length=100)
    apellido_medico = models.CharField(max_length=100)
    dni_medico = models.CharField(max_length=100)
    fecha_nac_medico = models.DateField()
    ubicacion_medico = models.CharField(max_length=100)
    
class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    dni_paciente = models.CharField(max_length=100)
    fecha_nac_paciente = models.DateField()
    # ubicacion_paciente = models.CharField(max_length=100, default=None)
    # medico_asignado = models.ForeignKey(Medico, default=None, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, default=None, on_delete=models.CASCADE)
