from django import forms
from . models import Family, FamilyCalendar


class FamilyForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_name', 'name': 'user_name'})),
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_surname', 'name': 'user_surname'})),
    about_me = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'about_me', 'name': 'about_me'})),
    about_me_eng = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'about_me_eng', 'name': 'about_me_eng'})),
    picture = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'id': 'user_image', 'name': 'user_image'})),
    sity = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'user_city', 'name': 'user_city', 'aria-label': 'Default select example'})),
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_phone', 'name': 'user_phone'})),
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'user_email', 'name': 'user_email'})),
    social_network = forms.URLField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_social_network', 'name': 'user_social_network'})),
    number_children = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'user_child_number', 'name': 'user_child_number', 'aria-label': 'Default select example'})),
    age_children = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'user_child_year', 'name': 'user_child_year', 'aria-label': 'Default select example'})),
    citizenship = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'form-check-input', 'name': 'flexRadioDefault'})),

    class Meta:
        model = Family
        fields = [
            'first_name',
            'last_name',
            'about_me',
            'about_me_eng',
            'picture',
            'sity',
            'mobile_number',
            'email',
            'social_network',
            'number_children',
            'age_children',
            'citizenship'

        ]


class FamilyCalendar(forms.ModelForm):
    pass
