from django.urls import path
from . import views

app_name = 'babysitter'

urlpatterns = [
    # Babysitter profil
    path('create_profil',
         views.create_profil, name='create_profil'),
    path('edit_profil', views.edit_profil,
         name='edit_profil'),
    path('profil', views.profil,
         name='profil'),
    path('delete_profile', views.delete_profile,
         name='delete_profile'),

    # Calendar
    path('edit_calendar', views.edit_calendar,
         name='edit_calendar'),

]
