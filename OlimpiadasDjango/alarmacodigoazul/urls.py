from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls), # Pagina de admin
    path('', include('main.urls')),  # Importa los links de main
    path('', include('autenticacion.urls')), # Importa los links de autentication
     path('', include('administracion.urls')) # Importa los links de administracion
]
