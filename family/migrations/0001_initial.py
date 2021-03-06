# Generated by Django 3.2.9 on 2021-12-28 15:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import family.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyCalendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('morning_monday', models.BooleanField(default=False)),
                ('morning_tuesday', models.BooleanField(default=False)),
                ('morning_wednesday', models.BooleanField(default=False)),
                ('morning_thursday', models.BooleanField(default=False)),
                ('morning_friday', models.BooleanField(default=False)),
                ('morning_saturday', models.BooleanField(default=False)),
                ('morning_sunday', models.BooleanField(default=False)),
                ('afternoon_monday', models.BooleanField(default=False)),
                ('afternoon_tuesday', models.BooleanField(default=False)),
                ('afternoon_wednesday', models.BooleanField(default=False)),
                ('afternoon_thursday', models.BooleanField(default=False)),
                ('afternoon_friday', models.BooleanField(default=False)),
                ('afternoon_saturday', models.BooleanField(default=False)),
                ('afternoon_sunday', models.BooleanField(default=False)),
                ('evening_monday', models.BooleanField(default=False)),
                ('evening_tuesday', models.BooleanField(default=False)),
                ('evening_wednesday', models.BooleanField(default=False)),
                ('evening_thursday', models.BooleanField(default=False)),
                ('evening_friday', models.BooleanField(default=False)),
                ('evening_saturday', models.BooleanField(default=False)),
                ('evening_sunday', models.BooleanField(default=False)),
                ('night_monday', models.BooleanField(default=False)),
                ('night_tuesday', models.BooleanField(default=False)),
                ('night_wednesday', models.BooleanField(default=False)),
                ('night_thursday', models.BooleanField(default=False)),
                ('night_friday', models.BooleanField(default=False)),
                ('night_saturday', models.BooleanField(default=False)),
                ('night_sunday', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200)),
                ('about_me', models.TextField(blank=True)),
                ('about_me_eng', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, default='no_face.png', help_text='Slika ne sme biti ve??a od 2Mb i mora biti formata jpg,png ili jpeg', null=True, upload_to='img/family', validators=[family.validators.validate_image, django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('sity', models.CharField(blank=True, choices=[('Beograd', 'Beograd'), ('Novi Sad', 'Novi Sad'), ('Ni??', 'Ni??'), ('Kragujevac', 'Kragujevac'), ('Leskovac', 'Leskovac'), ('Ada', 'Ada'), ('Aleksandrovac', 'Aleksandrovac'), ('Aleksinac', 'Aleksinac'), ('Alibunar', 'Alibunar'), ('Apatin', 'Apatin'), ('Aran??elovac', 'Aran??elovac'), ('Arilje', 'Arilje'), ('Babu??nica', 'Babu??nica'), ('Ba??', 'Ba??'), ('Ba??ka Palanka', 'Ba??ka Palanka'), ('Ba??ka Topola', 'Ba??ka Topola'), ('Ba??ki Petrovac', 'Ba??ki Petrovac'), ('Bajina Ba??ta', 'Bajina Ba??ta'), ('Bato??ina', 'Bato??ina'), ('Be??ej', 'Be??ej'), ('Bela Crkva', 'Bela Crkva'), ('Bela Palanka', 'Bela Palanka'), ('Beo??in', 'Beo??in'), ('Blace', 'Blace'), ('Bogati??', 'Bogati??'), ('Bojnik', 'Bojnik'), ('Boljevac', 'Boljevac'), ('Bor', 'Bor'), ('Bosilegrad', 'Bosilegrad'), ('Brus', 'Brus'), ('Bujanovac', 'Bujanovac'), ('??a??ak', '??a??ak'), ('??ajetina', '??ajetina'), ('??i??evac', '??i??evac'), ('??oka', '??oka'), ('Crna Trava', 'Crna Trava'), ('??uprija', '??uprija'), ('Despotovac', 'Despotovac'), ('Dimitrovgrad', 'Dimitrovgrad'), ('Doljevac', 'Doljevac'), ('Gad??in Han', 'Gad??in Han'), ('Golubac', 'Golubac'), ('Gornji Milanovac', 'Gornji Milanovac'), ('In??ija', 'In??ija'), ('Irig', 'Irig'), ('Ivanjica', 'Ivanjica'), ('Jagodina', 'Jagodina'), ('Kanji??a', 'Kanji??a'), ('Kikinda', 'Kikinda'), ('Kladovo', 'Kladovo'), ('Kni??', 'Kni??'), ('Knja??evac', 'Knja??evac'), ('Koceljeva', 'Koceljeva'), ('Kosjeri??', 'Kosjeri??'), ('Kova??ica', 'Kova??ica'), ('Kovin', 'Kovin'), ('Kraljevo', 'Kraljevo'), ('Krupanj', 'Krupanj'), ('Kru??evac', 'Kru??evac'), ('Ku??evo', 'Ku??evo'), ('Kula', 'Kula'), ('Kur??umlija', 'Kur??umlija'), ('Lajkovac', 'Lajkovac'), ('Lapovo', 'Lapovo'), ('Lebane', 'Lebane'), ('Ljig', 'Ljig'), ('Ljubovija', 'Ljubovija'), ('Loznica', 'Loznica'), ('Lu??ani', 'Lu??ani'), ('Majdanpek', 'Majdanpek'), ('Mali I??o??', 'Mali I??o??'), ('Mali Zvornik', 'Mali Zvornik'), ('Malo Crni??e', 'Malo Crni??e'), ('Medve??a', 'Medve??a'), ('Mero??ina', 'Mero??ina'), ('Mionica', 'Mionica'), ('Negotin', 'Negotin'), ('Nova Crnja', 'Nova Crnja'), ('Nova Varo??', 'Nova Varo??'), ('Novi Be??ej', 'Novi Be??ej'), ('Novi Kne??evac', 'Novi Kne??evac'), ('Novi Pazar', 'Novi Pazar'), ('Od??aci', 'Od??aci'), ('Opovo', 'Opovo'), ('Ose??ina', 'Ose??ina'), ('Pan??evo', 'Pan??evo'), ('Para??in', 'Para??in'), ('Pe??inci', 'Pe??inci'), ('Petrovac na Mlavi', 'Petrovac na Mlavi'), ('Pirot', 'Pirot'), ('Plandi??te', 'Plandi??te'), ('Po??arevac', 'Po??arevac'), ('Po??ega', 'Po??ega'), ('Pre??evo', 'Pre??evo'), ('Priboj', 'Priboj'), ('Prijepolje', 'Prijepolje'), ('Prokuplje', 'Prokuplje'), ('Ra??a', 'Ra??a'), ('Ra??ka', 'Ra??ka'), ('Ra??anj', 'Ra??anj'), ('Rekovac', 'Rekovac'), ('Ruma', 'Ruma'), ('??abac', '??abac'), ('Se??anj', 'Se??anj'), ('Senta', 'Senta'), ('??id', '??id'), ('Sjenica', 'Sjenica'), ('Smederevo', 'Smederevo'), ('Smederevska Palanka', 'Smederevska Palanka'), ('Sokobanja', 'Sokobanja'), ('Sombor', 'Sombor'), ('Srbobran', 'Srbobran'), ('Sremska Mitrovica', 'Sremska Mitrovica'), ('Sremski Karlovci', 'Sremski Karlovci'), ('Stara Pazova', 'Stara Pazova'), ('Subotica', 'Subotica'), ('Surdulica', 'Surdulica'), ('Svilajnac', 'Svilajnac'), ('Svrljig', 'Svrljig'), ('Temerin', 'Temerin'), ('Titel', 'Titel'), ('Topola', 'Topola'), ('Trgovi??te', 'Trgovi??te'), ('Trstenik', 'Trstenik'), ('Tutin', 'Tutin'), ('Ub', 'Ub'), ('U??ice', 'U??ice'), ('Valjevo', 'Valjevo'), ('Varvarin', 'Varvarin'), ('Velika Plana', 'Velika Plana'), ('Veliko Gradi??te', 'Veliko Gradi??te'), ('Vladi??in Han', 'Vladi??in Han'), ('Vladimirci', 'Vladimirci'), ('Vlasotince', 'Vlasotince'), ('Vranje', 'Vranje'), ('Vrbas', 'Vrbas'), ('Vrnja??ka Banja', 'Vrnja??ka Banja'), ('Vr??ac', 'Vr??ac'), ('??abalj', '??abalj'), ('??abari', '??abari'), ('??agubica', '??agubica'), ('Zaje??ar', 'Zaje??ar'), ('??iti??te', '??iti??te'), ('??itora??a', '??itora??a'), ('Zrenjanin', 'Zrenjanin')], max_length=200, null=True)),
                ('mobile_number', models.CharField(blank=True, help_text="Koristi slede??i format: '+381641234567'", max_length=17, validators=[django.core.validators.RegexValidator(message='Broj nije u odgovaraju??em formatu, +381641234567', regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('social_network', models.URLField(blank=True, max_length=225, null=True)),
                ('number_children', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('10+', '10+')], default='2', max_length=5)),
                ('age_children', models.CharField(choices=[('0-1', '0-1'), ('1-3', '1-3'), ('3-5', '3-5'), ('5-12', '5-12'), ('12-18', '12-18')], default='1-3', max_length=10)),
                ('citizenship', models.CharField(choices=[('Srpski Drzavljanin', 'Srpski Drzavljanin'), ('Strani Drzavljanin', 'Strani Drzavljanin')], default='Srpski Drzavljanin', max_length=50)),
                ('is_form_submit', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('calendar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='family.familycalendar')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
