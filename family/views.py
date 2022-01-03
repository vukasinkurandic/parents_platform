from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from layout.forms import NewsletterForm
from . forms import FamilyForm, FamilyCalendarForm
from . models import Family, FamilyCalendar


def create_profil(request):
    form_family = FamilyForm()
    user = request.user
    user_id = user.id

    try:
        family_obj = Family.objects.get(user_id=user_id)
    except Family.DoesNotExist:
        family_obj = None
    if family_obj:  # PROFIL EXIST

        return redirect('/family/profil')
    else:  # PROFIL NOT EXIST
        if request.method == "POST":
            form_family = FamilyForm(request.POST, request.FILES)
            if form_family.is_valid():
                family = form_family.save(commit=False)
                family.is_form_submit = True
                family.user_id = user.id
                family.save()
                messages.success(
                    request, 'Uspesno ste kreirali profil')
                return redirect('/family/edit_calendar')
            else:
                messages.error(
                    request, 'Slika ne sme biti vec od 2MB i mora biti u formatu jpg, png ili jpeg')
        newsletter_form = NewsletterForm()
        return render(request, 'family/create_profil_family.html', {'form_family': form_family, 'form': newsletter_form})


def edit_profil(request):
    user = request.user
    user_id = user.id
    family_obj = Family.objects.get(user_id=user_id)

    form_family = FamilyForm(instance=family_obj)
    if request.method == 'POST':
        form = FamilyForm(request.POST, request.FILES,  instance=family_obj)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Uspesno ste azurirali profil')
            return redirect('/family/profil')
        else:
            messages.error(
                request, 'Slika ne sme biti vec od 2MB i mora biti u formatu jpg, png ili jpeg')
    newsletter_form = NewsletterForm()
    context = {'form_family': form_family, 'form': newsletter_form}
    return render(request, 'family/edit_profil_family.html', context)


def profil(request):
    user = request.user
    user_id = user.id
    profil = Family.objects.get(user_id=user_id)
    calendar = FamilyCalendar.objects.get(family_id=profil.id)
    newsletter_form = NewsletterForm()
    context = {'profil': profil, 'calendar': calendar, 'form': newsletter_form}
    # return render(request, 'family/profil_family_proba.html', context) PROBA STRANICA
    return render(request, 'family/profil_family.html', context)


def edit_calendar(request):
    user = request.user
    user_id = user.id
    family_obj = Family.objects.get(user_id=user_id)
    family_id = family_obj.id
    family_calendar = FamilyCalendar.objects.get(family_id=family_id)
    family_calendar_form = FamilyCalendarForm(instance=family_calendar)
    if request.method == 'POST':
        form = FamilyCalendarForm(request.POST, instance=family_calendar)
        if form.is_valid():
            form_family_calendar = form.save(commit=False)
            form_family_calendar.family_id = family_id
            form_family_calendar.save()
            messages.success(
                request, 'Uspesno ste azurirali Vasu dostupnost')
            return redirect('/family/profil')
        else:
            messages.error(
                request, 'Slika ne sme biti vec od 2MB i mora biti u formatu jpg, png ili jpeg')

    context = {'family_calendar_form': family_calendar_form}
    return render(request, 'family/edit_calendar.html', context)
