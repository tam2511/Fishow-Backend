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
                  'areal': 'московская область', 'city': 'москва', 'prob': 0.5, 'fish': 'щука', 'features': "[('относительная влажность (2 дня и 3 ч. назад)', 0.57), ('день в году (2 дня и 3 ч. назад)', 106.0), ('ультрафиолетовый индекс (21 ч. назад)', 0.0), ('температура (2 дня и 21 ч. назад)', 5.0)]"},
                  {'time': 12, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'ленинградская область', 'city': 'питер', 'prob': 0.5, 'fish': 'карп', 'features': "[('погодное явление', 'пасмурно', 1.0), ('порывы ветра (2 дня и 15 ч. назад)', 0.0), ('направление ветра', 'З', 1.0), ('давление (1 день и 3 ч. назад)', 734.0)]"},
                  {'time': 0, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'московская область', 'city': 'не москва', 'prob': 0.5, 'fish': 'сом', 'features': "[('погодное явление', 'небольшой дождь', 0.0), ('погодное явление', 'малооблачно', 1.0), ('относительная влажность (3 ч. назад)', 0.92), ('относительная влажность (12 ч. назад)', 0.83)]"},
                  {'time': 3, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0,
                  'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1,
                  'moon_direction': -1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'московская область', 'city': 'москва', 'prob': 0.5, 'fish': 'сом', 'features': "[('направление ветра (1 день и 3 ч. назад)', 'З', 1.0), ('направление ветра', 'ЮЗ', 0.0), ('перепад температуры (15 ч. назад)', 1.0), ('погодное явление', 'небольшой дождь', 0.0)]"}]
names = list(dict_of_params[0])                  
cols = ', '.join(map(escape_name, names))  # assumes the keys are *valid column names*.
placeholders = ', '.join(['%({})s'.format(name) for name in names])

query = 'INSERT INTO prediction_prediction ({}) VALUES ({})'.format(cols, placeholders)
with con:
    cur = con.cursor()
    for _ in dict_of_params:
        cur.execute(query, _)

