from django.shortcuts import render
from administracion import models
# Create your views here.

def home(request):
    zonas = models.Zona.objects.all()
    return render(request, 'home.html',{
        'zonas': zonas
    })