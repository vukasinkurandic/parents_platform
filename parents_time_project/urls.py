from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . forms import UserPasswordResetForm
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = []

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('layout.urls', namespace='layout')),
    path('', include('account.urls', namespace='account')),
    path('family/', include('family.urls', namespace='family')),
    path('babysitter/', include('babysitter.urls', namespace='babysitter')),
    path('connection/', include('connection.urls', namespace='connection')),
    path('reviews/', include('reviews.urls', namespace='reviews')),

    path('rosetta/', include('rosetta.urls')),


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
         name="password_reset_complete"),
    prefix_default_language=False

)
handler400 = 'error_handlers.views.custom_bad_request_view'
handler403 = 'error_handlers.views.custom_permission_denied_view'
handler404 = 'error_handlers.views.custom_page_not_found_view'
handler500 = 'error_handlers.views.custom_error_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
