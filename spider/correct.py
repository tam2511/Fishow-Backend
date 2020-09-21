import datetime
import numpy as np

from spider.utils import read_config, average_time, DIGIT_KEYS, MOON_KEYS, SUN_KEYS, CATEGORY_KEYS


class DataError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return 'DataError: {}'.format(self.message)


def average_(left, right, key):
    left_value = left[key]
    right_value = right[key]
    if not left_value or not right_value:
        return None
    if key in DIGIT_KEYS:
        average = np.array(list(map(int, right_value.split(',')))) + np.array(list(map(int, left_value.split(','))))
        average = average // 2
        average = ','.join(map(str, average))
        return average
    elif key in CATEGORY_KEYS:
        return left_value
    elif key in MOON_KEYS:
        left_moon = int(left['moon'])
        right_moon = int(right['moon'])
        left_moon_direction = int(left['moon_direction'])
        right_moon_direction = int(right['moon_direction'])
        moon_average = left_moon * left_moon_direction + right_moon * right_moon_direction
        moon_average = moon_average // 2
        if key == 'moon':
            return abs(moon_average)
        return 1 if moon_average >= 0 else -1
    elif key in SUN_KEYS:
        return average_time(left_value, right_value)
    else:
        IndexError('Bad key for averaging data: {}'.format(key))
    return None


class Corrector:
    def __init__(self, config_path):
        self.config = read_config(config_path)
        try:
            from spider.mysql_utils import MysqlConnector
            self.mysql = MysqlConnector(host=self.config['database']['host'],
                                        username=self.config['database']['username'],
                                        password=self.config['database']['password'],
                                        database=self.config['database']['database'])
        except Exception:
            self.mysql = None

    def correct_mysql_(self, data, key, idx):
        date = data[idx]['date']
        city = data[idx]['city']
        extra_data = self.mysql.select(table_name='prediction_prediction',
                                       where={'date': [date, date - datetime.timedelta(days=1)], 'city': city})

        if len(extra_data) == 0:
            raise DataError('DataError: can\'t find data in table for date = {}, city = .'.format(date, city))
        else:
            current_data = [_ for _ in extra_data if _['date'] == date]
            yesterday_data = [_ for _ in extra_data if not _['date'] == date]

            if len(current_data) == 0 and idx < len(data) - 1:
                tommorow_data = data[idx + 1]
                average_data = average_(yesterday_data[0], tommorow_data, key)
                if not average_data:
                    raise DataError('Bad averaging data for data {} and key {}'.format(current_data, key))
                data[idx][key] = average_data
            elif len(yesterday_data) == 0:
                data[idx][key] = current_data[0][key]
            else:
                raise DataError(
                    'Last idx can\'t correct without nex idx for data {} and key {}'.format(current_data, key))

    def correct_(self, data, key):
        if not data[0][key]:
            if not self.mysql:
                raise DataError('Don\'t find key {} for first day and mysql corrector.'.format(key))
            else:
                self.correct_mysql_(data, key, 0)
        if not data[-1][key]:
            if not self.mysql:
                raise DataError('Don\'t find key {} for first day and mysql corrector.'.format(key))
            else:
                self.correct_mysql_(data, key, len(data) - 1)
        for idx in range(1, len(data) - 1):
            if data[idx][key]:
                continue
            average_data = average_(data[idx - 1], data[idx + 1], key)
            if not average_data:
                if not self.mysql:
                    raise DataError('Bad averaging data for key {}.'.format(key))
                else:
                    self.correct_mysql_(data, key, idx)
            else:
                data[idx][key] = average_data

    def correct(self, data):
        keys = list(data[0].keys())
        for key in keys:
            if key == 'date' or key == 'city' or key == 'areal' or key == 'fish':
                continue
            self.correct_(data, key)
