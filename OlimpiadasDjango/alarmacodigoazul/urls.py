from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Pagina de admin
    path('', include('main.urls')),  # Importa los links de main
    path('', include('autenticacion.urls')), # Importa los links de autentication
     path('', include('administracion.urls')) # Importa los links de administracion
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)