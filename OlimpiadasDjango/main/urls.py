
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="main"), # URL Pagina principal
    path('home', views.zonas, name="home") 
]
