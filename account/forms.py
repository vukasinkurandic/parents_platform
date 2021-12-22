from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
    email = forms.EmailField(error_messages={'unique': ('Email je vec registrovan')}, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'email', 'name': 'email'}))

    is_terms_confirmed = forms.BooleanField(required=True, widget=forms.CheckboxInput(
        attrs={'class': 'form-check-input', 'id': 'exampleCheck1'}))

    error_messages = {
        'password_mismatch': ('Dva polja za lozinku se ne poklapaju.'),
    }

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2', 'is_terms_confirmed']

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
