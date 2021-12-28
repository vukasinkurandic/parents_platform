from django.contrib import messages
from django.shortcuts import render, redirect
from layout.forms import NewsletterForm
from . forms import FamilyForm
from . models import Family
from account .models import CustomUser


def create_profil_family(request):
    form_family = FamilyForm()
    user = request.user
    if request.method == "POST":
        form_family = FamilyForm(request.POST, request.FILES)
        if form_family.is_valid():
            family = form_family.save(commit=False)
            print('EVOJEEEEEEEEEEOOOOOOOOOOOOOOOOO')
            family.is_form_submit = True
            family.user_id = user.id
            family.save()
            messages.success = 'Bravo VUKASINE'
        else:
            messages.error = 'Pusi ga VUKASINE'
        return redirect('/')
    newsletter_form = NewsletterForm()
    return render(request, 'family/create_profil_family.html', {'form_family': form_family, 'form': newsletter_form})
