'''
brief block
'''

not_influence_text = '''Температура воздуха оказывает значительное влияние на клев в случае резких перепадов температуры. В случае небольших изменений температуры воздуха при прогнозе клева <strong>{}</strong> учитывается влияние других факторов. '''

influence_text = '''Для <strong>{}</strong> даже несильные колебания температуры воздуха могут повлиять на ее клев. Наш алгоритм прогноза учитывает это. '''

'''
fish block
'''

pos_neg_fish = '''На <strong>{}</strong> положительно влияет {} температуры воздуха, а ее {} способствует уменьшению активности рыбы. '''

pos_fish = '''{} температуры воздуха благоприятно влияет на клев <strong>{}</strong>. '''

neg_fish = '''{} температуры воздуха может негативно повлиять на клев <strong>{}</strong>. '''

none_fish = '''На данный момент недостаточно изучено, как именно влияет изменения температуры воздуха на клев <strong>{}</strong>. '''

'''
desc block
'''

hard_low_desc = '''<strong>{}</strong> ожидается резкое <span class="blue strong">понижение</span> температуры воздуха. '''

hard_up_desc = '''<strong>{}</strong> прогнозируется резкое <span class="red strong">повышение</span> температуры воздуха. '''

hard_no_desc = '''За период <strong>{}</strong> резких перепадов температуры не ожидается. '''

minmax_desc = '''Минимальная температура воздуха в течение дня - <span class="blue strong">{}</span>, максимальная - <span class="red strong">{}</span>. '''

ten_minmax_desc = '''<strong>{}</strong> прогнозируется минимальная температура воздуха - <span class="blue strong">{}</span>, а <strong>{}</strong> ожидается максимальная - <span class="red strong">{}</span>. '''

'''
utils
'''

brief_dict = {
    'Щука': not_influence_text,
    'Сом': not_influence_text,
    'Судак': not_influence_text,
    'Окунь': not_influence_text,
    'Берш': not_influence_text,
    'Речная форель': influence_text,
    'Озерная форель': influence_text,
    'Елец': not_influence_text,
    'Чехонь': influence_text,
    'Голавль': not_influence_text,
    'Язь': not_influence_text,
    'Карп': not_influence_text,
    'Жерех': not_influence_text,
    'Лещ': not_influence_text,
    'Карась': not_influence_text,
    'Линь': not_influence_text,
    'Пескарь': not_influence_text,
    'Ротан': not_influence_text,
    'Плотва': not_influence_text,
    'Красноперка': not_influence_text,
    'Налим': influence_text,
    'Густера': not_influence_text,
    'Амур': influence_text,
    'Ерш': not_influence_text,
    'Сазан': not_influence_text,
    'Подуст': not_influence_text,
    'Толстолобик': influence_text,
    'Вобла': not_influence_text,
    'Хариус': not_influence_text
}

from ..helper.date import get_dates_by_intervals


def hard_dates(temperatures, dates, tag):
    subs = []
    for i in range(1, len(temperatures)):
        subs.append(temperatures[i] - temperatures[i - 1])
    if tag == 'low':
        mask_subs = [1 if sub <= -5 else 0 for sub in subs]
    elif tag == 'up':
        mask_subs = [1 if sub >= 5 else 0 for sub in subs]
    if sum(mask_subs) == 0:
        return None
    intervals = []
    current = [-1, -1]
    max_sub = 0
    for i in range(len(mask_subs)):
        if mask_subs[i]:
            max_sub = max(max_sub, abs(subs[i]))
            if current[0] == -1:
                current[0] = i
            current[1] = i + 1
        else:
            if not current[0] == -1:
                intervals.append((max_sub, (current[0], current[1])))
                max_sub = 0
            current[0] = -1
    if not current[0] == -1:
        intervals.append((max_sub, (current[0], current[1])))
    if len(intervals) == 0:
        return None
    top_interval = [max(intervals, key=lambda x: x[0])[1]]
    return get_dates_by_intervals(dates, top_interval)
