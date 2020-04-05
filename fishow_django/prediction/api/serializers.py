from rest_framework import serializers
from prediction.models import Prediction
from datetime import datetime,timezone
from django.utils.timesince import timesince


class PredictionSerializer(serializers.ModelSerializer):


    class Meta:
         model = Prediction
         fields = '__all__'

