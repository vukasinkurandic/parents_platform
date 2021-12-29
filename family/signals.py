from django.db.models.signals import post_save
from . models import Family, FamilyCalendar
from django.dispatch import receiver


@receiver(post_save, sender=Family)
def post_save_create_family_calendar(sender, instance, created, **krawgs):
    print('sender', sender)
    print('instance', instance.id)

    if created:
        FamilyCalendar.objects.create(family=instance)
