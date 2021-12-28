from django.db import models
from account .models import CustomUser
from django.core.validators import RegexValidator, FileExtensionValidator
from . validators import validate_image
from . utils import get_random_code
from django.template.defaultfilters import slugify


class FamilyCalendar(models.Model):
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


class Family(models.Model):
    CITIZENSHIP_CHOICES = (
        ('Srpski Drzavljanin', 'Srpski Drzavljanin'),
        ('Strani Drzavljanin', 'Strani Drzavljanin'),
    )
    AGE_CHOICES = (
        ('0-1', '0-1'),
        ('1-3', '1-3'),
        ('3-5', '3-5'),
        ('5-12', '5-12'),
        ('12-18', '12-18'),
    )
    NUMBER_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
    SITY_CHOICES = (
        ('Beograd', 'Beograd'),
        ('Novi Sad', 'Novi Sad'),
        ('Niš', 'Niš'),
        ('Kragujevac', 'Kragujevac'),
        ('Leskovac', 'Leskovac'),
        ('Ada', 'Ada'),
        ('Aleksandrovac', 'Aleksandrovac'),
        ('Aleksinac', 'Aleksinac'),
        ('Alibunar', 'Alibunar'),
        ('Apatin', 'Apatin'),
        ('Aranđelovac', 'Aranđelovac'),
        ('Arilje', 'Arilje'),
        ('Babušnica', 'Babušnica'),
        ('Bač', 'Bač'),
        ('Bačka Palanka', 'Bačka Palanka'),
        ('Bačka Topola', 'Bačka Topola'),
        ('Bački Petrovac', 'Bački Petrovac'),
        ('Bajina Bašta', 'Bajina Bašta'),
        ('Batočina', 'Batočina'),
        ('Bečej', 'Bečej'),
        ('Bela Crkva', 'Bela Crkva'),
        ('Bela Palanka', 'Bela Palanka'),
        ('Beočin', 'Beočin'),
        ('Blace', 'Blace'),
        ('Bogatić', 'Bogatić'),
        ('Bojnik', 'Bojnik'),
        ('Boljevac', 'Boljevac'),
        ('Bor', 'Bor'),
        ('Bosilegrad', 'Bosilegrad'),
        ('Brus', 'Brus'),
        ('Bujanovac', 'Bujanovac'),
        ('Čačak', 'Čačak'),
        ('Čajetina', 'Čajetina'),
        ('Ćićevac', 'Ćićevac'),
        ('Čoka', 'Čoka'),
        ('Crna Trava', 'Crna Trava'),
        ('Ćuprija', 'Ćuprija'),
        ('Despotovac', 'Despotovac'),
        ('Dimitrovgrad', 'Dimitrovgrad'),
        ('Doljevac', 'Doljevac'),
        ('Gadžin Han', 'Gadžin Han'),
        ('Golubac', 'Golubac'),
        ('Gornji Milanovac', 'Gornji Milanovac'),
        ('Inđija', 'Inđija'),
        ('Irig', 'Irig'),
        ('Ivanjica', 'Ivanjica'),
        ('Jagodina', 'Jagodina'),
        ('Kanjiža', 'Kanjiža'),
        ('Kikinda', 'Kikinda'),
        ('Kladovo', 'Kladovo'),
        ('Knić', 'Knić'),
        ('Knjaževac', 'Knjaževac'),
        ('Koceljeva', 'Koceljeva'),
        ('Kosjerić', 'Kosjerić'),
        ('Kovačica', 'Kovačica'),
        ('Kovin', 'Kovin'),
        ('Kraljevo', 'Kraljevo'),
        ('Krupanj', 'Krupanj'),
        ('Kruševac', 'Kruševac'),
        ('Kučevo', 'Kučevo'),
        ('Kula', 'Kula'),
        ('Kuršumlija', 'Kuršumlija'),
        ('Lajkovac', 'Lajkovac'),
        ('Lapovo', 'Lapovo'),
        ('Lebane', 'Lebane'),
        ('Ljig', 'Ljig'),
        ('Ljubovija', 'Ljubovija'),
        ('Loznica', 'Loznica'),
        ('Lučani', 'Lučani'),
        ('Majdanpek', 'Majdanpek'),
        ('Mali Iđoš', 'Mali Iđoš'),
        ('Mali Zvornik', 'Mali Zvornik'),
        ('Malo Crniće', 'Malo Crniće'),
        ('Medveđa', 'Medveđa'),
        ('Merošina', 'Merošina'),
        ('Mionica', 'Mionica'),
        ('Negotin', 'Negotin'),
        ('Nova Crnja', 'Nova Crnja'),
        ('Nova Varoš', 'Nova Varoš'),
        ('Novi Bečej', 'Novi Bečej'),
        ('Novi Kneževac', 'Novi Kneževac'),
        ('Novi Pazar', 'Novi Pazar'),
        ('Odžaci', 'Odžaci'),
        ('Opovo', 'Opovo'),
        ('Osečina', 'Osečina'),
        ('Pančevo', 'Pančevo'),
        ('Paraćin', 'Paraćin'),
        ('Pećinci', 'Pećinci'),
        ('Petrovac na Mlavi', 'Petrovac na Mlavi'),
        ('Pirot', 'Pirot'),
        ('Plandište', 'Plandište'),
        ('Požarevac', 'Požarevac'),
        ('Požega', 'Požega'),
        ('Preševo', 'Preševo'),
        ('Priboj', 'Priboj'),
        ('Prijepolje', 'Prijepolje'),
        ('Prokuplje', 'Prokuplje'),
        ('Rača', 'Rača'),
        ('Raška', 'Raška'),
        ('Ražanj', 'Ražanj'),
        ('Rekovac', 'Rekovac'),
        ('Ruma', 'Ruma'),
        ('Šabac', 'Šabac'),
        ('Sečanj', 'Sečanj'),
        ('Senta', 'Senta'),
        ('Šid', 'Šid'),
        ('Sjenica', 'Sjenica'),
        ('Smederevo', 'Smederevo'),
        ('Smederevska Palanka', 'Smederevska Palanka'),
        ('Sokobanja', 'Sokobanja'),
        ('Sombor', 'Sombor'),
        ('Srbobran', 'Srbobran'),
        ('Sremska Mitrovica', 'Sremska Mitrovica'),
        ('Sremski Karlovci', 'Sremski Karlovci'),
        ('Stara Pazova', 'Stara Pazova'),
        ('Subotica', 'Subotica'),
        ('Surdulica', 'Surdulica'),
        ('Svilajnac', 'Svilajnac'),
        ('Svrljig', 'Svrljig'),
        ('Temerin', 'Temerin'),
        ('Titel', 'Titel'),
        ('Topola', 'Topola'),
        ('Trgovište', 'Trgovište'),
        ('Trstenik', 'Trstenik'),
        ('Tutin', 'Tutin'),
        ('Ub', 'Ub'),
        ('Užice', 'Užice'),
        ('Valjevo', 'Valjevo'),
        ('Varvarin', 'Varvarin'),
        ('Velika Plana', 'Velika Plana'),
        ('Veliko Gradište', 'Veliko Gradište'),
        ('Vladičin Han', 'Vladičin Han'),
        ('Vladimirci', 'Vladimirci'),
        ('Vlasotince', 'Vlasotince'),
        ('Vranje', 'Vranje'),
        ('Vrbas', 'Vrbas'),
        ('Vrnjačka Banja', 'Vrnjačka Banja'),
        ('Vršac', 'Vršac'),
        ('Žabalj', 'Žabalj'),
        ('Žabari', 'Žabari'),
        ('Žagubica', 'Žagubica'),
        ('Zaječar', 'Zaječar'),
        ('Žitište', 'Žitište'),
        ('Žitorađa', 'Žitorađa'),
        ('Zrenjanin', 'Zrenjanin'),
    )
    # FAMILY FIELDS
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    about_me = models.TextField(blank=True)
    about_me_eng = models.TextField(blank=True)
    picture = models.ImageField(default='no_face.png', upload_to="img/", validators=[
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
    age_children = models.CharField(
        max_length=10, choices=AGE_CHOICES, default='1-3')
    citizenship = models.CharField(
        max_length=50, choices=CITIZENSHIP_CHOICES, default='Srpski Drzavljanin')
    calendar = models.ForeignKey(
        FamilyCalendar, on_delete=models.CASCADE, blank=True, null=True)
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
