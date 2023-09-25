from django.db import models

# Create your models here.

class Zona(models.Model):
    nombre_zona = models.CharField(max_length=50)
    cant_pacientes = models.IntegerField()
    def __str__(self):
        return self.nombre_zona
    
    
class Reporte(models.Model):
    tipo_reporte = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    
class Medico(models.Model):
    nombre_medico = models.CharField(max_length=100)
    apellido_medico = models.CharField(max_length=100)
    dni_medico = models.CharField(max_length=100)
    fecha_nac_medico = models.DateField()
    domicilio_medico = models.CharField(max_length=100)
    zona = models.ForeignKey(Zona, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_medico
    
class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    dni_paciente = models.CharField(max_length=100)
    fecha_nac_paciente = models.DateField()
    medico_asignado = models.ForeignKey(Medico, null=True, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, default=None, on_delete=models.CASCADE)
    domicilio_paciente = models.CharField(max_length=100, default="")

    genero_paciente = models.CharField(max_length=1, default="")
    telefono_paciente = models.IntegerField(default="")
    email_paciente = models.CharField(max_length=100, default="")
    grupo_sanguineo = models.CharField(max_length=5, default="")
    factor_rh = models.BooleanField(default=False)
    peso_paciente_kg = models.IntegerField(default=0)
    altura_paciente = models.IntegerField(default=0)
    alergias = models.TextField(default="")
    consulta = models.TextField(default="")


# Editar informacion de paciente
# Asignar formas de llamado
# Crear tabla Profile, para que al crearse un usuario comun, se cree un perfil. Y solo un admin puede agregar pacientes si este tiene perfil. Y desde ese perfil, puede activar llamado.
# Aumentar datos pacientes
# Usuario generico
# Calcular tiempo de respuesta promedio
# Visualizar tablas y graficos
# Filtrar reportes por area, origen del llamado (cama o baño), fecha y hora
# Diseño