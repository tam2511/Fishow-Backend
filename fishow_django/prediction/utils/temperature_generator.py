from .helper import *


class TemperatureTextGenerator:
    template_text_one = '''Как правило, температура воздуха несильно влияет на клев {}. 
        Это можно объяснить тем, что есть факторы, которые влияют на клев более существенно.'''

    template_text_ten = '''Как правило, температура воздуха несильно влияет на клев {}. 
            Это можно объяснить тем, что есть факторы, которые влияют на клев более существенно.'''

    template_text_fork_one = '''Однако, по нашим прогнозам изменения температуры воздуха за сегодня могут
                 повлиять на клев {}.'''

    template_text_fork_ten = '''Однако, по нашим прогнозам изменения температуры воздуха за сегодня могут
                     повлиять на клев {}.'''

    @staticmethod
    def day_text_generate(data, date, fish):
        '''
        Генерация текста для одного дня для блока температура на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        influence_time = get_influence_time(data, date, fish, 'temperature')
        text_builder = TemperatureTextGenerator.template_text_one.format(cases[fish]['r'])
        if len(influence_time) > 0:
            text_builder += TemperatureTextGenerator.template_text_fork_one.format(
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
        influence_days = get_influence_days(data, date, fish, 'temperature')
        text_builder = TemperatureTextGenerator.template_text_ten.format(cases[fish]['r'])
        if len(influence_days) > 0:
            text_builder += TemperatureTextGenerator.template_text_fork_ten.format(
                influence_tendays_text_generate(influence_days))
        return text_builder
