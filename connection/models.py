from django.db import models
from family . models import Family
from babysitter . models import Babysitter


class Connection(models.Model):
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name='family_match')
    babysitter = models.ForeignKey(
        Babysitter, on_delete=models.CASCADE, related_name='babysitter_match')
    is_matched = models.BooleanField(default=None, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def matched_check(connection):
        return connection.is_matched

    def __str__(self):
        return f'{self.family} - {self.babysitter}'
