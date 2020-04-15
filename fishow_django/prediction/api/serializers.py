from rest_framework import serializers
from prediction.models import Prediction,Predictionten
from datetime import datetime,timezone
from django.utils.timesince import timesince


class PredictionSerializer(serializers.ModelSerializer):


    class Meta:
         model = Prediction
         fields = '__all__'
         #exclude = ['time', 'temperature','wind', 'wind_direction','gust','phenomenon',
         #'pressure','humidity','uv_index','moon','moon_direction','day','date','areal','city','prob','fish','features']

class PredictiontenSerializer(serializers.ModelSerializer):


    class Meta:
         model = Predictionten
         fields = '__all__'
         #exclude = ['temperature_min', 'temperature_mean','temperature_max', 'wind_mean','wind_direction','gust_max',
         #'phenomenon','pressure_min','pressure_max','humidity_mean','uv_index_mean','moon','moon_direction','date','areal','city','fish','prob_min','prob_max']
