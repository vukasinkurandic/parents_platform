from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserAdminCreationForm
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .models import CustomUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import auth
from layout.forms import NewsletterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language


def register_family(request):
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            user = form.save()
            user.user_type = 1
            token = str(uuid.uuid4())
            user.auth_token = token
            user.is_terms_confirmed = form.cleaned_data.get(
                'is_terms_confirmed')
            user.save()
           # messages.success(request, ('Uspešno ste se registrovali!'))
            send_mail_after_registration(email, token)
            return redirect('account:token_send')
    else:
        form = UserAdminCreationForm()
    return render(request, 'account/register_family.html', {'form': form})


def register_babysitter(request):
    if request.method == 'POST':
        form = UserAdminCreationForm(request.POST)
        email = request.POST.get('email')
        if form.is_valid():
            user = form.save()
            user.user_type = 2
            token = str(uuid.uuid4())
            user.auth_token = token
            user.is_terms_confirmed = form.cleaned_data.get(
                'is_terms_confirmed')
            user.save()
            send_mail_after_registration(email, token)
            return redirect('account:token_send')

    else:
        form = UserAdminCreationForm()
    return render(request, 'account/register_babysitter.html', {'form': form})


def success(request):
    return render(request, 'account/success.html')


def token_send(request):
    return render(request, 'account/token_send.html')


def verify(request, auth_token):
    try:
        profile_obj = CustomUser.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_email_verified:
                messages.success(request, _('Vaš email je već verifikovan.'))
                return render(request, 'account/already_verified.html')
            profile_obj.is_email_verified = True
            profile_obj.save()
            messages.success(request, _('Uspešno ste se registrovali!'))
            return render(request, 'account/success.html')
        else:
            return redirect('account:error')
    except Exception as e:
        print(e)
        return redirect('account:login')


def error_page(request):
    return render(request, 'account/error.html')


def send_mail_after_registration(email, token):
    subject = _('Vaš nalog mora biti verifikovan')
    language = get_language()
    if language == 'sr':
        message = f'https://parentstime.rs/verify/{token}'
    else:
        message = f'https://parentstime.rs/en/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    html_content = render_to_string(
        "email_verified.html", {'title': subject, 'content': message})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject, text_content, email_from, recipient_list)
    email.attach_alternative(html_content, 'text/html')
    email.send()
    #send_mail(subject, message, email_from, recipient_list)
    # Odraditi try block ako ne ode email


def login(request):
    if request.user.is_authenticated:
        return redirect('account:logout')
    form = NewsletterForm()
    if request.method == 'POST':
        email = request.POST['email_login']
        password = request.POST['password_login']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            if user.is_email_verified:
                if user.user_type == 1:
                    # messages.success(
                    # request, 'You are logged in successfully like FAMILY!')
                    return redirect('family:create_profil')
                elif user.user_type == 2:
                    # messages.success(
                    # request, 'You are logged in successfully like Babysitter!')
                    return redirect('babysitter:create_profil')
            else:
                token = str(uuid.uuid4())
                user.auth_token = token
                user.save()
                send_mail_after_registration(email, token)
                return redirect('account:token_send')
        else:
            messages.error(request, _('Nepostojeći email ili netačna lozinka'))
            return redirect('account:login')
    else:
        return render(request, 'account/login.html', {'form': form})
