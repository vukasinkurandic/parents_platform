from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from layout.forms import NewsletterForm
from babysitter.models import Babysitter, BabysitterCalendar
from family.models import Family, FamilyCalendar
from family.choices import sity_list


@login_required
def all_babysitters(request):
    family = get_object_or_404(Family, user_id=request.user.id)
    family_city = family.sity
    babysitters = Babysitter.objects.filter(sity=family_city)

    # Babysitter with same city like family
    if babysitters.exists():
        babysitters = babysitters
    else:
        # Random Babysitter if same city is not exists. MEMBERSHIP GOLD OR A FEW FIRST
        babysitters = Babysitter.objects.all()

    if request.method == "POST":
        filter_babysitter = False
        # Filters after POST submit
        price_range_min = request.POST['price_range_min']
        price_range_max = request.POST['price_range_max']
        if price_range_min != '' or price_range_max != '':
            filter_babysitter = Babysitter.objects.filter(
                hourly_rate__gte=price_range_min).filter(hourly_rate__lte=price_range_max)
        city = request.POST['city']
        if city != '':
            filter_babysitter = Babysitter.objects.filter(sity=city)
        age_children = request.POST['age_children']
        if age_children != '':
            filter_babysitter = Babysitter.objects.filter(
                age_children=age_children)
        work_type = request.POST['work_type']
        if work_type != '':
            filter_babysitter = Babysitter.objects.filter(
                work_type=work_type)
        # If Filters match
        if filter_babysitter:
            babysitters = filter_babysitter
        # If Filters doesnt's match
        else:
            babysitters = False

    newsletter_form = NewsletterForm()
    city_list = sity_list
    context = {'babysitters': babysitters,
               'city_list': city_list, 'form': newsletter_form}
    return render(request, 'connection/all_babysitters.html', context)


@login_required
def babysitter_profil(request, slug):
    babysitter = get_object_or_404(Babysitter, slug=slug)
    calendar = get_object_or_404(BabysitterCalendar,
                                 babysitter_id=babysitter.id)

    newsletter_form = NewsletterForm()
    context = {'babysitter': babysitter,
               'calendar': calendar,
               'form': newsletter_form}
    return render(request, 'connection/babysitter_profil.html', context)
