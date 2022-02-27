from django.db import models
from family . models import Family
from babysitter . models import Babysitter


class Favorite(models.Model):
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, related_name='family_favorite')
    babysitter = models.ForeignKey(
        Babysitter, on_delete=models.CASCADE, related_name='babysitter_favorite')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.family} - {self.babysitter}'
