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
    prob = models.FloatField()
    fish = models.TextField()
    features = models.TextField()

    def __str__(self):
            return self.content

class Predictionten(models.Model):
    temperature_min = models.TextField()
    temperature_mean = models.TextField()
    temperature_max = models.TextField()
    wind_mean = models.TextField()
    wind_direction = models.TextField()
    gust_max = models.TextField()
    phenomenon = models.TextField()
    pressure_min = models.TextField()
    pressure_max = models.TextField()
    humidity_mean = models.TextField()
    uv_index_mean = models.TextField()
    moon = models.TextField()
    moon_direction = models.TextField()
    date = models.DateField()
    areal = models.TextField()
    city = models.TextField()
    fish = models.TextField()
    prob_min = models.TextField()
    prob_max = models.TextField()

    def __str__(self):
            return self.content