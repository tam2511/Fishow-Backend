'''
brief block
'''

brief_text = '''Погодные явления оказывают влияние на клев <strong>{}</strong> по-разному в зависимости от времени года и климата соответствующего региона.  '''

'''
warning block
'''

warning_text = '''На данный момент для определения степени влияния погодных явлений на клев <strong>{}</strong> в данном регионе необходимо больше данных. Вы можете <strong>оставить отчет</strong> о рыбалке в {} и помочь выявить закономерности нашему алгоритму. '''

'''
desc block
'''

extremal_raining = '''В этот день прогнозируется самая дождливая погода за <strong>{}</strong> - <strong>{}</strong>. Возможно резкое изменение клева.'''
extremal_snow = '''В этот день прогнозируется самое большое количество выпавшего снега за <strong>{}</strong> - <strong>{}</strong>. Возможно резкое изменение клева.'''
three_days_hot = '''В этот день и за период <strong>{}</strong> - <strong>{}</strong> наблюдается очень высокая температура воздуха. Это может плохо сказаться на активности рыбы.'''
dull_extremal = '''В этот день и за период <strong>{}</strong> - <strong>{}</strong> в основном наблюдается пасмурная погода. Это может плохо сказаться на солнечной активности рыбы.'''
good_from_hot = '''В этот день возможен дождь и пасмурная погода, что может восстановить активность рыбы в период высокой температуры воздуха с <strong>{}</strong> по <strong>{}</strong>.'''
good_from_bad = '''В этот день возможно улучшение погодных условий по сравнению с периодом <strong>{}</strong> - <strong>{}</strong>. Это может восстановить активность рыбы.'''
neutral = '''В этот день не наблюдается резких изменений погодных условий по сравнению с <strong>{}</strong> - <strong>{}</strong>, которые могут явно влиять на клев рыбы.'''

mark_map = {
    'rain': {
        'небольшой дождь': 1,
        'дождь': 2,
        'сильный дождь': 3,
    },
    'snow': {
        'небольшой снег': 1,
        'снег': 2,
        'сильный снег': 3,
    },
    'dull': {
        'ясно': 0,
        'малооблачно': 0.3,
        'облачно': 0.8,
        'пасмурно': 1.5
    }
}


def check_extra(day, observe, name):
    sum_day = 0
    for _ in day:
        if _ in mark_map[name]:
            sum_day += mark_map[name][_]
        else:
            sum_day += 0
    if sum_day < 6:
        return False
    for day_ in observe:
        temp = 0
        for _ in day_:
            if _ in mark_map[name]:
                temp += mark_map[name][_]
            else:
                temp += 0
        if temp >= sum_day:
            return False
    return True


def check_dull(day, observe):
    days = observe + [day]
    for day_ in days:
        temp = 0
        for _ in day_:
            if _ in mark_map['dull']:
                temp += mark_map['dull'][_]
            else:
                temp += 0
        if temp < 6:
            return False
    return True


def good_from_bad_check(day, observe):
    sum_day = 0
    for _ in day:
        for name in mark_map:
            if _ in mark_map[name]:
                sum_day += mark_map[name][_]
            else:
                sum_day += 0
    if sum_day > 6:
        return False
    for day_ in observe:
        temp = 0
        for _ in day_:
            for name in mark_map:
                if _ in mark_map[name]:
                    temp += mark_map[name][_]
                else:
                    temp += 0
        if temp <= sum_day:
            return False
        if temp < 6:
            return False
    return True


def check_bad_from_hot(day_phen, observe_temp, observe_phen):
    sum_day = 0
    for _ in day_phen:
        for name in mark_map:
            if _ in mark_map[name]:
                sum_day += mark_map[name][_]
            else:
                sum_day += 0
    if sum_day < 6:
        return False
    for i in range(len(observe_temp)):
        temp = sum(observe_temp[i]) / len(observe_temp[i])
        if temp < 20:
            return False
        sum_day = 0
        for _ in observe_phen[i]:
            for name in mark_map:
                if _ in mark_map[name]:
                    sum_day += mark_map[name][_]
                else:
                    sum_day += 0
        if sum_day > 4:
            return False
    return True


def check_hot(day_temps, observe_temps):
    days = observe_temps + [day_temps]
    for day in days:
        temp = sum(day) / len(day)
        if temp < 24:
            return False
    return True


def generate_desc(date, observe_date, day_data, observe_data):
    phenomenons_day = sum([_.split(',') for _ in day_data[1]], [])
    phenomenons_observe = [sum([_.split(',') for _ in observe_data_[1]], []) for observe_data_ in observe_data]
    if check_extra(phenomenons_day, phenomenons_observe, 'rain'):
        return extremal_raining.format(observe_date[-1], observe_date[0])
    if check_extra(phenomenons_day, phenomenons_observe, 'snow'):
        return extremal_raining.format(observe_date[-1], observe_date[0])
    if check_dull(phenomenons_day, phenomenons_observe):
        return dull_extremal.format(observe_date[-1], observe_date[0])
    if good_from_bad_check(phenomenons_day, phenomenons_observe):
        return good_from_bad.format(observe_date[-1], observe_date[0])
    temps_day = sum([list(map(int, _.split(','))) for _ in day_data[0]], [])
    temps_observe = [sum([list(map(int, _.split(','))) for _ in observe_data_[0]], []) for observe_data_ in
                     observe_data]
    if check_bad_from_hot(phenomenons_day, temps_observe, phenomenons_observe):
        return good_from_hot.format(observe_date[-1], observe_date[0])
    if check_hot(temps_day, temps_observe):
        return three_days_hot.format(observe_date[-1], observe_date[0])
    return neutral.format(observe_date[-1], observe_date[0])
