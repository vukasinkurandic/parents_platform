from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from account .models import CustomUser
from family . models import Family
from babysitter . models import Babysitter


class Commentary(models.Model):

    author_of_commentary = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='author_of_commentary')
    commentated_person = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='commentated_person')
    commentary_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):

    author_of_rate = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='author_of_rate')
    rated_person = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='rated_person')
    score = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0),
                                ]
                                )
    date = models.DateTimeField(auto_now_add=True)


class Report(models.Model):

    author_of_report = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='author_of_rate')
    reported_person = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='rated_person')
    report_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
