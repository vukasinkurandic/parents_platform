from django.contrib import messages
from django.shortcuts import render, redirect
# from . models import
# from . forms import


def create_profil_family(request):
    return render(request, 'family/create_profil_family.html')
