from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [

    path('register_family/', views.register_family, name='register_family'),
    path('register_babysitter/', views.register_babysitter,
         name='register_babysitter'),
    path('token/', views.token_send, name="token_send"),
    path('success/', views.success, name='success'),
    path('verify/<auth_token>', views.verify, name="verify"),
    path('error/', views.error_page, name="error"),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),

]
