from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Newsletter, ContactMessage
from . forms import NewsletterForm, ContactMessageForm


def home(request):
    form = NewsletterForm()
    context = {'form': form}
    return render(request, 'layout/index.html', context)


def contact(request):
    form = ContactMessageForm()
    context = {'form': form}
    return render(request, 'layout/contact.html', context)


def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Hvala, Uspešno ste poslali email!'))
        return redirect('layout:home')


def contact_message(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            print('VALIDNA JEEEEEEEEEEEEEEEEEEE')
            form.save()
            messages.success(request, ('Hvala, Uspešno ste poslali poruku!'))
        return redirect('layout:contact')
