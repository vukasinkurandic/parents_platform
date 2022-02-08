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
    published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_of_commentary} - {self.commentated_person} - {self.commentary_body} - {self.date}'


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

    def __str__(self):
        return f'{self.author_of_rate} - {self.rated_person} - {self.score} - {self.date}'


class Report(models.Model):

    author_of_report = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='author_of_report')
    reported_person = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='reported_person')
    report_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_of_report} - {self.reported_person} - {self.report_body} - {self.date}'
