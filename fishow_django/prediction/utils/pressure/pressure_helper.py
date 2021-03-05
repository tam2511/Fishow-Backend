'''
fish block
'''

pos_neg_fish = '''На <strong>{}</strong> положительно влияет {} атмосферного давления, а его {} может негативно повлиять на активность рыбы. '''

pos_fish = '''{} атмосферного давления благоприятно влияет на клев <strong>{}</strong>. '''

neg_fish = '''{} атмосферного давления может негативно повлиять на клев <strong>{}</strong>. '''

none_fish = '''На данный момент недостаточно изучено, как именно влияет изменения атмосферного давления на клев <strong>{}</strong>. '''

'''
desc block
'''

hard_low_desc = '''<strong>{}</strong> ожидается резкий <span class="blue strong">спад</span> атмосферного давления. '''

hard_low_desc_no = '''<strong>{}</strong> резких <span class="blue strong">спадов</span> атмосферного давления не ожидается. '''

hard_up_desc = '''<strong>{}</strong> прогнозируется резкий <span class="red strong">рост</span> атмосферного давления. '''

hard_up_desc_no = '''За период <strong>{}</strong> резкого <span class="blue strong">роста</span> атмосферного давления не прогнозируется. '''

minmax_desc = '''Минимальное значение атмосферного давления в течение - <span class="blue strong">{}</span>, максимальное - <span class="red strong">{}</span>. '''

ten_minmax_desc = '''<strong>{}</strong> прогнозируется минимальное значение атмосферного давления - <span class="blue strong">{}</span>, а <strong>{}</strong> ожидается максимальная - <span class="red strong">{}</span>. '''


'''
utils
'''

from ..helper.date import get_dates_by_intervals

def hard_dates(pressures, dates, tag):
    subs = []
    for i in range(1, len(pressures)):
        subs.append(pressures[i] - pressures[i - 1])
    if tag == 'low':
        mask_subs = [1 if sub <= -3 else 0 for sub in subs]
    elif tag == 'up':
        mask_subs = [1 if sub >= 3 else 0 for sub in subs]
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
                intervals.append((subs[i], (current[0], current[1])))
            current[0] = -1
    if not current[0] == -1:
        intervals.append((max_sub, (current[0], current[1])))
    if len(intervals) == 0:
        return None
    top_interval = [max(intervals, key=lambda x: x[0])[1]]
    return get_dates_by_intervals(dates, top_interval)