from .temperature.temperature_generator import TemperatureTextGenerator
from .phenomenon.phenomenon_generator import PhenomenonTextGenerator
from .prediction.prediction_generator import PredictTextGenerator
from .wind.wind_generator import WindTextGenerator
from .pressure.pressure_generator import PressureTextGenerator
from .moon.moon_generator import MoonTextGenerator
from .uv_index.uv_index_generator import UVIndexTextGenerator

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

    '''
    Температура
    '''

    @staticmethod
    def get_day_temperature_brief(fish):
        return TemperatureTextGenerator.get_day_brief(fish)

    @staticmethod
    def get_tenday_temperature_brief(fish):
        return TemperatureTextGenerator.get_tenday_brief(fish)

    @staticmethod
    def get_day_temperature_fish(fish):
        return TemperatureTextGenerator.get_day_fish(fish)

    @staticmethod
    def get_tenday_temperature_fish(fish):
        return TemperatureTextGenerator.get_tenday_fish(fish)

    @staticmethod
    def get_day_temperature_desc(date, fish):
        return TemperatureTextGenerator.get_day_desc(TextGenerator.data, date, fish)

    @staticmethod
    def get_tenday_temperature_desc(date, fish):
        return TemperatureTextGenerator.get_tenday_desc(TextGenerator.data, date, fish)

    '''
    Погодные явления
    '''

    @staticmethod
    def get_day_phenomenon_warning(areal, fish):
        return PhenomenonTextGenerator.get_warning(areal, fish)

    @staticmethod
    def get_tenday_phenomenon_warning(areal, fish):
        return PhenomenonTextGenerator.get_warning(areal, fish)

    '''
    Прогноз
    '''

    @staticmethod
    def get_day_prediction_brief(date, fish):
        return PredictTextGenerator.get_day_brief(date, fish)

    @staticmethod
    def get_tenday_prediction_brief(date, fish):
        return PredictTextGenerator.get_tenday_brief(date, fish)

    @staticmethod
    def get_day_prediction_desc(date, fish):
        return PredictTextGenerator.get_day_desc(TextGenerator.data, date, fish)

    @staticmethod
    def get_tenday_prediction_desc(date, fish):
        return PredictTextGenerator.get_tenday_desc(TextGenerator.data, date, fish)

    '''
    Ветер
    '''

    @staticmethod
    def get_day_wind_fish(fish):
        return WindTextGenerator.get_day_fish(fish)

    @staticmethod
    def get_tenday_wind_fish(fish):
        return WindTextGenerator.get_tenday_fish(fish)

    @staticmethod
    def get_day_wind_desc(date, fish):
        return WindTextGenerator.get_day_desc(TextGenerator.data, date, fish)

    @staticmethod
    def get_tenday_wind_desc(date, fish):
        return WindTextGenerator.get_tenday_desc(TextGenerator.data, date, fish)

    @staticmethod
    def get_day_wind_roza(date, fish):
        return WindTextGenerator.get_day_wind_roza(TextGenerator.data, date, fish)

    @staticmethod
    def get_tenday_wind_roza(date, fish):
        return WindTextGenerator.get_wind_roza(TextGenerator.data, date, fish)

    '''
    Давление
    '''

    @staticmethod
    def get_day_pressure_fish(fish):
        return PressureTextGenerator.get_day_fish(fish)

    @staticmethod
    def get_day_pressure_desc(date, fish):
        return PressureTextGenerator.get_day_desc(TextGenerator.data, date, fish)

    @staticmethod
    def get_tenday_pressure_fish(fish):
        return PressureTextGenerator.get_tenday_fish(fish)

    @staticmethod
    def get_tenday_pressure_desc(date, fish):
        return PressureTextGenerator.get_tenday_desc(TextGenerator.data, date, fish)

    '''
    Луна
    '''

    @staticmethod
    def get_day_moon_desc(date, fish):
        return MoonTextGenerator.get_day_desc(TextGenerator.data, date, fish)

    @staticmethod
    def get_tenday_moon_desc(date, fish):
        return MoonTextGenerator.get_tenday_desc(TextGenerator.data, date, fish)

    '''
    Ультрафиолетовый индекс
    '''

    @staticmethod
    def get_tenday_uv_index_desc(date, fish):
        return UVIndexTextGenerator.get_tenday_desc(TextGenerator.data, date, fish)
