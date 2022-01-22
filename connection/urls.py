from django.urls import path
from . import views

app_name = 'connection'

urlpatterns = [
    # ALL Babysitters profiles
    path('all_babysitters',
         views.all_babysitters, name='all_babysitters'),
    path('babysitter_profil/<str:slug>/',
         views.babysitter_profil, name='babysitter_profil'),
    path('send_match',
         views.send_match, name='send_match'),
    path('matched_babysitter_profil/<str:slug>/',
         views.matched_babysitter_profil, name='matched_babysitter_profil'),

    
]
