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
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'name': 'user_year', 'id': 'user_year'})),

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
            'citizenship',
            'age'
        ]

    def __init__(self, *args, **kwargs):
        super(FamilyForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['about_me'].widget.attrs['class'] = 'form-control'
        self.fields['about_me_eng'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['sity'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['social_network'].widget.attrs['class'] = 'form-control'
        self.fields['number_children'].widget.attrs['class'] = 'form-control'
        self.fields['age_children'].widget.attrs['class'] = 'form-control'
        self.fields['citizenship'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['class'] = 'form-control'


class FamilyCalendar(forms.ModelForm):
    pass
