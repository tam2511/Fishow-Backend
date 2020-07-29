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


def get_dates_tex(dates):
    intervals = []
    if dates == None:
        return None
    left_date = dates[0]
    current_date = dates[0]
    for i in range(1, len(dates) - 1):
        if (dates[i] - current_date).days > 1:
            intervals.append((left_date, current_date) if current_date > left_date else (left_date))
            left_date = dates[i]
        current_date = dates[i]
    if (dates[-1] - current_date).days > 1:
        intervals.append((left_date, current_date) if current_date > left_date else (left_date))
        intervals.append((dates[-1]))
    else:
        intervals.append((left_date, dates[-1]))
    dates_interval = ['{}-{}'.format(parse_date(_[0]), parse_date(_[1])) if len(_) == 2 else ''.format(parse_date(_[0]))
                      for _ in intervals]
    if len(dates_interval) == 1:
        return dates_interval[0]
    if len(dates_interval) == 2:
        return '{} и {}'.format(dates_interval[0], dates_interval[1])
    return ', '.join(dates_interval[:-1]) + ' и {}'.format(dates_interval[-1])
