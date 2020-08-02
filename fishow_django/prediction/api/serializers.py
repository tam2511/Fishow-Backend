from rest_framework import serializers
from prediction.models import Prediction, Predictionten
from datetime import datetime, timezone
from django.utils.timesince import timesince
from rest_framework.generics import get_object_or_404
from ..utils.text_generator import TextGenerator


class PredictionSerializer(serializers.ModelSerializer):
    temperature_brief = serializers.SerializerMethodField()
    temperature_fish = serializers.SerializerMethodField()
    temperature_desc = serializers.SerializerMethodField()
    phenomenon_warning = serializers.SerializerMethodField()
    prediction_text = serializers.SerializerMethodField()
    wind_text = serializers.SerializerMethodField()
    pressure_text = serializers.SerializerMethodField()
    moon_text = serializers.SerializerMethodField()

    class Meta:
        model = Prediction
        fields = '__all__'
        # exclude = ['time', 'temperature','wind', 'wind_direction','gust','phenomenon',
        # 'pressure','humidity','uv_index','moon','moon_direction','day','date','areal','city','prob','fish','features']

    def get_temperature_brief(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_temperature_brief(instance.fish)

    def get_temperature_fish(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_temperature_fish(instance.fish)

    def get_temperature_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_temperature_desc(instance.date, instance.fish)

    def get_phenomenon_warning(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_phenomenon_warning(instance.fish)

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

    def get_pressure_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.pressure_one(instance.date, instance.fish)

    def get_moon_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.moon_one(instance.date, instance.fish)


class PredictiontenSerializer(serializers.ModelSerializer):
    temperature_brief = serializers.SerializerMethodField()
    temperature_fish = serializers.SerializerMethodField()
    temperature_desc = serializers.SerializerMethodField()
    phenomenon_warning = serializers.SerializerMethodField()
    prediction_text = serializers.SerializerMethodField()
    wind_text = serializers.SerializerMethodField()
    pressure_text = serializers.SerializerMethodField()
    moon_text = serializers.SerializerMethodField()

    class Meta:
        model = Predictionten
        fields = '__all__'
        # exclude = ['temperature_min', 'temperature_mean','temperature_max', 'wind_mean','wind_direction','gust_max',
        # 'phenomenon','pressure_min','pressure_max','humidity_mean','uv_index_mean','moon','moon_direction','date','areal','city','fish','prob_min','prob_max']

    def get_temperature_brief(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_temperature_brief(instance.fish)

    def get_temperature_fish(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_temperature_fish(instance.fish)

    def get_temperature_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_temperature_desc(instance.date, instance.fish)

    def get_phenomenon_warning(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_phenomenon_warning(instance.fish)

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

    def get_pressure_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.pressure_ten(instance.date, instance.fish)

    def get_moon_text(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.moon_ten(instance.date, instance.fish)
