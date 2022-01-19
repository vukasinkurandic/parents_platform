from django.urls import path
from . import views

app_name = 'connection'

urlpatterns = [
    # ALL Babysitters profiles
    path('all_babysitters',
         views.all_babysitters, name='all_babysitters'),


]
