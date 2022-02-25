from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Newsletter, ContactMessage
from . forms import NewsletterForm, ContactMessageForm
from reviews .models import Commentary, Rate, Report
from babysitter.models import Babysitter
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _


def home(request):
    # BABYSITTERTS FOR SLIDER (ADD LOGIC IN FUTURE)
    babysitters = Babysitter.objects.all().order_by('-id')[:4]
    number_of_comment_list = []
    rate_list = []
    rate_number_list = []
    if babysitters:
        for babysitter in babysitters:
            number_of_comment = Commentary.objects.filter(
                commentated_person_id=babysitter.user_id).count()
            number_of_comment_list.append(number_of_comment)
            babysitter_rate = Rate.objects.filter(
                rated_person_id=babysitter.user_id).aggregate(Avg('score')).get('score__avg', 0.00)
            rate_list.append(babysitter_rate)
            babysitter_rate_number = Rate.objects.filter(
                rated_person_id=babysitter.user_id).count()
            rate_number_list.append(babysitter_rate_number)
            # Put 3 list in one list for context
        babysitter_list = zip(
            babysitters, number_of_comment_list, rate_list, rate_number_list)
    else:
        babysitter_list = False
    form = NewsletterForm()
    context = {'form': form, 'babysitter_list': babysitter_list}
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
            messages.success(request, _('Hvala, Uspešno ste poslali email!'))
        else:
            messages.error(
                request, _('Vec ste se prijavili ili je email neispravan!'))
        return redirect('layout:home')


def contact_message(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Hvala, Uspešno ste poslali poruku!'))
        return redirect('layout:contact')


def instruction_page(request):
    form = NewsletterForm()
    context = {'form': form}
    return render(request, 'layout/instruction_page.html', context)
