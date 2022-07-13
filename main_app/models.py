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
    day_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True)
    pain_lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True)
    fatigue_lvl = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True)
    water_cups = models.IntegerField(blank=True)
    sleep_hours = models.IntegerField(blank=True)
    time_outside = models.IntegerField(blank=True)
    meds = models.CharField(max_length=200, blank=True)
    mood = models.CharField(
        max_length=2,
        choices=MOODS,
        default=MOODS[0][0],
        blank=True
    )
    stretch = BooleanField()
    breakfast = models.CharField(max_length=100, blank=True)
    lunch = models.CharField(max_length=100, blank=True)
    dinner = models.CharField(max_length=100, blank=True)
    snacks = models.CharField(max_length=100, blank=True)
    day_notes = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.date.strftime("%d-%b-%y")

    def get_absolute_url(self):
        return reverse('detail', kwargs={'log_id': self.id})

    class Meta:
        ordering = ['-date']
