# Generated by Django 4.2.5 on 2023-09-25 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='alergias',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='altura_paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='consulta',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='domicilio_paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='email_paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='factor_rh',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='genero_paciente',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='grupo_sanguineo',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='peso_paciente_kg',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='telefono_paciente',
        ),
    ]
