from rest_framework import serializers
from prediction.models import Prediction, Predictionten
from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework.generics import get_object_or_404
from ..utils.text_generator import TextGenerator


class PredictionSerializer(serializers.ModelSerializer):
    temperature_text = serializers.SerializerMethodField()
    phenomenon_text = serializers.SerializerMethodField()
    prediction_text = serializers.SerializerMethodField()
    wind_text = serializers.SerializerMethodField()

    class Meta:
        model = Prediction
        fields = '__all__'
        # exclude = ['time', 'temperature','wind', 'wind_direction','gust','phenomenon',
        # 'pressure','humidity','uv_index','moon','moon_direction','day','date','areal','city','prob','fish','features']

    def get_temperature_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.temperature_one(instance.date, instance.fish)

    def get_phenomenon_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.phenomenon_one(instance.date, instance.fish)

    def get_prediction_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.prediction_one(instance.date, instance.fish)

    def get_wind_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.wind_one(instance.date, instance.fish)


class PredictiontenSerializer(serializers.ModelSerializer):
    temperature_text = serializers.SerializerMethodField()
    phenomenon_text = serializers.SerializerMethodField()
    prediction_text = serializers.SerializerMethodField()
    wind_text = serializers.SerializerMethodField()

    class Meta:
        model = Predictionten
        fields = '__all__'
        # exclude = ['temperature_min', 'temperature_mean','temperature_max', 'wind_mean','wind_direction','gust_max',
        # 'phenomenon','pressure_min','pressure_max','humidity_mean','uv_index_mean','moon','moon_direction','date','areal','city','fish','prob_min','prob_max']

    def get_temperature_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.temperature_ten(instance.date, instance.fish)

    def get_phenomenon_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.phenomenon_ten(instance.date, instance.fish)

    def get_prediction_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.prediction_ten(instance.date, instance.fish)

    def get_wind_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.wind_ten(instance.date, instance.fish)
