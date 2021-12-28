from django.urls import path
from . import views

app_name = 'family'

urlpatterns = [
    path('create_profil_family', views.create_profil, name='create_profil'),





]
