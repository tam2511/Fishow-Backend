from .helper import *


class TemperatureTextGenerator:
    template_text_one = '''Сама по себе температура воздуха несильно влияет на клев рыбы. При резком понижении или повышении температуры прогноз клева может изменится. Это можно объяснить тем, что температура воздуха влияет на клев рыбы косвенно через температуру воды. Поэтому при небольших колебаниях температуры воздуха температура воды не успевает изменится настолько, чтобы повлияет на клев в тот промежуток времени, по которому делается прогноз нашей моделью. '''

    template_text_ten = '''Сама по себе температура воздуха несильно влияет на клев рыбы. При резком понижении или повышении температуры прогноз клева может изменится. Это можно объяснить тем, что температура воздуха влияет на клев рыбы косвенно через температуру воды. Поэтому при небольших колебаниях температуры воздуха температура воды не успевает изменится настолько, чтобы повлияет на клев в тот промежуток времени, по которому делается прогноз нашей моделью. '''

    template_text_pos_influence = '''Наиболее благоприятные условия для ловли {}: *{}* температуры воздуха.'''

    template_text_neg_influence = '''Неблагоприятные условия для ловли {}: *{}* температуры воздуха.'''

    template_text_fork_one = '''По нашим прогнозом, изменения температуры воздуха за {} может повлиять на клев {} {}.'''

    template_text_fork_ten = '''По нашим прогнозом, изменения температуры воздуха наиболее сильно повлияют на клев {} {}.'''

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
        text_builder = TemperatureTextGenerator.template_text_one
        if cases[fish]['temperature+']:
            text_builder += TemperatureTextGenerator.template_text_pos_influence.format(cases[fish]['r'],
                                                                                        cases[fish]['temperature+'])
        if cases[fish]['temperature-']:
            text_builder += TemperatureTextGenerator.template_text_neg_influence.format(cases[fish]['r'],
                                                                                        cases[fish]['temperature-'])
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
        text_builder = TemperatureTextGenerator.template_text_ten
        if cases[fish]['temperature+']:
            text_builder += TemperatureTextGenerator.template_text_pos_influence.format(cases[fish]['r'],
                                                                                        cases[fish]['temperature+'])
        if cases[fish]['temperature-']:
            text_builder += TemperatureTextGenerator.template_text_neg_influence.format(cases[fish]['r'],
                                                                                        cases[fish]['temperature-'])
        if len(influence_days) > 0:
            text_builder += TemperatureTextGenerator.template_text_fork_ten.format(
                influence_tendays_text_generate(influence_days))
        return text_builder
