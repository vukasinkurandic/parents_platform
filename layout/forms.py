from django import forms
from . models import Newsletter


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(error_messages={'unique': ('Email je vec dodat')}, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'name': 'email'}))

    class Meta:
        model = Newsletter
        fields = ['email']
