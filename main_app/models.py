from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import BooleanField
from django.urls import reverse

MOODS = (
    (':D', 'Big Smile'),
    (':)', 'Slight Smile'),
    (':|', 'Neutral'),
    ('):', 'Slight Frown'),
    ('D:', 'Big Frown')
)

# Create your models here.
class Log(models.Model):
    date = models.DateField('log date')
    day_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    pain_lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    fatigue_lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    water_cups = models.IntegerField()
    sleep_hours = models.IntegerField()
    time_outside = models.IntegerField()
    meds = models.CharField(max_length=200)
    mood = models.CharField(
        max_length=2,
        choices=MOODS,
        default=MOODS[0][0]
    )
    stretch = BooleanField()
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)
    snacks = models.CharField(max_length=100)
    day_notes = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%d-%b-%y")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'log_id': self.id})
