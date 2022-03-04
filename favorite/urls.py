from django.urls import path
from . import views

app_name = 'favorite'

urlpatterns = [
    path('babysitters', views.babysitters, name='babysitters'),
    path('add_favorite/<str:slug>/', views.add_favorite, name='add_favorite'),
    path('remove_favorite/<str:slug>/',
         views.remove_favorite, name='remove_favorite'),

]
