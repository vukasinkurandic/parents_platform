from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect, reverse
from layout.forms import NewsletterForm
from . forms import FamilyForm
from . models import Family


def create_profil(request):
    form_family = FamilyForm()
    user = request.user
    user_id = user.id

    try:
        family_obj = Family.objects.get(user_id=user_id)
    except Family.DoesNotExist:
        family_obj = None
    if family_obj:  # PROFIL JE VEC KREIRAN
        # TREBA REDIRECT PROFIL
        return redirect(reverse('family:edit_profil',  kwargs={"slug": family_obj.slug}))
    else:  # PROFIL NIJE KREIRAN
        if request.method == "POST":
            form_family = FamilyForm(request.POST, request.FILES)
            if form_family.is_valid():
                family = form_family.save(commit=False)
                family.is_form_submit = True
                family.user_id = user.id
                family.save()
                messages.success(
                    request, 'Uspesno ste kreirali profil')
                return redirect('/')  # TREBA REDIRECT PROFIL
            else:
                messages.success(
                    request, 'Niste uspeli')
                return redirect('/family/create_profil')
        newsletter_form = NewsletterForm()
        return render(request, 'family/create_profil_family.html', {'form_family': form_family, 'form': newsletter_form})


def edit_profil(request, slug):
    family_obj = Family.objects.get(slug=slug)
    context = {'family': family_obj}
    return render(request, 'family/edit_profil_family.html', context)
