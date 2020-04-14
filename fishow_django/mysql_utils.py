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

dict_of_params = {'time': 23, 'temperature': 7, 'wind': 2, 'wind_direction': 'СЗ', 'gust': 0, 'phenomenon': "['пасмурно', ' небольшой дождь']", 'pressure': 748, 'humidity': 0.26, 'uv_index': 1, 'moon_direction': 1, 'moon': 0.82, 'day': 95, 'date': datetime.strptime('04.04.2020','%d.%m.%Y'),
                  'areal': 'московская область', 'city': 'город', 'probs': "{'щука': {'prob': 0.7, 'importance_features': {'names': [('wind', 0, 0), ('gust', 1, 3), ('gust', 0, 0), ('sub_temperature', 2, 0)], 'values': [3.0, 19.0, 9.0, -2.0]}},"
                                                                           "'судак': {'prob': 0.6, 'importance_features': {'names': [('temperature', 0, 15), ('humidity', 1, 12), ('gust', 0, 0), ('gust', 2, 9)], 'values': [-4.0, 0.76, 9.0, 0.0]}}"}
names = list(dict_of_params)
cols = ', '.join(map(escape_name, names))  # assumes the keys are *valid column names*.
placeholders = ', '.join(['%({})s'.format(name) for name in names])

query = 'INSERT INTO prediction_prediction ({}) VALUES ({})'.format(cols, placeholders)
with con:
    cur = con.cursor()
    cur.execute(query, dict_of_params)

