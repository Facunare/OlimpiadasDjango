from django.urls import path, include
from . import views

from django.views.generic import TemplateView
urlpatterns = [

    path('signup/', views.signup, name='signup'), # URL para vista SignUp
    path('signout/', views.signout, name='logout'), # URL para vista SignOut
    path('signin/', views.signin, name='signin'), # URL para vista SignIn
]