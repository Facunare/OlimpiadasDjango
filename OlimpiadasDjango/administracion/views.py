import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Zona, Paciente, Medico, Perfil, Reporte, Llamado
from .forms import MedicoForm, PacienteForm
from datetime import datetime, time, timedelta
from django.db.models import Count
import csv
from django.http import HttpResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Vista Agregar zona
@staff_member_required
@login_required
def agregarZona(req):

    if req.method == 'POST':
        nombre_zona = req.POST['nombre_zona']
        cant_pacientes = req.POST['cant_pacientes']
        foto = req.FILES['zonaFoto']
        
        if int(cant_pacientes)<=0:
            return render(req, 'agregarZona.html',{
                "error": "La cantidad de pacientes debe ser mayor o igual 1"
            })
        if nombre_zona=="":
            return render(req, 'agregarZona.html',{
                "error": "Escribe un nombre"
            })
            
     
        nueva_zona = Zona(nombre_zona=nombre_zona, cant_pacientes=cant_pacientes, foto = foto) # Se agregan los datos a la tabla Zona
        nueva_zona.save()
        return redirect('/')
    else:
        return render(req, 'agregarZona.html')
    
# Vista Agregar medico
@staff_member_required
@login_required
def agregarMedico(req):
    
    if req.method == 'POST':
        
        # Recoge los datos pasados por el formulario
        nombre_medico = req.POST['nombre_medico']
        apellido_medico = req.POST['apellido_medico']  
        dni_medico = req.POST['dni_medico']
        fecha_nac_medico = req.POST['fecha_nac_medico']
        domicilio_medico = req.POST['domicilio_medico']
        zona = Zona.objects.get(id=int(req.POST['zona'])) # En base al ID pasado por formulario, busca la zona en la tabla Zona que tenga dicho ID.
        
        nuevo_medico = Medico(zona=zona,nombre_medico=nombre_medico, apellido_medico=apellido_medico, dni_medico=dni_medico, fecha_nac_medico=fecha_nac_medico, domicilio_medico=domicilio_medico)
        nuevo_medico.save()
        return redirect('/')
    else:
        return render(req, 'agregarEnfermero.html',{
            "form": MedicoForm
        })
    
# Vista Detalle de zona

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

# Vista Crear paciente
@staff_member_required    
@login_required
def crear_paciente(req, zona_id):
    zona_id = Zona.objects.get(id=zona_id)

    cantidad_maxima = zona_id.cant_pacientes
    cantidad_actual = zona_id.paciente_set.count()

    if cantidad_actual >= cantidad_maxima:
        print("hola")
        return render(req, 'home.html', {'error_message': 'La zona está llena. No se puede crear más pacientes.'})

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
    return_url = req.GET.get('return_url')
    if return_url:
        return redirect(return_url+str(zona_id.id))
    return redirect('/', id=id)
    
# Vista Lista de pacientes

def pacientes(req):
    
    pacientes = Paciente.objects.all()
    return render(req, 'listaPacientes.html',{
        "pacientes":pacientes,
    })

# Vista Asignar medico
@login_required
@staff_member_required
def asignarMedico(request, id):
    if request.method == "POST":
        paciente = Paciente.objects.get(id=id)
        medico_id = request.POST["medico_id"]
        print(medico_id)
        if medico_id:
            medico = Medico.objects.get(id=medico_id)
            paciente.medico_asignado = medico
            paciente.save()
    return_url = request.GET.get('return_url')
    if return_url:
        return redirect(return_url)
    return redirect('/', id=id)

# Vista Eliminar pacientes
@login_required
@staff_member_required
def eliminarPaciente(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()
    return_url = request.GET.get('return_url')
    if return_url:
        return redirect(return_url)
    return redirect('/pacientes/', id=id)

# Vista Eliminar zona
@login_required
@staff_member_required
def removerZona(request, id):
    zona = Zona.objects.get(id=id)
    zona.delete()
    return redirect('/', id=id)


# Vista editar paciente
@login_required
@staff_member_required
def editar_paciente(req, paciente_id):
    paciente = Paciente.objects.get(id=paciente_id)
    
    if req.method == 'POST':
        form = PacienteForm(req.POST, instance=paciente) 
        if form.is_valid():
            form.save()  
            return redirect('/') 
    else:
        form = PacienteForm(instance=paciente)
    return_url = req.GET.get('return_url')
    if return_url:
        return redirect(return_url)
    return render(req, 'editar_pacientes.html', {'form': form})

# Vista Ver perfil
@login_required
def verPerfil(req):
    perfil = Perfil.objects.get(user=req.user) # Muestra el perfil del usuario actual = (request.user)

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

# Vista Llamar
@login_required
def llamar(req, id, type):
    paciente = Paciente.objects.get(perfil_id=id)
    paciente_encontrado = False
    if paciente:
        paciente_encontrado = True
    if(type==0):
        paciente.perfil.isCalling = True
    else:
        paciente.perfil.isCallingNormal = True
    

    nuevo_llamado = Llamado(paciente = paciente, zona = paciente.zona, origen = req.POST['origen'])
    nuevo_llamado.save()
    paciente.perfil.save()
    
    return render(req, 'perfil.html', {
        'perfil':paciente.perfil,
        'paciente_encontrado': paciente_encontrado
    })

# Vista Generar reporte
@login_required
@staff_member_required
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
        return redirect('/verReportes/')
    else:
        return render(req, 'generarReporte.html', {
            'paciente':paciente
        })

# Vista Ver reportes y calcula tiempo promedio de atencion

def verReportes(req):
    zonasTotales = Zona.objects.all()
    reportes = Reporte.objects.all()
    tiempo_promedio = []
    
    # Calcula el tiempo entre que el paciente toca el boton para llamar al medico, y el momento en que el medico emite el reporte.
    for reporte in reportes:
        fecha_inicio = reporte.llamado.created_at
        fecha_finalizacion = reporte.created_at
        tiempo_transcurrido = fecha_finalizacion - fecha_inicio
        tiempo_transcurrido_en_segundos = tiempo_transcurrido.total_seconds()
        tiempo_transcurrido_en_minutos = tiempo_transcurrido_en_segundos / 60
        tiempo_transcurrido_en_minutos_redondeado = round(tiempo_transcurrido_en_minutos, 2)
        tiempo_promedio.append(tiempo_transcurrido_en_minutos_redondeado)
    if reportes:
        tiempo_promedio = round(sum(tiempo_promedio) / len(reportes), 2)

    # Se aplican los filtros de los reportes
    if req.method == "POST":
        zona_id = req.POST.get('filtroZona')
        origen_llamado = req.POST.get('origenLlamado')
        fecha_reporte = req.POST.get('fechaReporte')
        hora_reporte = req.POST.get('horaReporte')
        
        filtros = {}
        
        if zona_id == "todas":
            print("Todas las opciones")
        else:
            print(zona_id)
            filtros['llamado__zona_id'] = zona_id # Filtrar por zona

        if origen_llamado != 'todos':
            filtros['llamado__origen__icontains'] = origen_llamado # Filtrar por origen de llamado (cama o baño)
            
        
        if fecha_reporte:
            fecha_reporte = datetime.strptime(fecha_reporte, '%Y-%m-%d').date() # Filtrar por fecha
            filtros['created_at__date'] = fecha_reporte
        
        # Filtrar por hora
        if hora_reporte:
            hora_reporte = datetime.strptime(hora_reporte, '%H:%M').time()
            # Esto permite que se acepte un margen de 5 minutos en los reportes. 
            # Es decir, si busco por hora = 10:00:00 aceptara reportes emitidos a las 9:55:00 y a las 10:05:00.
            rango_inicio = (datetime.combine(datetime.today(), hora_reporte) - timedelta(minutes=5)).time()
            rango_fin = (datetime.combine(datetime.today(), hora_reporte) + timedelta(minutes=5)).time() 
            filtros['created_at__time__gte'] = rango_inicio
            filtros['created_at__time__lte'] = rango_fin
        print(filtros)
        reportes = Reporte.objects.filter(**filtros)
        print(reportes)
    
    # Informacion para las graficas   
    pacientes_por_zona = Paciente.objects.values('zona__nombre_zona').annotate(num_pacientes=Count('id')).order_by('zona__nombre_zona')
    zonas = [item['zona__nombre_zona'] for item in pacientes_por_zona]
    num_pacientes_por_zona = [item['num_pacientes'] for item in pacientes_por_zona]
    reportes_por_zona = Reporte.objects.values('zona__nombre_zona').annotate(num_reportes=Count('id')).order_by('zona__nombre_zona')
    zonas_reportes = [item['zona__nombre_zona'] for item in reportes_por_zona]
    num_reportes_por_zona = [item['num_reportes'] for item in reportes_por_zona]
    
    reportes_por_genero = Reporte.objects.values('llamado__paciente__genero_paciente').annotate(num_reportes=Count('id'))
    for item in reportes_por_genero:
        item['porcentaje'] = (item['num_reportes'] / Reporte.objects.count()) * 100
        
    reportes_por_origen = Reporte.objects.values('llamado__origen').annotate(num_reportes=Count('id'))
    for item in reportes_por_origen:
        item['porcentaje'] = (item['num_reportes'] / Reporte.objects.count()) * 100
    return render(req, 'reportes.html', {
        'reportes': reportes,
        'zonas': zonasTotales,
        'tiempo_promedio':tiempo_promedio,
        'zonaReporte':list(zonas), # Esto es para pasar los datos a las estadisticas
        'pacientesPorZona': num_pacientes_por_zona,
        'reportesPorZona': num_reportes_por_zona,
        'zonas_reportes': zonas_reportes,
        'reportesPorGenero': list(reportes_por_genero),
        'reportesPorOrigen': list(reportes_por_origen)
    })

# Vista para agregar pacientes
@staff_member_required
@login_required
def agregarPaciente(req):
    print(req.POST['zona_id'])
    return render(req, 'agregarPaciente.html',{
        'id': req.POST['zona_id'],
        "formPaciente": PacienteForm
    })

# Vista para exportar todos los reportes
@login_required
def exportarReporte(req):
    reportes = Reporte.objects.all()
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=reportes.csv' 
    writer = csv.writer(response)

    writer.writerow(['Paciente', 'Tipo', 'Consulta', 'Zona', 'Llamado', 'Hora Reporte', 'Genero'])

    reportes_fields = reportes.values_list('llamado__paciente__nombre_paciente','tipo', 'consulta', 'zona', 'llamado', 'created_at',  'llamado__paciente__genero_paciente')


    for reporte in reportes_fields:
        writer.writerow(reporte)
    
    return response

# Vista para exportar reportes individualmente
@login_required
def exportarIdReporte(req, id):
    reportes = Reporte.objects.values_list('llamado__paciente__nombre_paciente', 'tipo', 'consulta', 'zona', 'llamado', 'created_at', 'llamado__paciente__genero_paciente').get(id=id)
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=reportes.csv' 
    writer = csv.writer(response)

    writer.writerow(['Paciente', 'Tipo', 'Consulta', 'Zona', 'Llamado', 'Hora Reporte', 'Genero'])

    writer.writerow(reportes)
    
    return response