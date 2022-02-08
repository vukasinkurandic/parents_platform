# Generated by Django 3.2.9 on 2022-02-06 13:25

import django.core.validators
from django.db import migrations, models
import family.models
import family.validators
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0007_alter_family_number_children'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='picture',
            field=models.ImageField(blank=True, default='no_face.png', help_text='Slika ne sme biti veća od 2Mb i mora biti formata jpg,png ili jpeg', null=True, upload_to=functools.partial(family.models.make_filepath, *('image',), **{}), validators=[family.validators.validate_image, django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])]),
        ),
    ]