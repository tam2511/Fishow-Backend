from fishow_django.prediction.utils.helper import *


class PressureTextGenerator:
    template_text_one = '''Давление является одним из самых важных показателей для определения прогноза клева {}. '''

    template_text_ten = '''Давление является одним из самых важных показателей для определения прогноза клева {}. '''

    template_text_fork_one = '''Колебания давления может повлиять на клева {}.'''

    template_text_fork_ten = '''Колебания давления может повлиять на клева {}.'''

    @staticmethod
    def day_text_generate(data, date, fish):
        '''
        Генерация текста для одного дня для блока температура на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        influence_time = get_influence_time(data, date, fish, 'pressure')
        text_builder = PressureTextGenerator.template_text_one.format(cases[fish]['r'])
        if len(influence_time) > 0:
            text_builder += PressureTextGenerator.template_text_fork_one.format(
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
        influence_days = get_influence_days(data, date, fish, 'pressure')
        text_builder = PressureTextGenerator.template_text_ten.format(cases[fish]['r'])
        if len(influence_days) > 0:
            text_builder += PressureTextGenerator.template_text_fork_ten.format(
                influence_tendays_text_generate(influence_days))
        return text_builder
