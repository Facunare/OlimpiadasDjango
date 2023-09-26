from django.shortcuts import render, redirect
from .models import Zona, Paciente, Medico, Perfil, Reporte, Llamado
from .forms import MedicoForm, PacienteForm
from datetime import datetime, time, timedelta
import csv
from django.http import HttpResponse
import json

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
        zona = Zona.objects.get(id=int(req.POST['zona']))
        
        nuevo_medico = Medico(zona=zona,nombre_medico=nombre_medico, apellido_medico=apellido_medico, dni_medico=dni_medico, fecha_nac_medico=fecha_nac_medico, domicilio_medico=domicilio_medico)
        nuevo_medico.save()
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
        fecha_nac_paciente = req.POST['fecha_nac_paciente']
        DNI_paciente = req.POST['dni_paciente']
        domicilio_paciente = req.POST['domicilio_paciente']
        genero_paciente = req.POST['genero_paciente']
        telefono_paciente = req.POST['telefono_paciente']
        email_paciente = req.POST['email_paciente']
        grupo_sanguineo = req.POST['grupo_sanguineo']
        peso_paciente_kg = req.POST['peso_paciente_kg']
        altura_paciente = req.POST['altura_paciente']
        alergias = req.POST['alergias']
        perfil = Perfil.objects.get(id=req.POST['perfil'])
        nuevo_paciente = Paciente(perfil=perfil,domicilio_paciente=domicilio_paciente, genero_paciente=genero_paciente, telefono_paciente=telefono_paciente,
        email_paciente=email_paciente, grupo_sanguineo=grupo_sanguineo,peso_paciente_kg=peso_paciente_kg, altura_paciente=altura_paciente, alergias=alergias, nombre_paciente=nombre_paciente, apellido_paciente=apellido_paciente, fecha_nac_paciente=fecha_nac_paciente, dni_paciente=int(DNI_paciente), zona=zona_id)
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


def editar_paciente(req, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    
    if req.method == 'POST':
        form = PacienteForm(req.POST, instance=paciente)
        if form.is_valid():
            form.save()  
            return redirect('/') 
    else:
        form = PacienteForm(instance=paciente)
    
    return render(req, 'editar_pacientes.html', {'form': form})

def verPerfil(req):
    perfil = Perfil.objects.get(user=req.user)

    try:
        paciente = Paciente.objects.get(perfil=perfil)
        paciente_encontrado = True
    except Paciente.DoesNotExist:
        paciente = None
        paciente_encontrado = False

    return render(req, 'perfil.html', {
        'perfil':perfil,
        'paciente_encontrado': paciente_encontrado
    })

def llamar(req, id, type):
    paciente = Paciente.objects.get(perfil_id=id)
    if(type==0):
        paciente.perfil.isCalling = True
    else:
        paciente.perfil.isCallingNormal = True
    
    print(req.POST['origen'])
    nuevo_llamado = Llamado(paciente = paciente, zona = paciente.zona, origen = req.POST['origen'])
    nuevo_llamado.save()
    paciente.perfil.save()
    return render(req, 'perfil.html', {
        'perfil':paciente.perfil
    })


def generarReporte(req, id):
    paciente = Paciente.objects.get(id=id)
    ultimo_llamado = Llamado.objects.filter(paciente = paciente).latest('created_at')
    if(paciente.perfil.isCalling):
        tipo = 'Emergencia'
    else:
        tipo = 'Normal'
    if req.method == "POST":
    
        nuevo_reporte = Reporte(tipo=tipo, consulta = req.POST['consulta'], zona = paciente.zona, llamado = ultimo_llamado)
        nuevo_reporte.save()

        paciente.perfil.isCalling = False
        paciente.perfil.isCallingNormal = False
        paciente.perfil.save()
        return redirect('/')
    else:
        return render(req, 'generarReporte.html', {
            'paciente':paciente
        })


def verReportes(req):
    zonas = Zona.objects.all()
    reportes = Reporte.objects.all()
    tiempo_promedio = []
    for reporte in reportes:
        fecha_inicio = reporte.llamado.created_at
        fecha_finalizacion = reporte.created_at
        tiempo_transcurrido = fecha_finalizacion - fecha_inicio
        tiempo_transcurrido_en_segundos = tiempo_transcurrido.total_seconds()
        tiempo_transcurrido_en_minutos = tiempo_transcurrido_en_segundos / 60
        tiempo_transcurrido_en_minutos_redondeado = round(tiempo_transcurrido_en_minutos, 2)
        tiempo_promedio.append(tiempo_transcurrido_en_minutos_redondeado)

    tiempo_promedio = sum(tiempo_promedio) / len(reportes)


    if req.method == "POST":
        zona_id = req.POST.get('filtroZona')
        origen_llamado = req.POST.get('origenLlamado')
        fecha_reporte = req.POST.get('fechaReporte')
        hora_reporte = req.POST.get('horaReporte')
        
        filtros = {}
        
        if zona_id:
            filtros['llamado__zona_id'] = zona_id
        
        if origen_llamado != 'todos':
            filtros['llamado__origen__icontains'] = origen_llamado
        
        if fecha_reporte:
            fecha_reporte = datetime.strptime(fecha_reporte, '%Y-%m-%d').date()
            filtros['created_at__date'] = fecha_reporte
        
        if hora_reporte:
            hora_reporte = datetime.strptime(hora_reporte, '%H:%M').time()
            rango_inicio = (datetime.combine(datetime.today(), hora_reporte) - timedelta(minutes=5)).time()
            rango_fin = (datetime.combine(datetime.today(), hora_reporte) + timedelta(minutes=5)).time()
            filtros['created_at__time__gte'] = rango_inicio
            filtros['created_at__time__lte'] = rango_fin
        
        reportes = Reporte.objects.filter(**filtros)
    
    return render(req, 'reportes.html', {
        'reportes': reportes,
        'zonas': zonas,
        'tiempo_promedio':tiempo_promedio,
        'zonaReporte':list(zonas)
    })

def agregarPaciente(req):
    print(req.POST['zona_id'])
    return render(req, 'agregarPaciente.html',{
        'id': req.POST['zona_id'],
        "formPaciente": PacienteForm
    })

def exportarReporte(req):
    reportes = Reporte.objects.all()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=reportes.csv' 
    writer = csv.writer(response)

    writer.writerow(['Tipo', 'Consulta', 'Zona', 'Llamado', 'Hora Reporte'])

    reportes_fields = reportes.values_list('tipo', 'consulta', 'zona', 'llamado', 'created_at')


    for reporte in reportes_fields:
        writer.writerow(reporte)
    
    return response

def exportarIdReporte(req, id):
    reportes = Reporte.objects.values_list('tipo', 'consulta', 'zona', 'llamado', 'created_at').get(id=id)
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=reportes.csv' 
    writer = csv.writer(response)

    writer.writerow(['Tipo', 'Consulta', 'Zona', 'Llamado', 'Hora Reporte'])

    writer.writerow(reportes)
    
    return response

