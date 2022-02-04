from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from layout.forms import NewsletterForm
from . forms import FamilyForm, FamilyCalendarForm
from . models import Family, FamilyCalendar
from babysitter . models import Babysitter
from connection . models import Connection
from reviews .models import Commentary, Rate
from django.db.models import Avg


@login_required
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
                    request, "Čestitamo, upravo ste kreirali profil na Parent's time platformi.")
                return redirect('/family/edit_calendar')
            else:
                messages.error(
                    request, 'Proverite format broja telefona ili slike (jpg, png ili jpeg)')
        newsletter_form = NewsletterForm()
        return render(request, 'family/create_profil_family.html', {'form_family': form_family, 'form': newsletter_form})


@login_required
def edit_profil(request):
    user = request.user
    user_id = user.id
    family_obj = get_object_or_404(Family, user_id=user_id)

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
                request, 'Proverite format broja telefona ili slike (jpg, png ili jpeg)')
    newsletter_form = NewsletterForm()
    context = {'form_family': form_family, 'form': newsletter_form}
    return render(request, 'family/edit_profil_family.html', context)


@login_required
def profil(request):
    user = request.user
    user_id = user.id
    profil = get_object_or_404(Family, user_id=user_id)
    calendar = get_object_or_404(FamilyCalendar, family_id=profil.id)

    # LOGIC FOR FIND ALL BABYSITTER WHICH PROFIL SEND MATCH REQUEST (CONNECTION APP)
    all_babysitters_match_queryset = []
    connection_list = []

    # All match for family profile
    all_match_queryset = Connection.objects.filter(family_id=profil.id)
    all_match_list = list(all_match_queryset)
    for one_match in all_match_list:
        connection_list.append(one_match)
        id_babysitter = one_match.babysitter_id
        one_match_babysitter = Babysitter.objects.get(id=id_babysitter)
        all_babysitters_match_queryset.append(one_match_babysitter)

    send_babysitters_list = list(all_babysitters_match_queryset)
    # MAKING ONE LIST FROM SEND_BABYSITTERS LIST AND IS_MATCHED_LIST
    match_list = zip(send_babysitters_list, connection_list)

    # COMMENTARY FOR FAMILY
    comment_list = []
    author_of_commentary_list = []
    comentary_queryset = Commentary.objects.filter(
        commentated_person_id=request.user.id)
    if comentary_queryset.exists():
        for comment in comentary_queryset:
            comment_list.append(comment)
            author_of_commentary = Babysitter.objects.get(
                user_id=comment.author_of_commentary_id)
            author_of_commentary_list.append(author_of_commentary)
        # MAKING ONE LIST FROM COMMENT LIST AND AUTHOR OF COMMENTARY_LIST
        commentary_list = zip(comment_list, author_of_commentary_list)
    else:
        commentary_list = None
    # RATE FOR FAMILY
    rate_average = Rate.objects.filter(
        rated_person_id=request.user.id).aggregate(Avg('score')).get('score__avg', 0.00)

    newsletter_form = NewsletterForm()
    context = {'profil': profil, 'calendar': calendar,
               'form': newsletter_form, 'match_list': match_list,
               'commentary_list': commentary_list, 'rate_average': rate_average}

    return render(request, 'family/profil_family.html', context)


@login_required
def edit_calendar(request):
    user = request.user
    user_id = user.id
    family_obj = get_object_or_404(Family, user_id=user_id)
    family_id = family_obj.id
    family_calendar = get_object_or_404(FamilyCalendar,
                                        family_id=family_id)
    family_calendar_form = FamilyCalendarForm(instance=family_calendar)
    if request.method == 'POST':
        form = FamilyCalendarForm(request.POST, instance=family_calendar)
        if form.is_valid():
            form_family_calendar = form.save(commit=False)
            form_family_calendar.family_id = family_id
            form_family_calendar.save()
            messages.success(
                request, 'Uspesno ste azurirali vreme kada Vam je potrebno čuvanje dece')
            return redirect('/family/profil')
        else:
            messages.error(
                request, 'Proverite format broja telefona ili slike (jpg, png ili jpeg)')

    context = {'family_calendar_form': family_calendar_form}
    return render(request, 'family/edit_calendar.html', context)


def delete_profile(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        messages.success(request, ('Uspešno ste obrisali profil!!!'))
        return redirect('layout:home')
