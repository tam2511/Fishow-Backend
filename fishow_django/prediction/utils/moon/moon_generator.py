from fishow_django.prediction.utils.helper import *


class MoonTextGenerator:
    template_text_one = '''Лунные фазы можно назвать важнейшим показателем при построении прогноза клева. Для {} этот показатель очень важен. '''

    template_text_ten = '''Лунные фазы можно назвать важнейшим показателем при построении прогноза клева. Для {} этот показатель очень важен. '''

    template_text_fork_one = '''Фаза луны влияет на клев всегда, на прогноз нашей модели она повлияла {}.'''

    template_text_fork_ten = '''Фаза луны влияет на клев всегда, на прогноз нашей модели она повлияла {}.'''

    @staticmethod
    def day_text_generate(data, date, fish):
        '''
        Генерация текста для одного дня для блока температура на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        influence_time_moon_direction = get_influence_days(data, date, fish, 'moon_direction')
        influence_time_moon = get_influence_days(data, date, fish, 'moon')
        influence_time = sorted(influence_time_moon + influence_time_moon_direction)
        text_builder = MoonTextGenerator.template_text_one.format(cases[fish]['r'])
        if len(influence_time) > 0:
            text_builder += MoonTextGenerator.template_text_fork_one.format(
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
        influence_days_moon_direction = get_influence_days(data, date, fish, 'moon_direction')
        influence_days_moon = get_influence_days(data, date, fish, 'moon')
        influence_days = sorted(influence_days_moon + influence_days_moon_direction)
        text_builder = MoonTextGenerator.template_text_ten.format(cases[fish]['r'])
        if len(influence_days) > 0:
            text_builder += MoonTextGenerator.template_text_fork_ten.format(
                influence_tendays_text_generate(influence_days))
        return text_builder
