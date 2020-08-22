
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
    'щука': not_influence_text,
    'сом': not_influence_text,
    'судак': not_influence_text,
    'окунь': not_influence_text,
    'берш': not_influence_text,
    'речная форель': influence_text,
    'озерная форель': influence_text,
    'елец': not_influence_text,
    'чехонь': influence_text,
    'голавль': not_influence_text,
    'язь': not_influence_text,
    'карп': not_influence_text,
    'жерех': not_influence_text,
    'лещ': not_influence_text,
    'карась': not_influence_text,
    'линь': not_influence_text,
    'пескарь': not_influence_text,
    'ротан': not_influence_text,
    'плотва': not_influence_text,
    'красноперка': not_influence_text,
    'налим': influence_text,
    'густера': not_influence_text,
    'амур': influence_text,
    'ерш': not_influence_text,
    'сазан': not_influence_text,
    'подуст': not_influence_text,
    'толстолобик': influence_text,
    'вобла': not_influence_text
}

from ..helper.date import get_dates_by_intervals

def hard_dates(temperatures, dates, tag):
    subs = []
    for i in range(1, len(temperatures)):
        subs.append(temperatures[i] - temperatures[i - 1])
    if tag == 'low':
        mask_subs = [1 if sub <= -3 else 0 for sub in subs]
    elif tag == 'up':
        mask_subs = [1 if sub >= 3 else 0 for sub in subs]
    if sum(mask_subs) == 0:
        return None
    intervals = []
    current = [-1, -1]
    for i in range(len(mask_subs)):
        if mask_subs[i]:
            if current[0] == -1:
                current[0] = i
            current[1] = i + 1
        else:
            if not current[0] == -1:
                intervals.append((current[0], current[1]))
            current[0] = -1
    if not current[0] == -1:
        intervals.append((current[0], current[1]))
    return get_dates_by_intervals(dates, intervals)