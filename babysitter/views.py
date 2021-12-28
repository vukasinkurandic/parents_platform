from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from layout.forms import NewsletterForm
# from . models import
# from . forms import


def create_profil_babysitter(request):
    newsletter_form = NewsletterForm()
    return render(request, 'babysitter/create_profil_babysitter.html', {'form': newsletter_form})
