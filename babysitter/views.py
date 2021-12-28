from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
# from . models import
# from . forms import


def create_profil_babysitter(request):
    return render(request, 'babysitter/create_profil_babysitter.html')
