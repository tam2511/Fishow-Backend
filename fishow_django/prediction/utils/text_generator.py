from .temperature_generator import TemperatureTextGenerator

class TextGenerator:
    '''
    Статический класс для генерации контента для 1 дня. Оптимизирован для запросов по полю time.
    '''
    current_city = None
    current_areal = None

    @staticmethod
    def update_stage(city, areal):
        TextGenerator.current_city = city
        TextGenerator.current_areal = areal

    @staticmethod
    def check_stage(city, areal):
        return TextGenerator.current_city == city and TextGenerator.current_areal == areal

    @staticmethod
    def temperature_one(data, date, fish):
        return TemperatureTextGenerator.day_temperature_text_generate(data, date, fish)

    @staticmethod
    def temperature_ten(data, date, fish):
        return TemperatureTextGenerator.ten_day_temperature_text_generate(data, date, fish)
