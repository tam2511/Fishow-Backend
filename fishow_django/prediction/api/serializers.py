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
    wind_roza = serializers.SerializerMethodField()
    wind_roza_desc = serializers.SerializerMethodField()
    uv_index_desc = serializers.SerializerMethodField()
    temperature = serializers.SerializerMethodField()
    wind = serializers.SerializerMethodField()
    gust = serializers.SerializerMethodField()
    pressure = serializers.SerializerMethodField()
    humidity = serializers.SerializerMethodField()
    uv_index = serializers.SerializerMethodField()
    prob = serializers.SerializerMethodField()
    wind_direction = serializers.SerializerMethodField()
    phenomenon = serializers.SerializerMethodField()

    class Meta:
        model = Prediction
        fields = '__all__'
        # fields = ['moon','moon_direction','date','areal','city','fish','sun_up','sun_down',]
        # exclude = ['time', 'temperature','wind', 'wind_direction','gust','phenomenon',
        # 'pressure','humidity','uv_index','moon','moon_direction','day','date','areal','city','prob','fish','features']

    def get_temperature(self, instance):
        return list(map(int, instance.temperature.replace('+', '').split(',')))

    def get_wind(self, instance):
        return list(map(int, instance.wind.split(',')))

    def get_gust(self, instance):
        return list(map(int, instance.gust.split(',')))

    def get_pressure(self, instance):
        return list(map(int, instance.pressure.split(',')))

    def get_humidity(self, instance):
        return list(map(int, instance.humidity.split(',')))

    def get_uv_index(self, instance):
        return list(map(int, instance.uv_index.split(',')))

    def get_prob(self, instance):
        return list(map(int, instance.prob.split(',')))

    def get_wind_direction(self, instance):
        return instance.wind_direction.split(',')

    def get_phenomenon(self, instance):
        return [_.replace('.', ',') for _ in instance.phenomenon.split(',')]

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

    def get_wind_roza(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_wind_roza(instance.date, instance.fish)

    def get_wind_roza_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_wind_roza_desc(instance.date, instance.fish, self.get_wind_roza(instance))

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

    def get_uv_index_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_day_uv_index_desc(instance.date, instance.fish)


class PredictiontenSerializer(serializers.ModelSerializer):
    temperature_min = serializers.SerializerMethodField()
    temperature_max = serializers.SerializerMethodField()
    wind_mean = serializers.SerializerMethodField()
    wind_direction = serializers.SerializerMethodField()
    gust_max = serializers.SerializerMethodField()
    phenomenon = serializers.SerializerMethodField()
    pressure_min = serializers.SerializerMethodField()
    pressure_max = serializers.SerializerMethodField()
    humidity_mean = serializers.SerializerMethodField()
    uv_index_mean = serializers.SerializerMethodField()
    moon = serializers.SerializerMethodField()
    moon_direction = serializers.SerializerMethodField()
    prob_min = serializers.SerializerMethodField()
    prob_max = serializers.SerializerMethodField()
    prob_mean = serializers.SerializerMethodField()
    temperature_brief = serializers.SerializerMethodField()
    temperature_fish = serializers.SerializerMethodField()
    temperature_desc = serializers.SerializerMethodField()
    phenomenon_warning = serializers.SerializerMethodField()
    prediction_brief = serializers.SerializerMethodField()
    prediction_desc = serializers.SerializerMethodField()
    wind_fish = serializers.SerializerMethodField()
    wind_desc = serializers.SerializerMethodField()
    wind_roza = serializers.SerializerMethodField()
    wind_roza_desc = serializers.SerializerMethodField()
    pressure_fish = serializers.SerializerMethodField()
    pressure_desc = serializers.SerializerMethodField()
    moon_desc = serializers.SerializerMethodField()
    uv_index_desc = serializers.SerializerMethodField()

    class Meta:
        model = Predictionten
        fields = '__all__'
        # exclude = ['temperature_min', 'temperature_mean','temperature_max', 'wind_mean','wind_direction','gust_max',
        # 'phenomenon','pressure_min','pressure_max','humidity_mean','uv_index_mean','moon','moon_direction','date','areal','city','fish','prob_min','prob_max']

    def get_temperature_min(self, instance):
        return list(map(int, instance.temperature_min.replace('+', '').split(',')))

    def get_temperature_max(self, instance):
        return list(map(int, instance.temperature_max.replace('+', '').split(',')))

    def get_wind_mean(self, instance):
        return list(map(int, instance.wind_mean.split(',')))

    def get_wind_direction(self, instance):
        return instance.wind_direction.split(',')

    def get_gust_max(self, instance):
        return list(map(int, instance.gust_max.split(',')))

    def get_phenomenon(self, instance):
        return [_.replace('.', ',') for _ in instance.phenomenon.split(',')]

    def get_pressure_min(self, instance):
        return list(map(int, instance.pressure_min.split(',')))

    def get_pressure_max(self, instance):
        return list(map(int, instance.pressure_max.split(',')))

    def get_humidity_mean(self, instance):
        return list(map(int, instance.humidity_mean.split(',')))

    def get_uv_index_mean(self, instance):
        return list(map(int, instance.uv_index_mean.split(',')))

    def get_moon(self, instance):
        return list(map(int, instance.moon.split(',')))

    def get_moon_direction(self, instance):
        return list(map(int, instance.moon_direction.split(',')))

    def get_prob_min(self, instance):
        return list(map(int, instance.prob_min.split(',')))

    def get_prob_max(self, instance):
        return list(map(int, instance.prob_max.split(',')))

    def get_prob_mean(self, instance):
        return list(map(int, map(float, instance.prob_mean.split(','))))

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

    def get_wind_roza(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_wind_roza(instance.date, instance.fish)

    def get_wind_roza_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_wind_roza_desc(instance.date, instance.fish, self.get_wind_roza(instance))

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

    def get_uv_index_desc(self, instance):
        if not TextGenerator.check_stage(instance.city, instance.areal):
            data = Prediction.objects.filter(city=instance.city, areal=instance.areal)
            TextGenerator.set_data(data)
            TextGenerator.update_stage(instance.city, instance.areal)
        return TextGenerator.get_tenday_uv_index_desc(instance.date, instance.fish)
