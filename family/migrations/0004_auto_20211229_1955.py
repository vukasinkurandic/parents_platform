# Generated by Django 3.2.9 on 2021-12-29 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_alter_family_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='calendar',
        ),
        migrations.AddField(
            model_name='familycalendar',
            name='family',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='family.family'),
        ),
    ]
