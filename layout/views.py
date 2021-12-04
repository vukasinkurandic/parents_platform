from django.shortcuts import render, redirect


def home(request):
    return render(request, 'layout/index.html')


def contact(request):
    return render(request, 'layout/contact.html')
