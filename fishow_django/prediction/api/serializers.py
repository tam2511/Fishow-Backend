from rest_framework import serializers
from prediction.models import Prediction
from datetime import datetime,timezone
from django.utils.timesince import timesince


class PredictionSerializer(serializers.ModelSerializer):


    class Meta:
         model = Prediction
         exclude = ['time', 'temperature','wind', 'wind_direction','gust','phenomenon',
         'pressure','humidity','uv_index','moon','moon_direction','day','date','areal','city','prob','fish','features']
