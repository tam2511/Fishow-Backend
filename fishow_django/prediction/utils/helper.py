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


def parse_date(date):
    date = date.split('.')
    day = date[0]
    month = date[1]
    month_map = {
        '1': 'января', '2': 'февраля', '3': 'марта',
        '4': 'апреля', '5': 'мая', '6': 'июня',
        '7': 'июля', '8': 'августа', '9': 'сентября',
        '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    return '{} {}'.format(day, month_map[month])


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
    return text_builder


def influence_tendays_text_generate(influence_time):
    days = list(set(influence_time))
    if len(days) == 1:
        return parse_date(days[0])
    return ', '.join([parse_date(_) for _ in days[:-1]]) + ' и {}'.format(parse_date(days[-1]))


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


def get_influence_time(data, date, fish, target_feature_name):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(4)]
    filtred_data = {observe_date: [(eval(_.features), _.temperature, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for features, temperature, time in explain_prediction:
            for feature, value, weight in features:
                feature_name, day_shift, time_shift = feature
                if 0 <= index * 24 + time - (day_shift * 24 + time_shift) < 24 and feature_name == target_feature_name:
                    influence.append((index, time, weight, value))
    influence = sorted(influence)
    return [(_[0], _[1]) for _ in influence]


def get_influence_days(data, date, fish, target_feature_name):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
    filtred_data = {observe_date: [(eval(_.features), _.temperature, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for features, temperature, time in explain_prediction:
            for feature, value, weight in features:
                feature_name, day_shift, time_shift = feature
                if 0 <= index * 24 + time - (day_shift * 24 + time_shift) < 24 and feature_name == target_feature_name:
                    influence.append((observe_date, time, weight, value))
    return list(set([_[0] for _ in influence]))


def get_influence_time_prob(data, date, fish, lower_bound, upper_bound):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(4)]

    filtred_data = {observe_date: [(_.prob, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence_low = []
    influence_up = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for prob, time in explain_prediction:
            if prob < lower_bound:
                influence_low.append((index, time))
            if prob > upper_bound:
                influence_up.append((index, time))
    influence_low = sorted(influence_low)
    influence_up = sorted(influence_up)
    return influence_low, influence_up


def get_influence_days_prob(data, date, fish, lower_bound, upper_bound):
    observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
    filtred_data = {observe_date: [(_.prob, _.time) for _ in data if
                                   _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
    influence_low = []
    influence_up = []
    for index, observe_date in enumerate(observe_dates):
        explain_prediction = sorted(filtred_data[observe_date], key=lambda x: x[-1])
        for prob, time in explain_prediction:
            if prob < lower_bound:
                influence_low.append((observe_date))
            if prob > upper_bound:
                influence_up.append((observe_date))
    influence_low = sorted(influence_low)
    influence_up = sorted(influence_up)
    return list(set(influence_low)), list(set(influence_up))
