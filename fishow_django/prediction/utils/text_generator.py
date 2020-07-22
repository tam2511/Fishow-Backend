from fishow_django.prediction.utils.temperature.temperature_generator import TemperatureTextGenerator
from fishow_django.prediction.utils.phenomenon.phenomenon_generator import PhenomenonTextGenerator
from fishow_django.prediction.utils.prediction.prediction_generator import PredictTextGenerator
from fishow_django.prediction.utils.wind.wind_generator import WindTextGenerator
from fishow_django.prediction.utils.pressure.pressure_generator import PressureTextGenerator
from fishow_django.prediction.utils.moon.moon_generator import MoonTextGenerator

class TextGenerator:
    '''
    Статический класс для генерации контента для 1 дня. Оптимизирован для запросов по полю time.
    '''
    current_city = None
    current_areal = None
    data = None

    @staticmethod
    def update_stage(city, areal):
        TextGenerator.current_city = city
        TextGenerator.current_areal = areal

    @staticmethod
    def check_stage(city, areal):
        return TextGenerator.current_city == city and TextGenerator.current_areal == areal

    @staticmethod
    def set_data(data):
        TextGenerator.data = data

    @staticmethod
    def get_temperature_brief(date, fish):
        return TemperatureTextGenerator

    @staticmethod
    def temperature_one(date, fish):
        return TemperatureTextGenerator.day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def temperature_ten(date, fish):
        return TemperatureTextGenerator.ten_day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def phenomenon_one(date, fish):
        return PhenomenonTextGenerator.day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def phenomenon_ten(date, fish):
        return PhenomenonTextGenerator.ten_day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def prediction_one(date, fish):
        return PredictTextGenerator.day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def prediction_ten(date, fish):
        return PredictTextGenerator.ten_day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def wind_one(date, fish):
        return WindTextGenerator.day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def wind_ten(date, fish):
        return WindTextGenerator.ten_day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def pressure_one(date, fish):
        return PressureTextGenerator.day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def pressure_ten(date, fish):
        return PressureTextGenerator.ten_day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def moon_one(date, fish):
        return MoonTextGenerator.day_text_generate(TextGenerator.data, date, fish)

    @staticmethod
    def moon_ten(date, fish):
        return MoonTextGenerator.ten_day_text_generate(TextGenerator.data, date, fish)
