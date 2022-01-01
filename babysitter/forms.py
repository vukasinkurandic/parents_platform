from django import forms
from . models import Babysitter, BabysitterCalendar


class BabysitterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_name', 'name': 'user_name'})),
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_surname', 'name': 'user_surname'})),
    about_me = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'about_me', 'name': 'about_me'})),
    about_me_eng = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'about_me_eng', 'name': 'about_me_eng'})),
    picture = forms.ImageField(error_messages={'invalid': ("Image files only")}, widget=forms.FileInput(
        attrs={'class': 'form-control', 'id': 'user_image', 'name': 'user_image'})),
    sity = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'user_city', 'name': 'user_city', 'aria-label': 'Default select example'})),
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_phone', 'name': 'user_phone'})),
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'user_email', 'name': 'user_email'})),
    social_network = forms.URLField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'user_social_network', 'name': 'user_social_network'})),
    age_children = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'user_child_year', 'name': 'user_child_year', 'aria-label': 'Default select example'})),
    citizenship = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'form-check-input', 'name': 'flexRadioDefault'})),
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'name': 'user_year', 'id': 'user_year'})),

    sex = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': '', 'name': '', 'aria-label': 'Default select example'})),
    hourly_rate = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': '', 'name': '', 'aria-label': 'Default select example'})),
    years_care_experience = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': '', 'name': '', 'aria-label': 'Default select example'})),
    work_type = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': '', 'name': '', 'aria-label': 'Default select example'})),
    car = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    driver_license = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    pets = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    own_children = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    house = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    cooking = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    school_activities = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''})),
    children_with_special_needs = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={'class': 'form-control', 'id': ''}))

    class Meta:
        model = Babysitter
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
            'age_children',
            'citizenship',
            'age',


            'sex',  # choice
            'hourly_rate',  # MoneyField
            'years_care_experience',  # choice
            'work_type',  # choice
            'car',  # BooleanField
            'driver_license',  # BooleanField
            'pets',  # BooleanField
            'own_children',  # BooleanField
            'house',  # BooleanField
            'cooking',  # BooleanField
            'school_activities',  # BooleanField
            'children_with_special_needs'  # BooleanField


        ]

    def __init__(self, *args, **kwargs):
        super(BabysitterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['about_me'].widget.attrs['class'] = 'form-control'
        self.fields['about_me_eng'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['sity'].widget.attrs['class'] = 'form-control'
        self.fields['mobile_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['social_network'].widget.attrs['class'] = 'form-control'
        self.fields['age_children'].widget.attrs['class'] = 'form-control'
        self.fields['citizenship'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['class'] = 'form-control'

        self.fields['sex'].widget.attrs['class'] = 'form-control'
        self.fields['hourly_rate'].widget.attrs['class'] = 'form-control'
        self.fields['years_care_experience'].widget.attrs['class'] = 'form-control'
        self.fields['work_type'].widget.attrs['class'] = 'form-control'
        self.fields['car'].widget.attrs['class'] = 'form-control'
        self.fields['driver_license'].widget.attrs['class'] = 'form-control'
        self.fields['pets'].widget.attrs['class'] = 'form-control'
        self.fields['own_children'].widget.attrs['class'] = 'form-control'
        self.fields['house'].widget.attrs['class'] = 'form-control'
        self.fields['cooking'].widget.attrs['class'] = 'form-control'
        self.fields['school_activities'].widget.attrs['class'] = 'form-control'
        self.fields['children_with_special_needs'].widget.attrs['class'] = 'form-control'


class BabysitterCalendarForm(forms.ModelForm):
    morning_monday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    morning_tuesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    morning_wednesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    morning_thursday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    morning_friday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    morning_saturday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    morning_sunday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_monday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_tuesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_wednesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_thursday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_friday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_saturday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    afternoon_sunday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_monday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_tuesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_wednesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_thursday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_friday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_saturday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    evening_sunday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_monday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_tuesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_wednesday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_thursday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_friday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_saturday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))
    night_sunday = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={'class': 'chk'}))

    class Meta:
        model = BabysitterCalendar
        fields = '__all__'
