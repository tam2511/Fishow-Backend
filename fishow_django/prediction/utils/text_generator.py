import datetime


def morning_influence(influence_time):
    return (0, 6) in influence_time or (0, 9) in influence_time


def day_influence(influence_time):
    return (0, 12) in influence_time or (0, 15) in influence_time


def evening_influence(influence_time):
    return (0, 18) in influence_time or (0, 21) in influence_time


def night_influence(influence_time):
    return (0, 0) in influence_time or (0, 3) in influence_time


def feature_influence(influence_time):
    return sum([_[0] for _ in influence_time]) > 0


def influence_text_generate(influence_time):
    text_builder = ''
    morning, day, evening, night = morning_influence(influence_time), day_influence(influence_time), evening_influence(
        influence_time), night_influence(influence_time)
    if morning or day or evening or night:
        text_builder += 'сегодня '
        words = []
        if morning:
            words.append('утром')
        if day:
            words.append('днем')
        if evening:
            words.append('вечером')
        if night:
            words.append('ночью')
        if feature_influence(influence_time):
            text_builder += ', '.join(words)
            text_builder += 'и на клев в ближайшие трое суток'
        elif len(words) == 1:
            text_builder += (words[0]) + ''
        else:
            text_builder += ', '.join(words[:-1]) + 'и {}'.format(words[-1])
    else:
        text_builder += 'в ближайшие трое суток'


cases = {
    'щука': {'r': 'щуки'},
    'сом': {'r': 'сома'},
    'судак': {'r': 'судака'},
    'окунь': {'r': 'окуня'},
    'берш': {'r': 'берша'},
    'речная форель': {'r': 'речной форели'},
    'озерная форель': {'r': 'озерной форели'},
    'елец': {'r': 'ельца'},
    'чехонь': {'r': 'чехони'},
    'голавль': {'r': 'голавля'},
    'язь': {'r': 'язя'},
    'карп': {'r': 'карпа'},
    'жерех': {'r': 'жереха'},
    'лещ': {'r': 'леща'},
    'карась': {'r': 'карася'},
    'линь': {'r': 'линя'},
    'пескарь': {'r': 'пескаря'},
    'ротан': {'r': 'ротана'},
    'плотва': {'r': 'плотвы'},
    'красноперка': {'r': 'красноперки'},
    'налим': {'r': 'налима'},
    'густера': {'r': 'густеры'},
    'амур': {'r': 'амура'},
    'ерш': {'r': 'ерша'},
    'сазан': {'r': 'сазана'},
    'подуст': {'r': 'подуста'},
    'толстолобик': {'r': 'толстолобика'},
    'вобла': {'r': 'воблы'},
}


class TextGenerator:
    '''
    Статический класс для генерации контента для 1 дня. Оптимизирован для запросов по полю time.
    '''
    current_city = None
    current_areal = None

    @staticmethod
    def check_current_stage(city, areal):
        return TextGenerator.current_city == city and TextGenerator.current_areal == areal

    @staticmethod
    def update_stage(city, areal):
        TextGenerator.current_city = city
        TextGenerator.current_areal = areal

    @staticmethod
    def day_temperature_text_generate(data, date, fish):
        '''
        Генерация текста для одного дня для блока температура на основе 1-3 дневного прогноза.
        :param data: Список строк из базы данных для фиксированной местности
        :param date: Текущая дата
        :param fish: Текущий вид рыбы
        :return: Текст
        '''
        observe_dates = [date - datetime.timedelta(days=day) for day in range(4)]
        filtred_data = {observe_date: [(eval(_.feature), _.temperature, _.time) for _ in data if
                                       _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
        influence = []
        for index, observe_date in enumerate(observe_dates):
            explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
            for features, temperature, time in explain_prediction:
                for feature, value, weight in features:
                    feature_name, day_shift, time_shift = feature
                    if 0 <= index * 24 + time - (day_shift * 24 + time_shift) < 24 and feature_name == 'temperature':
                        influence.append((index, time, weight, value))
        influence = sorted(influence)
        influence_time = [(_[0], _[1]) for _ in influence]
        text_builder = '''Как правило, температура воздуха несильно влияет на клев {}. 
        Это можно объяснить тем, что есть факторы, которые влияют на клев более существенно.'''.format(cases[fish]['r'])
        if len(influence_time) > 0:
            text_builder += '''Однако, по нашим прогнозам изменения температуры воздуха за сегодня могут
             повлиять на клев {}.'''.format(influence_text_generate(influence_time))
        ...
        return text_builder
