from django.db import models
from django.conf import settings

# Create your models here.
class Prediction(models.Model):
    time = models.IntegerField()
    temperature = models.IntegerField()
    wind = models.IntegerField()
    wind_direction = models.TextField()
    gust = models.IntegerField()
    phenomenon = models.TextField()
    pressure = models.IntegerField()
    humidity = models.FloatField()
    uv_index = models.IntegerField()
    moon = models.FloatField()
    moon_direction = models.IntegerField()
    day = models.IntegerField()
    date = models.DateField()
    areal = models.TextField()
    city = models.TextField()
    probs = models.TextField()

    def __str__(self):
            return self.content