from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('test-template', views.test,name='test_template'),
    
]

