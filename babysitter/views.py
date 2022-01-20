from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from layout.forms import NewsletterForm
from . forms import BabysitterForm, BabysitterCalendarForm
from . models import Babysitter, BabysitterCalendar


@login_required
def create_profil(request):
    form_babysitter = BabysitterForm()
    user = request.user
    user_id = user.id
    try:
        babysitter_obj = get_object_or_404(Babysitter, user_id=user_id)
    except Babysitter.DoesNotExist:
        babysitter_obj = None
    if babysitter_obj:  # PROFIL EXIST
        return redirect('/babysitter/profil')
    else:  # PROFIL NOT EXIST
        if request.method == "POST":
            form_babysitter = BabysitterForm(request.POST, request.FILES)
            if form_babysitter.is_valid():
                babysitter = form_babysitter.save(commit=False)
                babysitter.is_form_submit = True
                babysitter.user_id = user.id
                babysitter.save()
                messages.success(
                    request, 'Uspesno ste kreirali profil')
                return redirect('/babysitter/edit_calendar')
            else:
                messages.error(
                    request, 'Proverite formu unetih podataka')
        newsletter_form = NewsletterForm()
        context = {'form_babysitter': form_babysitter, 'form': newsletter_form}
        return render(request, 'babysitter/create_profil_babysitter.html', context)


@login_required
def edit_profil(request):
    user = request.user
    user_id = user.id
    babysitter_obj = get_object_or_404(Babysitter, user_id=user_id)

    form_babysitter = BabysitterForm(instance=babysitter_obj)
    if request.method == 'POST':
        form = BabysitterForm(
            request.POST, request.FILES,  instance=babysitter_obj)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Uspesno ste azurirali profil')
            return redirect('/babysitter/profil')
        else:
            messages.error(
                request, 'Proverite formu unetih podataka')
    newsletter_form = NewsletterForm()
    context = {'form_babysitter': form_babysitter, 'form': newsletter_form}
    return render(request, 'babysitter/edit_profil_babysitter.html', context)


@login_required
def profil(request):
    user = request.user
    user_id = user.id
    profil = get_object_or_404(Babysitter, user_id=user_id)
    calendar = get_object_or_404(BabysitterCalendar, babysitter_id=profil.id)
    newsletter_form = NewsletterForm()
    context = {'profil': profil, 'calendar': calendar, 'form': newsletter_form}
    # PROBA STRANICA
    # return render(request, 'babysitter/profil_babysitter_proba.html', context)
    return render(request, 'babysitter/profil_babysitter.html', context)


@login_required
def edit_calendar(request):
    user = request.user
    user_id = user.id
    babysitter_obj = get_object_or_404(
        Babysitter, user_id=user_id)
    babysitter_id = babysitter_obj.id
    babysitter_calendar = get_object_or_404(BabysitterCalendar,
                                            babysitter_id=babysitter_id)
    babysitter_calendar_form = BabysitterCalendarForm(
        instance=babysitter_calendar)
    if request.method == 'POST':
        form = BabysitterCalendarForm(
            request.POST, instance=babysitter_calendar)
        if form.is_valid():
            form_babysitter_calendar = form.save(commit=False)
            form_babysitter_calendar.babysitter_id = babysitter_id
            form_babysitter_calendar.save()
            messages.success(
                request, 'Uspesno ste azurirali Vasu dostupnost')
            return redirect('/babysitter/profil')
        else:
            messages.error(
                request, 'Proverite formu unetih podataka')

    context = {'babysitter_calendar_form': babysitter_calendar_form}
    return render(request, 'babysitter/edit_calendar.html', context)
