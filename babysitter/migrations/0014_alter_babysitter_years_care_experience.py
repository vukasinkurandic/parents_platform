# Generated by Django 3.2.9 on 2022-03-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babysitter', '0013_auto_20220225_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babysitter',
            name='years_care_experience',
            field=models.CharField(blank=True, choices=[('Nema iskustva', 'Nema iskustva'), ('Do godinu dana', 'Do godinu dana'), ('Više od godinu dana', 'Više od godinu dana')], max_length=255, null=True),
        ),
    ]
