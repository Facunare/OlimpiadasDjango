from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Tabla Perfil

class Perfil(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    isCalling = models.BooleanField(default=False)
    isCallingNormal = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

# Tabla Zona

class Zona(models.Model):
    nombre_zona = models.CharField(max_length=50)
    cant_pacientes = models.IntegerField()
    foto = models.ImageField(upload_to='zonaFoto', blank=True, null=True)

    def __str__(self):
        return self.nombre_zona
    
# Tabla Medico
    
class Medico(models.Model):
    nombre_medico = models.CharField(max_length=100)
    apellido_medico = models.CharField(max_length=100)
    dni_medico = models.CharField(max_length=100)
    fecha_nac_medico = models.DateField()
    domicilio_medico = models.CharField(max_length=100)
    zona = models.ForeignKey(Zona, default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_medico
    
# Tabla Paciente

class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    dni_paciente = models.CharField(max_length=100)
    fecha_nac_paciente = models.DateField()
    medico_asignado = models.ForeignKey(Medico, null=True, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, default=None, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, default=None, on_delete=models.CASCADE)
    domicilio_paciente = models.CharField(max_length=100, default="")
    genero_paciente = models.CharField(max_length=1, default="")
    telefono_paciente = models.CharField(null=True, default="", max_length=10)
    email_paciente = models.CharField(max_length=100, default="")
    grupo_sanguineo = models.CharField(max_length=5, default="")
    peso_paciente_kg = models.IntegerField(default=0)
    altura_paciente = models.IntegerField(default=0)
    alergias = models.TextField(default="")
    def __str__(self):
        return self.nombre_paciente

# Tabla Llamado

class Llamado(models.Model):
    paciente = models.ForeignKey(Paciente, default=None, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, default=None, on_delete=models.CASCADE)
    origen = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    
# Tabla Reporte

class Reporte(models.Model):
    tipo = models.CharField(default="", max_length=100)
    consulta = models.TextField(default="")
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE, default=1)
    llamado = models.ForeignKey(Llamado, default=None, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

# Alojar en un servidor con acceso por usuario clave de caracter publico e incluir en la presentacion las credenciales de acceso
# Hacer informe final e incluir bibliografia
# Codigo en formato texto