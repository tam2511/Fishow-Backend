from django.db import models
from django.conf import settings

# Create your models here.
# class Prediction(models.Model):
#     time = models.IntegerField()
#     temperature = models.IntegerField()
#     wind = models.IntegerField()
#     wind_direction = models.TextField()
#     gust = models.IntegerField()
#     phenomenon = models.TextField()
#     pressure = models.IntegerField()
#     humidity = models.FloatField()
#     uv_index = models.IntegerField()
#     moon = models.FloatField()
#     moon_direction = models.IntegerField()
#     day = models.IntegerField()
#     date = models.DateField()
#     areal = models.TextField()
#     city = models.TextField()
#     prob = models.FloatField()
#     fish = models.TextField()
#     features = models.TextField()
    # water_temperature = models.FloatField()

#     def __str__(self):
#             return self
 class Prediction(models.Model):
    temperature = models.TextField() # "-1,+1,+2,+5,-2,-3,+4,0" - максимум 32 символа
    wind = models.TextField() # "3,4,5,1,3,4,2,3" - максимум 24 символа
    wind_direction = models.TextField() # "З,З,З,ЗС,В,СВ,Ю,ЮЗ" - максимум 24 символа
    gust = models.TextField() # "3,4,5,1,3,4,2,3" - максимум 24 символа
    phenomenon = models.TextField() # "облачно.дождь,гроза,пасмурно.ясно....." - не ограничено
    pressure = models.TextField() # "730,744,751,719,734,745,725,732" - максимум 32 символа
    humidity = models.TextField() # "30,44,51,19,34,45,25,32" - максимум 24 символа
    uv_index = models.TextField() # "3,4,5,1,3,4,2,3" - максимум 24 символа
    moon = models.FloatField() # 0.12
    moon_direction = models.IntegerField() # -1
    date = models.DateField() # 2020.07.15
    areal = models.TextField() # Московская область
    city = models.TextField() # Москва
    prob = models.TextField() # "34,45,53,11,34,46,28,33" - максимум 24 символа
    fish = models.TextField()  # "щука" - максимум 24 символов
    sun_up = models.TextField()  # "12:22" - максимум 5 символов
    sun_down = models.TextField()  # "21:32" - максимум 5 символов


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
    # water_temperature = models.TextField()

#     def __str__(self):
#             return self.content