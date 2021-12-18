from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserAdminCreationForm
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .models import CustomUser


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
            messages.success(request, ('Uspešno ste se registrovali!'))
            send_mail_after_registration(email, token)
            return redirect('/token')
    else:
        form = UserAdminCreationForm()
    return render(request, 'account/register.html', {'form': form})


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
            messages.success(request, ('Uspešno ste se registrovali!'))
            send_mail_after_registration(email, token)
            return redirect('/token')

    else:
        form = UserAdminCreationForm()
    return render(request, 'account/register.html', {'form': form})


def success(request):
    return render(request, 'account/success.html')


def token_send(request):
    return render(request, 'account/token_send.html')


def verify(request, auth_token):
    try:
        profile_obj = CustomUser.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_email_verified:
                messages.success(request, 'Your account is already verified.')
                return HttpResponse("Your is already verified")
            profile_obj.is_email_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return HttpResponse("Your account has been verified")
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')


def error_page(request):
    return render(request, 'account/error.html')


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
