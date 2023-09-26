from django import forms
from .models import Medico, Paciente


# Formulario para la creacion de un medico

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'nombre_medico',
            'apellido_medico',
            'dni_medico',
            'fecha_nac_medico',
            'domicilio_medico',
            'zona',
        ]
        
# Formulario para la creacion de un Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'nombre_paciente',
            'apellido_paciente',
            'fecha_nac_paciente',
            'dni_paciente',
            'perfil'
        ]