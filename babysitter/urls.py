from django.urls import path
from . import views

app_name = 'babysitter'

urlpatterns = [
    path('create_profil_babysitter',
         views.create_profil_babysitter, name='create_profil_babysitter'),





]
