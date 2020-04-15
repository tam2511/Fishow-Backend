import pymysql
from datetime import datetime

def escape_name(s):
    """Escape name to avoid SQL injection and keyword clashes.

    Doubles embedded backticks, surrounds the whole in backticks.

    Note: not security hardened, caveat emptor.

    """
    return '`{}`'.format(s.replace('`', '``'))

con = pymysql.connect('localhost', 'tam2511_fishow',
                      '081099', 'tam2511_fishow')

dict_of_params = [{'time': 23, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'московская область', 'city': 'москва', 'prob': 0.5, 'fish': 'щука', 'features': "признаки ляляля"},
                  {'time': 12, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'ленинградская область', 'city': 'питер', 'prob': 0.5, 'fish': 'карп', 'features': "признаки ляляля"},
                  {'time': 0, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'московская область', 'city': 'не москва', 'prob': 0.5, 'fish': 'сом', 'features': "признаки ляляля"},
                  {'time': 3, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'московская область', 'city': 'москва', 'prob': 0.5, 'fish': 'сом', 'features': "признаки ляляля"}]
names = list(dict_of_param[0])                  
cols = ', '.join(map(escape_name, names))  # assumes the keys are *valid column names*.
placeholders = ', '.join(['%({})s'.format(name) for name in names])

query = 'INSERT INTO prediction_prediction ({}) VALUES ({})'.format(cols, placeholders)
with con:
    cur = con.cursor()
    for _ in dict_of_params:
        cur.execute(query, _)

