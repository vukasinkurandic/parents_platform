from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from layout.forms import NewsletterForm
from . models import Connection
from babysitter.models import Babysitter, BabysitterCalendar
from family.models import Family, FamilyCalendar
from family.choices import sity_list, work_list, number_list, number_experience_list
from django.db.models import Q
from reviews .models import Commentary, Rate, Report
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def all_babysitters(request):

    family = get_object_or_404(Family, user_id=request.user.id)
    family_city = family.sity

    if request.method == 'GET':
        filter_babysitter = False
        # IF SOME SEESION EXIST
        if 'price_range_min' in request.session and 'price_range_max' in request.session:
            price_range_min = request.session['price_range_min']
            price_range_max = request.session['price_range_max']
            filter_babysitter = Babysitter.objects.filter(
                hourly_rate__gte=price_range_min).filter(hourly_rate__lte=price_range_max)

        if 'city' in request.session:
            city = request.session['city']
            filter_babysitter = filter_babysitter.filter(sity=city)

        if 'age_children' in request.session:
            city = request.session['age_children']
            filter_babysitter = filter_babysitter.filter(
                Q(age_children=age_children) | Q(age_children__contains=age_children))

        if 'work_type' in request.session:
            work_type = request.session['work_type']
            if work_type == 'Bebisiterka i Dadilja':
                filter_babysitter = filter_babysitter

            else:
                filter_babysitter = filter_babysitter.filter(
                    work_type=work_type)

        if 'experience_number' in request.session:
            experience_number = request.session['experience_number']
            filter_babysitter = filter_babysitter.filter(
                years_care_experience=experience_number)

        # ADVANCED FILTER BY SESSION
        if 'children_with_special_needs' in request.session:
            children_with_special_needs = request.session['children_with_special_needs']
            filter_babysitter = filter_babysitter.filter(
                children_with_special_needs='Da')

        if 'home_job' in request.session:
            home_job = request.session['home_job']
            filter_babysitter = filter_babysitter.filter(
                home_job='Da')

        if 'pets' in request.session:
            pets = request.session['pets']
            filter_babysitter = filter_babysitter.filter(
                pets='Ne')

        if 'house' in request.session:
            house = request.session['house']
            filter_babysitter = filter_babysitter.filter(
                house='Da')

        if 'own_children' in request.session:
            own_children = request.session['own_children']
            filter_babysitter = filter_babysitter.filter(
                own_children='Da')

        if 'cooking' in request.session:
            cooking = request.session['cooking']
            filter_babysitter = filter_babysitter.filter(
                cooking='Da')

        if 'sick_child' in request.session:
            sick_child = request.session['sick_child']
            filter_babysitter = filter_babysitter.filter(
                sick_child='Da')

        if 'car' in request.session:
            car = request.session['car']
            filter_babysitter = filter_babysitter.filter(
                car='Da')

        if 'school_activities' in request.session:
            school_activities = request.session['school_activities']
            filter_babysitter = filter_babysitter.filter(
                school_activities='Da')

        if 'travel' in request.session:
            travel = request.session['travel']
            filter_babysitter = filter_babysitter.filter(
                travel='Da')

        # END OF SESSION FILTER
        # If Filters match
        if filter_babysitter:
            babysitters = filter_babysitter
        # If Filters doesnt's match
        else:

            #babysitters = False
            babysitters = Babysitter.objects.filter(sity=family_city)
            if babysitters.exists():
                babysitters = babysitters
            else:
                babysitters = Babysitter.objects.all()

    if request.method == "POST":
        # DELETE ALL FILTER SESSION
        if 'price_range_min' in request.session:
            del request.session['price_range_min']
        if 'price_range_max' in request.session:
            del request.session['price_range_max']
        if 'city' in request.session:
            del request.session['city']
        if 'age_children' in request.session:
            del request.session['age_children']
        if 'work_type' in request.session:
            del request.session['work_type']
        if 'experience_number' in request.session:
            del request.session['experience_number']
        if 'children_with_special_needs' in request.session:
            del request.session['children_with_special_needs']
        if 'home_job' in request.session:
            del request.session['home_job']
        if 'pets' in request.session:
            del request.session['pets']
        if 'cooking' in request.session:
            del request.session['cooking']
        if 'own_children' in request.session:
            del request.session['own_children']
        if 'house' in request.session:
            del request.session['house']
        if 'sick_child' in request.session:
            del request.session['sick_child']
        if 'car' in request.session:
            del request.session['car']
        if 'school_activities' in request.session:
            del request.session['school_activities']
        if 'travel' in request.session:
            del request.session['travel']
        # DELETE ALL FILTER SESSION

        filter_babysitter = False
        # Filters after POST submit
        # BASIC FILTERS
        price_range_min = request.POST['price_range_min']
        request.session['price_range_min'] = price_range_min
        price_range_max = request.POST['price_range_max']
        request.session['price_range_max'] = price_range_max
        if price_range_min != '' or price_range_max != '':
            filter_babysitter = Babysitter.objects.filter(
                hourly_rate__gte=price_range_min).filter(hourly_rate__lte=price_range_max)
        city = request.POST['city']
        if city != '':
            request.session['city'] = city
            filter_babysitter = filter_babysitter.filter(sity=city)
        age_children = request.POST['age_children']
        if age_children != '':
            request.session['age_children'] = age_children
            filter_babysitter = filter_babysitter.filter(
                Q(age_children=age_children) | Q(age_children__contains=age_children))
        work_type = request.POST['work_type']
        if work_type != '':
            request.session['work_type'] = work_type
            # IF 'Bebisiter i Dadilja' don't filter work
            if work_type == 'Bebisiterka i Dadilja':
                filter_babysitter = filter_babysitter
            else:
                filter_babysitter = filter_babysitter.filter(
                    work_type=work_type)
        experience_number = request.POST['experience_number']
        if experience_number != '':
            request.session['experience_number'] = experience_number
            filter_babysitter = filter_babysitter.filter(
                years_care_experience=experience_number)

        # ADVANCED FILTERS
        if "children_with_special_needs" in request.POST:
            children_with_special_needs = request.POST['children_with_special_needs']
            request.session['children_with_special_needs'] = children_with_special_needs
            filter_babysitter = filter_babysitter.filter(
                children_with_special_needs='Da')

        if "home_job" in request.POST:
            home_job = request.POST['home_job']
            request.session['home_job'] = home_job
            filter_babysitter = filter_babysitter.filter(
                home_job='Da')

        if "pets" in request.POST:
            pets = request.POST['pets']
            request.session['pets'] = pets
            filter_babysitter = filter_babysitter.filter(
                pets='Ne')

        if "house" in request.POST:
            house = request.POST['house']
            request.session['house'] = house
            filter_babysitter = filter_babysitter.filter(
                house='Da')

        if "own_children" in request.POST:
            own_children = request.POST['own_children']
            request.session['own_children'] = own_children
            filter_babysitter = filter_babysitter.filter(
                own_children='Da')

        if "cooking" in request.POST:
            cooking = request.POST['cooking']
            request.session['cooking'] = cooking
            filter_babysitter = filter_babysitter.filter(
                cooking='Da')

        if "sick_child" in request.POST:
            sick_child = request.POST['sick_child']
            request.session['sick_child'] = sick_child
            filter_babysitter = filter_babysitter.filter(
                sick_child='Da')

        if "car" in request.POST:
            car = request.POST['car']
            request.session['car'] = car
            filter_babysitter = filter_babysitter.filter(
                car='Da')

        if "school_activities" in request.POST:
            school_activities = request.POST['school_activities']
            request.session['school_activities'] = school_activities
            filter_babysitter = filter_babysitter.filter(
                school_activities='Da')

        if "travel" in request.POST:
            travel = request.POST['travel']
            request.session['travel'] = travel
            filter_babysitter = filter_babysitter.filter(
                travel='Da')

        # If Filters match
        if filter_babysitter:
            babysitters = filter_babysitter
        # If Filters doesnt's match
        else:
            babysitters = False

    # Commentary and Rate number for babysitters
    number_of_comment_list = []
    rate_list = []
    if babysitters:
        for babysitter in babysitters:
            number_of_comment = Commentary.objects.filter(
                commentated_person_id=babysitter.user_id).count()
            number_of_comment_list.append(number_of_comment)
            babysitter_rate = Rate.objects.filter(
                rated_person_id=babysitter.user_id).aggregate(Avg('score')).get('score__avg', 0.00)
            rate_list.append(babysitter_rate)

        paginator = Paginator(babysitters, 2)  # 10 babysitters in page
        page = request.GET.get('page')
        venues = paginator.get_page(page)

    else:
        venues = False

    newsletter_form = NewsletterForm()
    city_list = sity_list
    work_role_list = work_list
    experience_number_list = number_experience_list
    context = {'venues': venues,
               'city_list': city_list, 'work_role_list': work_role_list, 'experience_number_list': experience_number_list, 'form': newsletter_form}
    return render(request, 'connection/all_babysitters.html', context)


@login_required
def babysitter_profil(request, slug):
    # Stop babysitters to see another babysitters
    if request.user.user_type == 2:
        return redirect('babysitter:profil')

    babysitter = get_object_or_404(Babysitter, slug=slug)
    calendar = get_object_or_404(BabysitterCalendar,
                                 babysitter_id=babysitter.id)
    # COMMENTARY FOR BABYSITTER
    comment_list = []
    author_of_commentary_list = []
    comentary_queryset = Commentary.objects.filter(
        commentated_person_id=babysitter.user_id)

    if comentary_queryset.exists():
        for comment in comentary_queryset:
            comment_list.append(comment)

            author_of_commentary = Family.objects.get(
                user_id=comment.author_of_commentary_id)

            author_of_commentary_list.append(author_of_commentary)
        # MAKING ONE LIST FROM COMMENT LIST AND AUTHOR OF COMMENTARY_LIST
        commentary_list = zip(comment_list, author_of_commentary_list)
    else:
        commentary_list = None
    # RATE FOR BABYSITTER
    rate_average = Rate.objects.filter(
        rated_person_id=babysitter.user_id).aggregate(Avg('score')).get('score__avg', 0.00)

    newsletter_form = NewsletterForm()
    context = {'babysitter': babysitter,
               'calendar': calendar, 'form': newsletter_form,
               'commentary_list': commentary_list, 'rate_average': rate_average}
    return render(request, 'connection/babysitter_profil.html', context)


@login_required
def send_match(request):
    if request.method == "POST":
        babysitter_slug = request.POST['babysitter_slug']
        babysiter_for_match = Babysitter.objects.get(slug=babysitter_slug)
        family_id = request.user.family.id
        babysitter_id = babysiter_for_match.id
        connection = Connection()
        connection.family_id = family_id
        connection.babysitter_id = babysitter_id
        connection.is_matched = None

        all_connection = Connection.objects.filter(
            family_id=family_id, babysitter_id=babysitter_id)
        if all_connection.exists():
            for connection in all_connection:
                if connection.is_matched == False:
                    connection.is_matched = None
                    connection.save()
                    messages.success(
                        request, (f'Ponovo ste ste rezervisali {babysiter_for_match.work_type} {babysiter_for_match.first_name} {babysiter_for_match.last_name}'))
                else:
                    messages.success(
                        request, (f'Već ste rezervisali {babysiter_for_match.work_type} {babysiter_for_match.first_name} {babysiter_for_match.last_name}'))
        else:
            connection.save()
            messages.success(
                request, (f'Uspešno ste rezervisali {babysiter_for_match.work_type} {babysiter_for_match.first_name} {babysiter_for_match.last_name}'))
    return redirect('family:profil')


@login_required
def matched_babysitter_profil(request, slug):
    # Stop babysitters to see another babysitters
    if request.user.user_type == 2:
        return redirect('babysitter:profil')
    babysitter = get_object_or_404(Babysitter, slug=slug)
    calendar = get_object_or_404(BabysitterCalendar,
                                 babysitter_id=babysitter.id)

    connection_queryset = Connection.objects.filter(
        family_id=request.user.family.id, babysitter_id=babysitter.id)
    # Stop URL connection if is mached is FALSE or Connection doesn't exists
    if connection_queryset.exists():
        if connection_queryset[0].is_matched == False:
            return redirect('family:profil')
        else:
            # COMMENTARY FOR BABYSITTER
            comment_list = []
            author_of_commentary_list = []
            comentary_queryset = Commentary.objects.filter(
                commentated_person_id=babysitter.user_id)

            if comentary_queryset.exists():
                for comment in comentary_queryset:
                    comment_list.append(comment)

                    author_of_commentary = Family.objects.get(
                        user_id=comment.author_of_commentary_id)

                    author_of_commentary_list.append(author_of_commentary)
                # MAKING ONE LIST FROM COMMENT LIST AND AUTHOR OF COMMENTARY_LIST
                commentary_list = zip(comment_list, author_of_commentary_list)
            else:
                commentary_list = None
            # RATE FOR BABYSITTER
            rate_average = Rate.objects.filter(
                rated_person_id=babysitter.user_id).aggregate(Avg('score')).get('score__avg', 0.00)

            # COMENNTARY, RATE and REPORT FORM
            author_id = request.user.id
            person_id = babysitter.user_id
            commentary_model = Commentary()
            rate_model = Rate()
            report_model = Report()
            if request.method == "POST":
                # Commentary section
                if 'commentary_submit' in request.POST:
                    commentary = request.POST['comment_area']
                    try:
                        commentary_model = Commentary.objects.get(
                            author_of_commentary_id=author_id, commentated_person_id=person_id)
                        commentary_model.commentary_body = commentary
                        commentary_model.published = True
                        commentary_model.save()
                        messages.success(
                            request, ('Uspešno ste ostavili komentar!'))
                    except Commentary.DoesNotExist:
                        commentary_model = Commentary.objects.create(
                            author_of_commentary_id=author_id,
                            commentated_person_id=person_id,
                            commentary_body=commentary,
                            published=True
                        )
                        messages.success(
                            request, ('Uspešno ste ostavili komentar!'))
                # Rate section
                if 'rate_submit' in request.POST and request.POST.get('rate'):
                    score = request.POST['rate']
                    try:
                        rate_model = Rate.objects.get(
                            author_of_rate_id=author_id, rated_person_id=person_id)
                        rate_model.score = score
                        rate_model.save()
                        messages.success(
                            request, ('Uspešno ste ocenili korisnika!'))
                    except Rate.DoesNotExist:
                        rate_model = Rate.objects.create(
                            author_of_rate_id=author_id,
                            rated_person_id=person_id,
                            score=score
                        )
                        messages.success(
                            request, ('Uspešno ste ocenili korisnika!'))
                elif 'rate_submit' in request.POST:
                    messages.error(
                        request, ('Morate izabrati željenu ocenu!'))
                # Report section
                if 'report_submit' in request.POST:
                    report = request.POST['user_report']
                    try:
                        report_model = Report.objects.get(
                            author_of_report_id=author_id, reported_person_id=person_id)
                        report_model.report_body = report
                        report_model.save()
                        messages.success(
                            request, ('Uspešno ste prijavili korisnika!'))
                    except Report.DoesNotExist:
                        report_model = Report.objects.create(
                            author_of_report_id=author_id,
                            reported_person_id=person_id,
                            report_body=report
                        )
                        messages.success(
                            request, ('Uspešno ste prijavili korisnika!'))

            # END OF COMENNTARY, RATE and REPORT

            newsletter_form = NewsletterForm()
            context = {'babysitter': babysitter,
                       'calendar': calendar, 'form': newsletter_form,
                       'commentary_list': commentary_list, 'rate_average': rate_average}
            return render(request, 'connection/matched_babysitter_profil.html', context)
    else:
        return redirect('family:profil')


@login_required
def family_profil(request, slug):
    # Stop family to see another family
    if request.user.user_type == 1:
        return redirect('family:profil')

    profil = get_object_or_404(Family, slug=slug)
    calendar = get_object_or_404(FamilyCalendar,
                                 family_id=profil.id)
    babysitter_id = request.user.babysitter.id
    # Connection for context
    connection_list = []
    all_connection_queryset = Connection.objects.filter(
        family_id=profil.id, babysitter_id=babysitter_id)

    # STOP SEE FAMILY PROFILE FROM URL WITHOUT MATCHED REQUEST
    if all_connection_queryset.exists():
        True
    else:
        return redirect('layout:home')
    # STOP SEE FAMILY PROFILE FROM URL WITHOUT MATCHED REQUEST

    for connection in all_connection_queryset:
        connection_list.append(connection)

    # COMMENTARY FOR FAMILY
    comment_list = []
    author_of_commentary_list = []
    comentary_queryset = Commentary.objects.filter(
        commentated_person_id=profil.user_id)

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
        rated_person_id=profil.user_id).aggregate(Avg('score')).get('score__avg', 0.00)

    newsletter_form = NewsletterForm()
    context = {'profil': profil, 'connection_list': connection_list,
               'calendar': calendar, 'form': newsletter_form,
               'commentary_list': commentary_list, 'rate_average': rate_average}
    return render(request, 'connection/family_profil.html', context)


@login_required
def matched_family_profil(request, slug):
    # Stop family to see another family
    if request.user.user_type == 1:
        return redirect('family:profil')
    babysitter_id = request.user.babysitter.id
    profil = get_object_or_404(Family, slug=slug)
    calendar = get_object_or_404(FamilyCalendar,
                                 family_id=profil.id)

    connection_queryset = Connection.objects.filter(
        family_id=profil.id, babysitter_id=babysitter_id)
    # Stop URL connection if is mached is FALSE or Connection doesn't exists
    if connection_queryset.exists():
        if connection_queryset[0].is_matched == False:
            return redirect('babysitter:profil')
        else:
            # COMMENTARY FOR FAMILY
            comment_list = []
            author_of_commentary_list = []
            comentary_queryset = Commentary.objects.filter(
                commentated_person_id=profil.user_id)

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
                rated_person_id=profil.user_id).aggregate(Avg('score')).get('score__avg', 0.00)
            # Change is matched in TRUE
            for connection in connection_queryset:
                connection.is_matched = True
                connection.save()
            # COMENNTARY, RATE and REPORT
            author_id = request.user.id
            person_id = profil.user_id
            commentary_model = Commentary()
            rate_model = Rate()
            report_model = Report()
            if request.method == "POST":
                # Commentary section
                if 'commentary_submit' in request.POST:
                    commentary = request.POST['comment_area']
                    try:
                        commentary_model = Commentary.objects.get(
                            author_of_commentary_id=author_id, commentated_person_id=person_id)
                        commentary_model.commentary_body = commentary
                        commentary_model.published = True
                        commentary_model.save()
                        messages.success(
                            request, ('Uspešno ste ostavili komentar!'))
                    except Commentary.DoesNotExist:
                        commentary_model = Commentary.objects.create(
                            author_of_commentary_id=author_id,
                            commentated_person_id=person_id,
                            commentary_body=commentary,
                            published=True
                        )
                        messages.success(
                            request, ('Uspešno ste ostavili komentar!'))
                # Rate section
                if 'rate_submit' in request.POST and request.POST.get('rate'):
                    score = request.POST['rate']
                    try:
                        rate_model = Rate.objects.get(
                            author_of_rate_id=author_id, rated_person_id=person_id)
                        rate_model.score = score
                        rate_model.save()
                        messages.success(
                            request, ('Uspešno ste ocenili korisnika!'))
                    except Rate.DoesNotExist:
                        rate_model = Rate.objects.create(
                            author_of_rate_id=author_id,
                            rated_person_id=person_id,
                            score=score
                        )
                        messages.success(
                            request, ('Uspešno ste ocenili korisnika!'))
                elif 'rate_submit' in request.POST:
                    messages.error(
                        request, ('Morate izabrati željenu ocenu!'))
                # Report section
                if 'report_submit' in request.POST:
                    report = request.POST['user_report']
                    try:
                        report_model = Report.objects.get(
                            author_of_report_id=author_id, reported_person_id=person_id)
                        report_model.report_body = report
                        report_model.save()
                        messages.success(
                            request, ('Uspešno ste prijavili korisnika!'))
                    except Report.DoesNotExist:
                        report_model = Report.objects.create(
                            author_of_report_id=author_id,
                            reported_person_id=person_id,
                            report_body=report
                        )
                        messages.success(
                            request, ('Uspešno ste prijavili korisnika!'))

            # END OF COMENNTARY, RATE and REPORT

            newsletter_form = NewsletterForm()
            context = {'profil': profil,
                       'calendar': calendar, 'form': newsletter_form,
                       'commentary_list': commentary_list, 'rate_average': rate_average}
            return render(request, 'connection/matched_family_profil.html', context)
    else:
        return redirect('babysitter:profil')


@login_required
def deny_connection(request):
    if request.method == "POST":
        connection_id = request.POST['connection_id']
        connection = Connection.objects.get(id=connection_id)
        connection.is_matched = False
        connection.save()
        messages.success(
            request, ('Uspešno ste odbili zahtev!'))
        context = {'connection': connection}
        return redirect('babysitter:profil')


@login_required
def delete_connection(request):
    if request.method == "POST":
        connection_id = request.POST['connection_id']
        connection = Connection.objects.get(id=connection_id)
        connection.delete()
        messages.success(
            request, ('Uspešno ste obrisali zahtev!'))
        context = {'connection': connection}
        return redirect('family:profil')
