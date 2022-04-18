from django.utils.translation import gettext_lazy as _

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

NUMBER_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('5+', '5+'),

)
NUMBER_EXPERIENCE_CHOICES = (
    ('Nema iskustva', _('Nema iskustva')),
    ('Do godinu dana', _('Do godinu dana')),
    ('Više od godinu dana', _('Više od godinu dana')),

)
AGE_CHOICES = (
    ('0-1', '0-1'),
    ('1-3', '1-3'),
    ('3-5', '3-5'),
    ('5-12', '5-12'),
    ('12-17', '12-17'),
)
CITIZENSHIP_CHOICES = (
    ('Srpski Državljanin', _('Srpski Državljanin')),
    ('Strani Državljanin', _('Strani Državljanin')),
)

CHILDCARE_PERIOD_CHOICES = (
    ('Povremeno', _('Povremeno')),
    ('Manje od mesec dana', _('Manje od mesec dana')),
    ('Mesec dana', _('Mesec dana')),
    ('Par meseci', _('Par meseci')),
    ('Godinu dana', _('Godinu dana')),
    ('Više od godinu dana', _('Više od godinu dana')),
)

SEX_CHOICES = (
    ('Muško', _('Muško')),
    ('Žensko', _('Žensko')),
)
YES_NO_CHOICES = (
    ('Da', _('Da')),
    ('Ne', _('Ne')),
)
WORK_CHOICES = (
    ('Bebisiter/ka', _('Bebisiter/ka')),
    ('Dadilja', _('Dadilja')),
    ('Bebisiter/ka i Dadilja', _('Bebisiter/ka i Dadilja')),

)

# MAKE LIST OF VALUE FOR SITY_CHOICES
sity_choices = SITY_CHOICES
sity_list = []
for field, value in sity_choices:
    sity_list.append(value)

# MAKE LIST OF VALUE FOR CHILDCARE_PERIOD_CHOICES
childcare_period_choices = CHILDCARE_PERIOD_CHOICES
childcare_period_list = []
for field, value in childcare_period_choices:
    childcare_period_list.append(value)

# MAKE LIST OF VALUE FOR WORK_CHOICES
work_choices = WORK_CHOICES
work_list = []
for field, value in work_choices:
    work_list.append(value)

# MAKE LIST OF VALUE FOR NUMBER_CHOICES
number_choices = NUMBER_CHOICES
number_list = []
for field, value in number_choices:
    number_list.append(value)


# MAKE LIST OF VALUE FOR NUMBER_EXPERIENCE_CHOICES
number_experience_choices = NUMBER_EXPERIENCE_CHOICES
number_experience_list = []
for field, value in number_experience_choices:
    number_experience_list.append(value)
