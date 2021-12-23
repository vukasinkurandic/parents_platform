from django import forms
from . models import Newsletter, ContactMessage


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(error_messages={'unique': ('Email je vec dodat')}, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'name': 'email'}))

    class Meta:
        model = Newsletter
        fields = ['email']


class ContactMessageForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'sender_name', 'name': 'sender_name'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'sender_email', 'name': 'sender_email'}))
    contact_message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'sender_message', 'name': 'sender_message'}))

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'contact_message']
