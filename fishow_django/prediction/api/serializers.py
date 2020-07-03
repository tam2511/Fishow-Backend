from rest_framework import serializers
from prediction.models import Prediction,Predictionten
from datetime import datetime,timezone
from django.utils.timesince import timesince
from rest_framework.generics import get_object_or_404

class PredictionSerializer(serializers.ModelSerializer):
    temperature_text = serializers.SerializerMethodField()

    class Meta:
         model = Prediction
         fields = '__all__'
         #exclude = ['time', 'temperature','wind', 'wind_direction','gust','phenomenon',
         #'pressure','humidity','uv_index','moon','moon_direction','day','date','areal','city','prob','fish','features']
    def get_temperature_text(self, instance):
        temp = Prediction.objects.filter(city=instance.city,fish=instance.fish, areal=instance.areal, date=instance.date)
        temperatures=temp[0].temperature
        print(temperatures)
        print('daaa')
        return 'aaaaaaaaa  tut libo stroka libo chislo. dobavim veter tekushego' + str(instance.wind)


class PredictiontenSerializer(serializers.ModelSerializer):

    temperature_text = serializers.SerializerMethodField()
    class Meta:
         model = Predictionten
         fields = '__all__'
         #exclude = ['temperature_min', 'temperature_mean','temperature_max', 'wind_mean','wind_direction','gust_max',
         #'phenomenon','pressure_min','pressure_max','humidity_mean','uv_index_mean','moon','moon_direction','date','areal','city','fish','prob_min','prob_max']

    def get_temperature_text(self, instance):
        return 'pogodochka'