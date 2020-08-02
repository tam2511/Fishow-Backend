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
    date = str(date).split(' ')[0].split('-')
    day = str(int(date[2]))
    month = str(int(date[1]))
    month_map = {
        '1': 'января', '2': 'февраля', '3': 'марта',
        '4': 'апреля', '5': 'мая', '6': 'июня',
        '7': 'июля', '8': 'августа', '9': 'сентября',
        '10': 'октября', '11': 'ноября', '12': 'декабря'
    }
    return '*{} {}*'.format(day, month_map[month])

def get_dates_by_intervals(dates, intervals):
    dates_interval = []
    for interval in intervals:
        date1 = parse_date(dates[interval[0]])
        date2 = parse_date(dates[interval[1]])
        dates_interval.append('{}-{}'.format(date1, date2))
    if len(dates_interval) == 1:
        return dates_interval[0]
    elif len(dates_interval) == 2:
        return '{} и {}'.format(dates_interval[0], dates_interval[1])
    return ', '.join(dates_interval[:-1]) + 'и {}'.format(dates_interval[-1])


def influence_text_generate(influence_time):
    text_builder = ''
    morning, day, evening, night = morning_influence(influence_time), day_influence(influence_time), evening_influence(
        influence_time), night_influence(influence_time)
    if morning or day or evening or night:
        text_builder += '*сегодня* '
        words = []
        if morning:
            words.append('*утром*')
        if day:
            words.append('*днем*')
        if evening:
            words.append('*вечером*')
        if night:
            words.append('*ночью*')
        if feature_influence(influence_time):
            text_builder += ', '.join(words)
            text_builder += ' и в *ближайшие трое суток*'
        elif len(words) == 1:
            text_builder += (words[0]) + ''
        else:
            text_builder += ', '.join(words[:-1]) + ' и {}'.format(words[-1])
    else:
        text_builder += 'в *ближайшие трое суток*'
    return text_builder

def influence_tendays_text_generate(influence_time):
    days = list(dict.fromkeys(influence_time).keys())
    if len(days) == 1:
        return parse_date(days[0])
    return ', '.join([parse_date(_) for _ in days[:-1]]) + ' и {}'.format(parse_date(days[-1]))