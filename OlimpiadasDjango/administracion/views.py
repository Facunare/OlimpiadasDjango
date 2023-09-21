from django.shortcuts import render, redirect
from .models import Zona, Paciente
# Create your views here.

def agregarZona(req):
    if req.method == 'POST':
        nombre_zona = req.POST['nombre_zona']
        cant_pacientes = req.POST['cant_pacientes']

        nueva_zona = Zona(nombre_zona=nombre_zona, cant_pacientes=cant_pacientes)
        nueva_zona.save()
        return redirect('/')
    else:
        return render(req, 'agregarZona.html')

def detalle_zona(req, id):
    
    pacientes = Paciente.objects.all().filter(zona = id)
    return render(req, 'detalle_zona.html',{
        "pacientes":pacientes,
        "zona_id": id
    })
    
def crear_paciente(req, zona_id):
    zona_id = Zona.objects.get(id=7)
    if req.method == 'POST':
        nombre_paciente = req.POST['nombre_paciente']
        apellido_paciente = req.POST['apellido_paciente']
        fecha_nac_paciente = req.POST['fecha_nac']
        DNI_paciente = req.POST['DNI_paciente']
        nuevo_paciente = Paciente(nombre_paciente=nombre_paciente, apellido_paciente=apellido_paciente, fecha_nac_paciente=fecha_nac_paciente, dni_paciente=DNI_paciente, zona=zona_id)
        nuevo_paciente.save()
    return redirect('/')
    
