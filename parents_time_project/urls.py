from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . forms import UserPasswordResetForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('layout.urls', namespace='layout')),
    path('', include('account.urls', namespace='account')),
    path('family/', include('family.urls', namespace='family')),
    path('babysitter/', include('babysitter.urls', namespace='babysitter')),

    ### Views za resetovanje lozinke ###
    path("password-reset", auth_views.PasswordResetView.as_view(
         template_name='password_reset.html',
         html_email_template_name='password_reset_email.html', form_class=UserPasswordResetForm
         ), name="password_reset"),
    path("password-reset/done/",
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name="password_reset_complete")

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
