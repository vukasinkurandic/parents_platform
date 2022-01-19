from django.shortcuts import render
from layout.forms import NewsletterForm


def all_babysitters(request):
    newsletter_form = NewsletterForm()
    podatak = "Sve Bebisiterke su ovde"
    context = {'podatak': podatak, 'form': newsletter_form}
    return render(request, 'connection/all_babysitters.html', context)
