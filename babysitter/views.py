from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from layout.forms import NewsletterForm
from . forms import BabysitterForm, BabysitterCalendarForm
from . models import Babysitter, BabysitterCalendar
from connection . models import Connection
from family . models import Family
from reviews .models import Commentary, Rate
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _


@login_required
def create_profil(request):
    form_babysitter = BabysitterForm()
    user = request.user
    user_id = user.id
    try:
        babysitter_obj = Babysitter.objects.get(user_id=user_id)
    except Babysitter.DoesNotExist:
        babysitter_obj = None
    if babysitter_obj:  # PROFIL EXIST
        return redirect('babysitter:profil')
    else:  # PROFIL NOT EXIST
        if request.method == "POST":
            form_babysitter = BabysitterForm(request.POST, request.FILES)
            if form_babysitter.is_valid():
                babysitter = form_babysitter.save(commit=False)
                babysitter.is_form_submit = True
                babysitter.user_id = user.id
                babysitter.save()
                messages.success(
                    request, _("Čestitamo, upravo ste kreirali profil na Parent's time platformi."))
                return redirect('babysitter:edit_calendar')
            else:
                messages.error(
                    request, _('Proverite raspone cene, format broja telefona, društvene mreže ili slike (jpg, png ili jpeg)'))
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
                request, _('Uspesno ste azurirali profil'))
            return redirect('babysitter:profil')
        else:
            messages.error(
                request, _('Proverite raspone cene, format broja telefona, društvene mreže ili slike (jpg, png ili jpeg)'))
    newsletter_form = NewsletterForm()
    context = {'form_babysitter': form_babysitter, 'form': newsletter_form}
    return render(request, 'babysitter/edit_profil_babysitter.html', context)


@login_required
def profil(request):
    user = request.user
    user_id = user.id
    profil = get_object_or_404(Babysitter, user_id=user_id)
    calendar = get_object_or_404(BabysitterCalendar, babysitter_id=profil.id)

    # LOGIC FOR FIND ALL FAMILY WHICH PROFIL SEND MATCH REQUEST (CONNECTION APP)
    all_families_match_queryset = []
    connection_list = []
    # All match for babysitter profile
    all_match_connections_queryset = Connection.objects.filter(
        babysitter_id=profil.id)
    all_match_connections_list = list(all_match_connections_queryset)

    for one_match in all_match_connections_list:
        # Append every singe connection to list
        connection_list.append(one_match)

        id_family = one_match.family_id
        one_match_family = Family.objects.get(id=id_family)
        # Append every singe family to list MOZDA MOZE JEDAN KORAK MANJE
        all_families_match_queryset.append(one_match_family)

    send_family_list = list(all_families_match_queryset)

    # Put to send_family_list and connection_list in one and send in context
    send_list = zip(send_family_list, connection_list)

    # COMMENTARY FOR BABYSITTER
    comment_list = []
    author_of_commentary_list = []
    comentary_queryset = Commentary.objects.filter(
        commentated_person_id=request.user.id)
    if comentary_queryset.exists():
        for comment in comentary_queryset:
            comment_list.append(comment)
            author_of_commentary = Family.objects.get(
                user_id=comment.author_of_commentary_id)
            author_of_commentary_list.append(author_of_commentary)
        # MAKING ONE LIST FROM COMMENT LIST AND AUTHOR OF COMMENTARY
        commentary_list = zip(comment_list, author_of_commentary_list)
    else:
        commentary_list = None
    # RATE FOR BABYSITTER
    rate_average = Rate.objects.filter(
        rated_person_id=request.user.id).aggregate(Avg('score')).get('score__avg', 0.00)

    newsletter_form = NewsletterForm()
    context = {'profil': profil, 'calendar': calendar,
               'form': newsletter_form, 'send_list': send_list,
               'commentary_list': commentary_list, 'rate_average': rate_average}
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
                request, _('Uspesno ste azurirali vreme kada možete da čuvate decu'))
            return redirect('babysitter:profil')
        else:
            messages.error(
                request, _('Proverite raspone cene, format broja telefona, društvene mreže ili slike (jpg, png ili jpeg)'))

    context = {'babysitter_calendar_form': babysitter_calendar_form}
    return render(request, 'babysitter/edit_calendar.html', context)


def delete_profile(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, _('Uspešno ste obrisali profil!!!'))
        return redirect('layout:home')
