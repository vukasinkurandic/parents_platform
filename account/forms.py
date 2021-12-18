from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    is_terms_confirmed = forms.BooleanField(required=True)

    error_messages = {
        'password_mismatch': ('Dva polja za lozinku se ne poklapaju.'),
    }

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2', 'is_terms_confirmed']
