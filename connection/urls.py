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
    # Matched Babysitter
    path('matched_babysitter_profil/<str:slug>/',
         views.matched_babysitter_profil, name='matched_babysitter_profil'),
    # Matched Family
    path('family_profil/<str:slug>/', views.family_profil,
         name='family_profil'),
    path('matched_family_profil/<str:slug>/', views.matched_family_profil,
         name='matched_family_profil'),
    #  Deny connection
    path('deny_connection', views.deny_connection,
         name='deny_connection'),
    # Delete connection
    path('delete_connection', views.delete_connection,
         name='delete_connection'),


]
