from django.db import models
from account .models import CustomUser
from django.core.validators import RegexValidator, FileExtensionValidator
from family . validators import validate_image
from family . utils import get_random_code
from django.template.defaultfilters import slugify
from family . choices import SITY_CHOICES, NUMBER_CHOICES, AGE_CHOICES, CITIZENSHIP_CHOICES


class Babysitter(models.Model):
    SEX_CHOICES = (
        ('Muško', 'Muško'),
        ('Žensko', 'Žensko'),
    )
    YES_NO_CHOICES = (
        ('Da', 'Da'),
        ('Ne', 'Ne'),
    )
    WORK_CHOICES = (
        ('Bebisiter', 'Bebisiter'),
        ('Dadilja', 'Dadilja'),
    )
    CITIZENSHIP_CHOICES = CITIZENSHIP_CHOICES
    AGE_CHOICES = AGE_CHOICES
    NUMBER_CHOICES = NUMBER_CHOICES
    # BABYSITTER FIELDS
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(default='no_face.png', upload_to="img/babysitter", validators=[
                                validate_image, FileExtensionValidator(['jpg', 'png', 'jpeg'])], blank=True, null=True, help_text='Slika ne sme biti veća od 2Mb i mora biti formata jpg,png ili jpeg')
    age = models.PositiveIntegerField(null=True, blank=True)
    sex = models.CharField(
        max_length=15, choices=SEX_CHOICES, default='Žensko')
    sity = models.CharField(
        max_length=200, choices=SITY_CHOICES, null=True, blank=True)

    hourly_rate = models.PositiveIntegerField(
        blank=True, null=True)
    mobile_num_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Broj nije u odgovarajućem formatu, +381641234567")
    mobile_number = models.CharField(blank=True, validators=[mobile_num_regex], max_length=17, help_text=(
        "Koristi sledeći format: '+381641234567'"))
    email = models.EmailField(max_length=200, blank=True)
    social_network = models.URLField(max_length=225, blank=True, null=True)
    about_me = models.TextField(blank=True)
    about_me_eng = models.TextField(blank=True)
    years_care_experience = models.CharField(
        max_length=5, choices=NUMBER_CHOICES, blank=True, null=True)
    work_type = models.CharField(
        max_length=15, choices=WORK_CHOICES, blank=True, null=True)
    car = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    driver_license = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    pets = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    own_children = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    house = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    cooking = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    school_activities = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    children_with_special_needs = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    home_job = models.CharField(
        max_length=5, choices=YES_NO_CHOICES, default='Ne')
    slug = models.SlugField(unique=True, blank=True)
    age_children = models.CharField(
        max_length=10, choices=AGE_CHOICES, default='1-3')
    citizenship = models.CharField(
        max_length=50, choices=CITIZENSHIP_CHOICES, default='Srpski Drzavljanin')
    is_form_submit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.user} - {self.sity} - {self.created} - {self.sex}- {self.age}'

    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            base_slug = slugify(str(self.first_name) +
                                " " + str(self.last_name))
        elif self.first_name:
            base_slug = str(self.first_name)
        else:
            base_slug = str(self.user)
        to_slug = slugify(base_slug + " " + str(get_random_code()))
        self.slug = to_slug
        super().save(*args, **kwargs)


class BabysitterCalendar(models.Model):
    babysitter = models.OneToOneField(
        Babysitter, on_delete=models.CASCADE, blank=True, null=True)
    morning_monday = models.BooleanField(default=False)
    morning_tuesday = models.BooleanField(default=False)
    morning_wednesday = models.BooleanField(default=False)
    morning_thursday = models.BooleanField(default=False)
    morning_friday = models.BooleanField(default=False)
    morning_saturday = models.BooleanField(default=False)
    morning_sunday = models.BooleanField(default=False)

    afternoon_monday = models.BooleanField(default=False)
    afternoon_tuesday = models.BooleanField(default=False)
    afternoon_wednesday = models.BooleanField(default=False)
    afternoon_thursday = models.BooleanField(default=False)
    afternoon_friday = models.BooleanField(default=False)
    afternoon_saturday = models.BooleanField(default=False)
    afternoon_sunday = models.BooleanField(default=False)

    evening_monday = models.BooleanField(default=False)
    evening_tuesday = models.BooleanField(default=False)
    evening_wednesday = models.BooleanField(default=False)
    evening_thursday = models.BooleanField(default=False)
    evening_friday = models.BooleanField(default=False)
    evening_saturday = models.BooleanField(default=False)
    evening_sunday = models.BooleanField(default=False)

    night_monday = models.BooleanField(default=False)
    night_tuesday = models.BooleanField(default=False)
    night_wednesday = models.BooleanField(default=False)
    night_thursday = models.BooleanField(default=False)
    night_friday = models.BooleanField(default=False)
    night_saturday = models.BooleanField(default=False)
    night_sunday = models.BooleanField(default=False)

    date_added = models.DateTimeField(auto_now_add=True)
