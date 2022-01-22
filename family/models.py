from django.db import models
from account .models import CustomUser
from django.core.validators import RegexValidator, FileExtensionValidator
from . validators import validate_image
from . utils import get_random_code
from django.template.defaultfilters import slugify
from . choices import SITY_CHOICES, NUMBER_CHOICES, AGE_CHOICES, CITIZENSHIP_CHOICES, CHILDCARE_PERIOD_CHOICES
from multiselectfield import MultiSelectField


class Family(models.Model):
    CITIZENSHIP_CHOICES = CITIZENSHIP_CHOICES

    AGE_CHOICES = AGE_CHOICES
    NUMBER_CHOICES = NUMBER_CHOICES
    # FAMILY FIELDS
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    about_me = models.TextField(blank=True)
    about_me_eng = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    picture = models.ImageField(default='no_face.png', upload_to="img/family", validators=[
                                validate_image, FileExtensionValidator(['jpg', 'png', 'jpeg'])], blank=True, null=True, help_text='Slika ne sme biti veća od 2Mb i mora biti formata jpg,png ili jpeg')
    sity = models.CharField(
        max_length=200, choices=SITY_CHOICES, null=True, blank=True)
    mobile_num_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Broj nije u odgovarajućem formatu, +381641234567")
    mobile_number = models.CharField(blank=True, validators=[mobile_num_regex], max_length=17, help_text=(
        "Koristi sledeći format: '+381641234567'"))
    email = models.EmailField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    social_network = models.URLField(max_length=225, blank=True, null=True)
    number_children = models.CharField(
        max_length=5, choices=NUMBER_CHOICES, default='2')
    age_children = MultiSelectField(
        choices=AGE_CHOICES, default='1-3')
    citizenship = models.CharField(
        max_length=50, choices=CITIZENSHIP_CHOICES, default='Srpski Drzavljanin')
    childcare_period = models.CharField(
        max_length=50, choices=CHILDCARE_PERIOD_CHOICES, default='Mesec dana')
    is_form_submit = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.user} - {self.sity} - {self.created}'

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


class FamilyCalendar(models.Model):
    family = models.OneToOneField(
        Family, on_delete=models.CASCADE, blank=True, null=True)
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

    def __str__(self):
        # pk = Family.objects.get(calendar_id=self.id).user_id
        # return f'{CustomUser.objects.get(id=pk).email}-{self.date_added}'
        pk = self.family.user_id
        return f'{CustomUser.objects.get(id=pk).email}-{self.date_added}'
