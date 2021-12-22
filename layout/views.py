from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Newsletter
from . forms import NewsletterForm


def home(request):
    form = NewsletterForm()
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Hvala, Uspešno ste poslali email!'))
        context = {'form': form}
        return redirect('layout:home')
    context = {'form': form}
    return render(request, 'layout/index.html', context)


def contact(request):
    return render(request, 'layout/contact.html')


# if request.method == "POST":
#     subscribedUsers = Newsletter()
#     post_data = request.POST.copy()
#     email = post_data.get("exampleInputEmail1", None)
#     subscribedUsers.email = email
#     subscribedUsers.save()
