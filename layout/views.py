from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Newsletter
from . forms import NewsletterForm


def home(request):
    form = NewsletterForm()
    context = {'form': form}
    return render(request, 'layout/index.html', context)


def contact(request):
    form = NewsletterForm()
    context = {'form': form}
    return render(request, 'layout/contact.html', context)


def newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Hvala, Uspešno ste poslali email!'))
        return redirect('layout:home')
