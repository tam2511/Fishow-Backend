from ..helper.extra import *
from ..helper.date import *
from ..helper.text import *
LOWER_BOUND = 0.3
UPPER_BOUND = 0.7


class PredictTextGenerator:
    template_text_one = '''Наша модель прогноза обучается и предсказывает для каждого вида рыб по-своему, в частности,
     для {}.'''

    template_text_ten = ''''Наша модель прогноза обучается и предсказывает для каждого вида рыб по-своему, в частности,
     для {}.'''

    template_text_negative_fork_one = '''Плохо будет клевать {}.'''

    template_text_positive_fork_one = '''Хорошо будет клевать {}.'''

    template_text_negative_fork_ten = '''Плохо будет клевать {}.'''

    template_text_positive_fork_ten = '''Хорошо будет клевать {}.'''

    @staticmethod
    def day_text_generate(data, date, fish):
        '''
        Генерация текста для одного дня для блока температура на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        influence_low, influence_up = get_influence_time_prob(data, date, fish, LOWER_BOUND, UPPER_BOUND)
        text_builder = PredictTextGenerator.template_text_one.format(cases[fish]['r'])
        if len(influence_low) > 0:
            text_builder += PredictTextGenerator.template_text_negative_fork_one.format(
                influence_text_generate(influence_low))
        if len(influence_up) > 0:
            text_builder += PredictTextGenerator.template_text_positive_fork_one.format(
                influence_text_generate(influence_up))
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
        influence_low, influence_up = get_influence_days_prob(data, date, fish, LOWER_BOUND, UPPER_BOUND)
        text_builder = PredictTextGenerator.template_text_ten.format(cases[fish]['r'])
        if len(influence_low) > 0:
            text_builder += PredictTextGenerator.template_text_negative_fork_one.format(
                influence_text_generate(influence_low))
        if len(influence_up) > 0:
            text_builder += PredictTextGenerator.template_text_positive_fork_one.format(
                influence_text_generate(influence_up))
        return text_builder
