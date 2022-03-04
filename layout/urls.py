from django.urls import path
from . import views

app_name = 'layout'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('contact_message', views.contact_message, name='contact_message'),
    path('instruction', views.instruction_page, name='instruction_page'),




]
