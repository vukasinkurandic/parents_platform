# Generated by Django 3.2.9 on 2022-02-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
