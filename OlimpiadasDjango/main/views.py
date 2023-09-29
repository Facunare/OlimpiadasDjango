from django.shortcuts import render
from administracion import models

# Vista Pagina principal

def main(request):
    return render(request, 'main.html')
    
def zonas(request):
    zonas = models.Zona.objects.all() # Se muestran todas las zonas con sus datos.
    for zona in zonas:
        zona.cantidad_actual_pacientes = zona.paciente_set.count() # Permite ver la cantidad de pacientes actuales que tiene cada zona
    return render(request, 'home.html',{
        'zonas': zonas
    })
