class DayTextGenerator:
    '''
    Статический класс для генерации контента для 1 дня. Оптимизирован для запросов по полю time.
    '''
    current_city = None
    current_areal = None
    current_fish = None
    current_date = None

    @staticmethod
    def check_current_stage(city, areal, fish, date):
        return DayTextGenerator.current_city == city and DayTextGenerator.current_areal == areal \
               and DayTextGenerator.current_fish == fish and DayTextGenerator.current_date == date

    @staticmethod
    def update_stage(city, areal, fish, date):
        DayTextGenerator.current_city = city
        DayTextGenerator.current_areal = areal
        DayTextGenerator.current_fish = fish
        DayTextGenerator.current_date = date

    @staticmethod
    def temperature_text_generate(data):
        '''
        Генерация текста для блока температура на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности, начиная с current_date
        до current_date + min(3, max - current_data)
        :return: Текст
        '''
        predictions = [(_.prob, _.feature) for _ in data]
        temperatures = [_.temperature for _ in data]
        return 'example'
