from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from layout.forms import NewsletterForm
from . models import Favorite
from babysitter .models import Babysitter


# Create your views here.
def add_favorite(request, slug):
    if request.method == "GET":
        family_id = request.user.family.id
        babysiter_for_favorite = get_object_or_404(Babysitter, slug=slug)
        babysitter_id = babysiter_for_favorite.id
        favorite = Favorite()
        favorite.family_id = family_id
        favorite.babysitter_id = babysitter_id
        favorite.save()
        return redirect('connection:babysitter_profil', slug=slug)


def remove_favorite(request, slug):
    if request.method == "GET":
        family_id = request.user.family.id
        babysiter_for_favorite = get_object_or_404(Babysitter, slug=slug)
        babysitter_id = babysiter_for_favorite.id
        favorite_remove = Favorite.objects.get(
            family_id=family_id, babysitter_id=babysitter_id)
        favorite_remove.delete()
        return redirect('connection:babysitter_profil', slug=slug)


def babysitters(request):
    babysitters = []
    favorites_queryset = Favorite.objects.filter(
        family_id=request.user.family.id)
    all_favorites_list = list(favorites_queryset)
    for favorite in all_favorites_list:
        babysiter = Babysitter.objects.get(id=favorite.babysitter_id)
        babysitters.append(babysiter)

    newsletter_form = NewsletterForm()
    context = {'babysitters': babysitters, 'form': newsletter_form}
    return render(request, 'favorite/babysitters.html', context)
