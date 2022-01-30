from django import forms
from . models import Babysitter, BabysitterCalendar


class BabysitterForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'siter_name', 'name': 'siter_name'})),
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'siter_surname', 'name': 'siter_surname'})),
    about_me = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'siter_about_me', 'name': 'siter_about_me'})),
    about_me_eng = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'sitier_about_me_eng', 'name': 'sitier_about_me_eng'})),
    picture = forms.ImageField(error_messages={'invalid': ("Image files only")}, widget=forms.FileInput(
        attrs={'class': 'form-control', 'id': 'user_image', 'name': 'user_image'})),
    sity = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_city', 'name': 'siter_city', 'aria-label': 'Default select example'})),
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'siter_phone', 'name': 'siter_phone'})),
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'siter_email', 'name': 'siter_email'})),
    social_network = forms.URLField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'siter_social_network', 'name': 'siter_social_network'})),
    age_children = forms.MultipleChoiceField(widget=forms.CheckboxInput(
        attrs={'class': 'chk', 'id': 'user_child_number', 'name': 'user_child_number', 'aria-label': 'Default select example'})),
    citizenship = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'user_municipality', 'name': 'user_municipality'})),
    age = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'name': 'user_year', 'id': 'user_year'})),

    sex = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_sex', 'name': 'siter_sex', 'aria-label': 'Default select example'})),
    hourly_rate = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'siter_money', 'name': 'siter_money'})),
    years_care_experience = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_experience', 'name': 'siter_experience'})),
    work_type = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_bd', 'name': 'siter_bd', 'aria-label': 'Default select example'})),
    car = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_car', 'name': 'siter_car', 'aria-label': 'Default select example'})),
    sick_child = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'sick_child', 'name': 'sick_child', 'aria-label': 'Default select example'})),
    travel = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'travel', 'name': 'travel', 'aria-label': 'Default select example'})),
    pets = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_pet', 'name': 'siter_pet', 'aria-label': 'Default select example'})),
    own_children = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_hc', 'name': 'siter_hc', 'aria-label': 'Default select example'})),
    house = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_home', 'name': 'siter_home', 'aria-label': 'Default select example'})),
    cooking = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_food', 'name': 'siter_food', 'aria-label': 'Default select example'})),
    school_activities = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_schol_act', 'name': 'siter_schol_act', 'aria-label': 'Default select example'})),
    home_job = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_house_job', 'name': 'siter_house_job', 'aria-label': 'Default select example'})),
    children_with_special_needs = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-select', 'id': 'siter_spec_chd', 'name': 'siter_pet', 'aria-label': 'Default select example'})),

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
            'sick_child',  # BooleanField
            'travel',  # BooleanField
            'pets',  # BooleanField
            'own_children',  # BooleanField
            'house',  # BooleanField
            'cooking',  # BooleanField
            'school_activities',  # BooleanField
            'home_job',  # BooleanField
            'children_with_special_needs'  # BooleanField



        ]

    def __init__(self, *args, **kwargs):
        super(BabysitterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['about_me'].widget.attrs['class'] = 'form-control'
        self.fields['about_me_eng'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['picture'].widget.initial_text = ("")
        self.fields['picture'].widget.input_text = ("")
        self.fields['sity'].widget.attrs['class'] = 'form-select'
        self.fields['mobile_number'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['social_network'].widget.attrs['class'] = 'form-control'
        self.fields['age_children'].widget.attrs['class'] = 'chk'
        self.fields['citizenship'].widget.attrs['class'] = 'form-select'
        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['home_job'].widget.attrs['class'] = 'form-select'
        self.fields['sex'].widget.attrs['class'] = 'form-select'
        self.fields['hourly_rate'].widget.attrs['class'] = 'form-control'
        self.fields['years_care_experience'].widget.attrs['class'] = 'form-select'
        self.fields['work_type'].widget.attrs['class'] = 'form-select'
        self.fields['car'].widget.attrs['class'] = 'form-select'
        self.fields['sick_child'].widget.attrs['class'] = 'form-select'
        self.fields['travel'].widget.attrs['class'] = 'form-select'
        self.fields['pets'].widget.attrs['class'] = 'form-select'
        self.fields['own_children'].widget.attrs['class'] = 'form-select'
        self.fields['house'].widget.attrs['class'] = 'form-select'
        self.fields['cooking'].widget.attrs['class'] = 'form-select'
        self.fields['school_activities'].widget.attrs['class'] = 'form-select'
        self.fields['children_with_special_needs'].widget.attrs['class'] = 'form-select'


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
