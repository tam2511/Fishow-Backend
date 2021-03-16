from ..helper.date import parse_date

'''
fish block
'''

pos_neg_fish = '''На данный момент, не известно как именно влияет сила и направление ветра на клев <strong>{}</strong> . Однако, сильный <strong>северный</strong> или <strong>восточный</strong> ветер может испортить рыбалку.'''

'''
desc block
'''

mean_wind_desc = '''Средняя скорость ветра в течение дня - <strong>{}</strong> м/с. Преимущественно <strong>{}</strong> направление ветра. '''

low_wind_desc = '''Возможна безветренная погода в течение дня. Преимущественно <strong>{}</strong> направление ветра.'''

hard_wind_desc = '''Ожидается сильный ветер в течении дня со средней скоростью - <strong>{}</strong> м/с. Преимущественно <strong>{}</strong> направление ветра.'''

ten_minmax_desc = '''<strong>{}</strong> ожидается самая слабая за рассматриваемый период скорость ветра - <strong>{}</strong> м/с, а <strong>{}</strong> возможнен сильный ветер - около <strong>{}</strong> м/с. '''

'''
roza desc block
'''

roza_neutral_day = '''<strong>{}</strong> не наблюдается выраженного глобального направления воздуха. В данном случае клев рыбы от направления ветра не сильно зависит.'''
roza_good_day = '''<strong>{}</strong> преимущeственно наблюдается <span class="red strong">{}</span> направление ветра. Вероятность хорошего клева в этот день <span class="red strong">увеличивается</span>.'''
roza_bad_day = '''<strong>{}</strong> преимущeственно наблюдается <span class="blue strong">{}</span> направление ветра. Вероятность хорошего клева в этот день <span class="blue strong">уменьшается</span>.'''
roza_good_good_day = '''<strong>{}</strong> преимущeственно наблюдается <span class="red strong">{}</span> и <span class="red strong">{}</span> направления ветра. Вероятность хорошего клева в этот день <span class="red strong">увеличивается</span>.'''
roza_good_bad_day = '''<strong>{}</strong> преимущeственно наблюдается <span class="red strong">{}</span> и <span class="blue strong">{}</span> направления ветра. В часы, когда наблюдается <span class="red strong">{}</span> направление ветра вероятность клева <span class="red strong">выше</span>.'''
roza_bad_good_day = '''<strong>{}</strong> преимущeственно наблюдается <span class="blue strong">{}</span> и <span class="red strong">{}</span> направления ветра. В часы, когда наблюдается <span class="red strong">{}</span> направление ветра вероятность клева <span class="red strong">выше</span>.'''
roza_bad_bad_day = '''<strong>{}</strong> преимущeственно наблюдается <span class="blue strong">{}</span> и <span class="blue strong">{}</span> направления ветра. Вероятность хорошего клева в этот день <span class="blue strong">уменьшается</span>.'''

roza_neutral_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> не наблюдается выраженного глобального направления воздуха. В данном случае клев рыбы от направления ветра не сильно зависит.'''
roza_good_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> преимущeственно наблюдается <span class="red strong">{}</span> направление ветра. Вероятность хорошего клева в данный период <span class="red strong">увеличивается</span>.'''
roza_bad_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> преимущeственно наблюдается <span class="blue strong">{}</span> направление ветра. Вероятность хорошего клева в данный период <span class="blue strong">уменьшается</span>.'''
roza_good_good_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> преимущeственно наблюдается <span class="red strong">{}</span> и <span class="red strong">{}</span> направления ветра. Вероятность хорошего клева в данный период <span class="red strong">увеличивается</span>.'''
roza_good_bad_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> преимущeственно наблюдается <span class="red strong">{}</span> и <span class="blue strong">{}</span> направления ветра. В дни, когда наблюдается <span class="red strong">{}</span> направление ветра вероятность клева <span class="red strong">выше</span>.'''
roza_bad_good_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> преимущeственно наблюдается <span class="blue strong">{}</span> и <span class="red strong">{}</span> направления ветра. В дни, когда наблюдается <span class="red strong">{}</span> направление ветра вероятность клева <span class="red strong">выше</span>.'''
roza_bad_bad_tenday = '''За период <strong>{}</strong> - <strong>{}</strong> преимущeственно наблюдается <span class="blue strong">{}</span> и <span class="blue strong">{}</span> направления ветра. Вероятность хорошего клева в данный период <span class="blue strong">уменьшается</span>.'''

'''
utils
'''

wind_cases = {
    'С': 'северное',
    'СЗ': 'северо-западное',
    'З': 'западное',
    'ЮЗ': 'юго-западное',
    'Ю': 'южное',
    'ЮВ': 'юго-восточное',
    'В': 'восточное',
    'СВ': 'северо-восточное',
}

wind_reduce = {
    'С': ('северное'),
    'В': ('восточное'),
    'Ю': ('южное'),
    'З': ('западное'),
    'В,С': ('восточное', 'северное'),
    'В,З': ('восточное', 'западное'),
    'В,Ю': ('восточное', 'южное'),
    'З,С': ('западное', 'северное'),
    'З,Ю': ('западное', 'южное'),
    'С,Ю': ('северное', 'южное'),
}

wind_mark = {
    'С': (0),
    'В': (0),
    'Ю': (1),
    'З': (1),
    'В,С': (0, 0),
    'В,З': (0, 1),
    'В,Ю': (0, 1),
    'З,С': (1, 0),
    'З,Ю': (1, 1),
    'С,Ю': (0, 1),
}


def roza_desc_day(label, date_start):
    date_start = parse_date(date_start)
    if not label in wind_reduce:
        return roza_neutral_day.format(date_start)
    mark = wind_mark[label]
    if len(mark) == 1 and mark[0] == 0:
        return roza_bad_day.format(date_start, wind_reduce[label][0])
    elif len(mark) == 1 and mark[0] == 1:
        return roza_good_day.format(date_start, wind_reduce[label][0])
    elif mark[0] == 0 and mark[1] == 0:
        return roza_bad_bad_day.format(date_start, *wind_reduce[label])
    elif mark[0] == 0 and mark[1] == 1:
        return roza_bad_good_day.format(date_start, *wind_reduce[label], wind_reduce[1])
    elif mark[0] == 1 and mark[1] == 0:
        return roza_good_bad_day.format(date_start, *wind_reduce[label], wind_reduce[0])
    elif mark[0] == 1 and mark[1] == 1:
        return roza_good_good_day.format(date_start, *wind_reduce[label])


def roza_desc_tenday(label, date_start, date_end):
    date_start = parse_date(date_start)
    date_end = parse_date(date_end)
    if not label in wind_reduce:
        return roza_neutral_tenday.format(date_start, date_end)
    mark = wind_mark[label]
    if len(mark) == 1 and mark[0] == 0:
        return roza_bad_tenday.format(date_start, date_end, wind_reduce[label][0])
    elif len(mark) == 1 and mark[0] == 1:
        return roza_good_tenday.format(date_start, date_end, wind_reduce[label][0])
    elif mark[0] == 0 and mark[1] == 0:
        return roza_bad_bad_tenday.format(date_start, date_end, *wind_reduce[label])
    elif mark[0] == 0 and mark[1] == 1:
        return roza_bad_good_tenday.format(date_start, date_end, *wind_reduce[label], wind_reduce[1])
    elif mark[0] == 1 and mark[1] == 0:
        return roza_good_bad_tenday.format(date_start, date_end, *wind_reduce[label], wind_reduce[0])
    elif mark[0] == 1 and mark[1] == 1:
        return roza_good_good_tenday.format(date_start, date_end, *wind_reduce[label])
