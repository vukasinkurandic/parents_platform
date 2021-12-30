from django.urls import path
from . import views

app_name = 'family'

urlpatterns = [
    # Family profil
    path('create_profil', views.create_profil,
         name='create_profil'),
    path('edit_profil', views.edit_profil,
         name='edit_profil'),
    path('profil', views.profil,
         name='profil'),
    # Calendar
    path('edit_calendar', views.edit_calendar,
         name='edit_calendar'),





]
