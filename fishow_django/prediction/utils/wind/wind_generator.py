from fishow_django.prediction.utils.helper import *


class WindTextGenerator:
    template_text_one = '''Направление и скорость ветра могу существенно повлиять на клев {}. '''

    template_text_ten = '''Направление и скорость ветра могу существенно повлиять на клев {}. '''

    template_text_fork_one = '''Изменения в направлении и силе воздушных потоков, по нашим прогнозам могут повлиять на клев {}.'''

    template_text_fork_ten = '''Изменения в направлении и силе воздушных потоков, по нашим прогнозам могут повлиять на клев {}.'''

    @staticmethod
    def day_text_generate(data, date, fish):
        '''
        Генерация текста для одного дня для блока воздух на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        influence_time_wind = get_influence_time(data, date, fish, 'wind')
        influence_time_wind_direction = get_influence_time(data, date, fish, 'wind_direction')
        influence_time_gust = get_influence_time(data, date, fish, 'gust')
        influence_time = sorted(influence_time_wind + influence_time_wind_direction + influence_time_gust)
        text_builder = WindTextGenerator.template_text_one.format(cases[fish]['r'])
        if len(influence_time) > 0:
            text_builder += WindTextGenerator.template_text_fork_one.format(
                influence_text_generate(influence_time))
        return text_builder

    @staticmethod
    def ten_day_text_generate(data, date, fish):
        '''
        Генерация текста для девяти суток для блока температура на основе десяти дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        influence_days_wind = get_influence_days(data, date, fish, 'wind')
        influence_days_wind_direction = get_influence_days(data, date, fish, 'wind_direction')
        influence_days_gust = get_influence_days(data, date, fish, 'gust')
        influence_days = sorted(influence_days_wind + influence_days_wind_direction + influence_days_gust)
        text_builder = WindTextGenerator.template_text_ten.format(cases[fish]['r'])
        if len(influence_days) > 0:
            text_builder += WindTextGenerator.template_text_fork_ten.format(
                influence_tendays_text_generate(influence_days))
        return text_builder
