'''
desc block
'''

brief_text = '''Прогноз клева <strong>{}</strong> рассчитан на основе всех погодных факторов за <strong>{}</strong>. Если вероятность клева в интересующее Вас время больше 70%, то клев считается хорошим, если вероятность меньше 30%, то клев считается плохим, иначе клев является умеренный и успех рыбалки во многом зависит от вашего мастерства. '''

minmax_day_text = '''<strong>{}</strong> лучшее время для ловли <strong>{}</strong> <strong>{}</strong> с вероятностью клева - <span class="red strong">{}</span>. А <strong>{}</strong> ожидается наименьшая вероятность клева - <span class="blue strong">{}</span>. '''

minmax_tenday_text = '''<span class="red strong">{}</span> по нашим прогнозам ожидается лучший клев <strong>{}</strong>, вероятность клева в этот день - <strong>{}</strong>. А <span class="blue strong">{}</span> прогнозируется самый плохой клев рыбы с вероятностью клева - <strong>{}</strong>. '''

time_map = {
    0: 0,
    3: 0,
    6: 1,
    9: 1,
    12: 2,
    15: 2,
    18: 3,
    21: 3
}

text_map = {
    0: 'ночью',
    1: 'утром',
    2: 'днем',
    3: 'вечером'
}

from ..helper.date import parse_date

def get_day_date_times(date, times):
    times_keys = list(set([time_map[_] for _ in times]))
    date_text = parse_date(date)
    if len(times_keys) == 1:
        return '{} {}'.format(text_map[times_keys[0]], date_text)
    if len(times_keys) == 2:
        return '{} и {} {}'.format(text_map[times_keys[0]], text_map[times_keys[1]], date_text)
    else:
        temp_text = ', '.format([text_map[_] for _ in times_keys[:-1]]) + ' и {}'.format(text_map[times_keys[-1]])
        return '{} {}'.format(temp_text, date_text)

def get_day_times(times):
    times_keys = list(set([time_map[_] for _ in times]))
    if len(times_keys) == 1:
        return '{}'.format(text_map[times_keys[0]])
    if len(times_keys) == 2:
        return '{} и {}'.format(text_map[times_keys[0]], text_map[times_keys[1]])
    else:
        temp_text = ', '.format([text_map[_] for _ in times_keys[:-1]]) + ' и {}'.format(text_map[times_keys[-1]])
        return '{}'.format(temp_text)

def get_time_text(date, time):
    date_text = parse_date(date)
    time_text = text_map[time_map[time]]
    return '{}, {}'.format(date_text, time_text)

def get_date_time_text(date, time):
    date_text = parse_date(date)
    return '{}, {}'.format(date_text, time)
