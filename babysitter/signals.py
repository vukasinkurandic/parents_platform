from django.db.models.signals import post_save
from . models import Babysitter, BabysitterCalendar
from django.dispatch import receiver


@receiver(post_save, sender=Babysitter)
def post_save_create_babysitter_calendar(sender, instance, created, **krawgs):

    if created:
        BabysitterCalendar.objects.create(babysitter=instance)
