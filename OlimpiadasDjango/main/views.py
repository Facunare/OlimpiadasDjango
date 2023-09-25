from django.shortcuts import render
from administracion import models
# Create your views here.

def home(request):
    zonas = models.Zona.objects.all()
    for zona in zonas:
        zona.cantidad_actual_pacientes = zona.paciente_set.count()
    return render(request, 'home.html',{
        'zonas': zonas
    })