from django.shortcuts import render, redirect
from .models import Zona, Paciente, Medico
from .forms import MedicoForm, PacienteForm
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
    
def agregarMedico(req):
    
    if req.method == 'POST':
        nombre_medico = req.POST['nombre_medico']
        apellido_medico = req.POST['apellido_medico']  
        dni_medico = req.POST['dni_medico']
        fecha_nac_medico = req.POST['fecha_nac_medico']
        domicilio_medico = req.POST['domicilio_medico']
        nueva_zona = Zona(nombre_medico=nombre_medico, apellido_medico=apellido_medico, dni_medico=dni_medico, fecha_nac_medico=fecha_nac_medico, domicilio_medico=domicilio_medico)
        nueva_zona.save()
        return redirect('/')
    else:
        return render(req, 'agregarEnfermero.html',{
            "form": MedicoForm
        })

def detalle_zona(req, id):
    medicos = Medico.objects.all().filter(zona = id)
    pacientes = Paciente.objects.all().filter(zona = id)
    zona = Zona.objects.get(id=id)
    return render(req, 'detalle_zona.html',{
        "pacientes":pacientes,
        "zona": zona,
        "medicos": medicos,
        "formPaciente": PacienteForm
        
    })
    
def crear_paciente(req, zona_id):
    zona_id = Zona.objects.get(id=zona_id)
    if req.method == 'POST':
        nombre_paciente = req.POST['nombre_paciente']
        apellido_paciente = req.POST['apellido_paciente']
        fecha_nac_paciente = req.POST['fecha_nac']
        DNI_paciente = req.POST['DNI_paciente']
        nuevo_paciente = Paciente(nombre_paciente=nombre_paciente, apellido_paciente=apellido_paciente, fecha_nac_paciente=fecha_nac_paciente, dni_paciente=DNI_paciente, zona=zona_id)
        nuevo_paciente.save()
    return redirect('/')
    

def pacientes(req):
    
    pacientes = Paciente.objects.all()
    return render(req, 'listaPacientes.html',{
        "pacientes":pacientes,
    })
    
def asignarMedico(request, id):
    if request.method == "POST":
        paciente = Paciente.objects.get(id=id)
        medico_id = request.POST["medico_id"]
        print(medico_id)
        if medico_id:
            medico = Medico.objects.get(id=medico_id)
            paciente.medico_asignado = medico
            paciente.save()
    return redirect("/")

# def editar_paciente(request, paciente_id):
#     paciente = Paciente.objects.get(id=paciente_id)

#     if request.method == 'POST':
#         form = PacienteForm(request.POST, instance=paciente)

#     return render(request, 'detalle_zona.html', {'formPaciente': form})