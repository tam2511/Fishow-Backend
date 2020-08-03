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
    prediction_brief = serializers.SerializerMethodField()
    prediction_desc = serializers.SerializerMethodField()
    wind_fish = serializers.SerializerMethodField()
    wind_desc = serializers.SerializerMethodField()
    pressure_fish = serializers.SerializerMethodField()
    pressure_desc = serializers.SerializerMethodField()
    moon_desc = serializers.SerializerMethodField()

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
        return TextGenerator.get_day_phenomenon_warning(instance.areal, instance.fish)

    def get_prediction_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_prediction_desc(instance.date, instance.fish)

    def get_prediction_brief(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_prediction_brief(instance.date, instance.fish)

    def get_wind_fish(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_wind_fish(instance.fish)

    def get_wind_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_wind_desc(instance.date, instance.fish)

    def get_pressure_fish(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_pressure_fish(instance.fish)

    def get_pressure_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_pressure_desc(instance.date, instance.fish)

    def get_moon_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_moon_desc(instance.date, instance.fish)


class PredictiontenSerializer(serializers.ModelSerializer):
    temperature_brief = serializers.SerializerMethodField()
    temperature_fish = serializers.SerializerMethodField()
    temperature_desc = serializers.SerializerMethodField()
    phenomenon_warning = serializers.SerializerMethodField()
    prediction_brief = serializers.SerializerMethodField()
    prediction_desc = serializers.SerializerMethodField()
    wind_fish = serializers.SerializerMethodField()
    wind_desc = serializers.SerializerMethodField()
    pressure_fish = serializers.SerializerMethodField()
    pressure_desc = serializers.SerializerMethodField()
    moon_desc = serializers.SerializerMethodField()

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
        return TextGenerator.get_tenday_phenomenon_warning(instance.areal, instance.fish)

    def get_prediction_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_prediction_desc(instance.date, instance.fish)

    def get_prediction_brief(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_prediction_brief(instance.date, instance.fish)

    def get_wind_fish(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_wind_fish(instance.fish)

    def get_wind_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_wind_desc(instance.date, instance.fish)

    def get_pressure_fish(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_pressure_fish(instance.fish)

    def get_pressure_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_pressure_desc(instance.date, instance.fish)

    def get_moon_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_moon_desc(instance.date, instance.fish)
