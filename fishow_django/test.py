import sqlite3
from datetime import datetime


def escape_name(s):
    """Escape name to avoid SQL injection and keyword clashes.
    Doubles embedded backticks, surrounds the whole in backticks.
    Note: not security hardened, caveat emptor.
    """
    return '`{}`'.format(s.replace('`', '``'))


# con = pymysql.connect('localhost', 'tam2511_fishow',
#                       '081099', 'tam2511_fishow')
con = sqlite3.connect('db.sqlite3')

dict_of_params = [
    {
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('04.04.2020', '%d.%m.%Y'),
        'areal': 'московская область',
        'city': 'москва',
        'fish': 'щука',
        'prob_min': '[0.1,0.2,0.1,0.5,0.3,0.5,0.2,0.3,0.2]',
        'prob_max': '[0.2,0.5,0.3,0.8,0.6,0.8,0.5,0.7,0.6]'
    },
    {
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('05.04.2020', '%d.%m.%Y'),
        'areal': 'московская область',
        'city': 'москва',
        'fish': 'щука',
        'prob_min': '[0.1,0.2,0.1,0.5,0.3,0.5,0.2,0.3,0.2]',
        'prob_max': '[0.2,0.5,0.3,0.8,0.6,0.8,0.5,0.7,0.6]'
    },
    {
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('04.04.2020', '%d.%m.%Y'),
        'areal': 'московская область',
        'city': 'москва',
        'fish': 'сом',
        'prob_min': '[0.15,0.25,0.15,0.55,0.35,0.55,0.25,0.35,0.25]',
        'prob_max': '[0.25,0.55,0.35,0.85,0.65,0.85,0.55,0.75,0.65]'
    },
    {
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('05.04.2020', '%d.%m.%Y'),
        'areal': 'московская область',
        'city': 'москва',
        'fish': 'сом',
        'prob_min': '[0.15,0.25,0.15,0.55,0.35,0.55,0.25,0.35,0.25]',
        'prob_max': '[0.25,0.55,0.35,0.85,0.65,0.85,0.55,0.75,0.65]'
    },
{
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('04.04.2020', '%d.%m.%Y'),
        'areal': 'московская область',
        'city': 'балашиха',
        'fish': 'сом',
        'prob_min': '[0.15,0.25,0.15,0.55,0.35,0.55,0.25,0.35,0.25]',
        'prob_max': '[0.25,0.55,0.35,0.85,0.65,0.85,0.55,0.75,0.65]'
    },
    {
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('05.04.2020', '%d.%m.%Y'),
        'areal': 'московская область',
        'city': 'балашиха',
        'fish': 'сом',
        'prob_min': '[0.15,0.25,0.15,0.55,0.35,0.55,0.25,0.35,0.25]',
        'prob_max': '[0.25,0.55,0.35,0.85,0.65,0.85,0.55,0.75,0.65]'
    },
{
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('04.04.2020', '%d.%m.%Y'),
        'areal': 'ленинградская область',
        'city': 'санкт-петербург',
        'fish': 'сом',
        'prob_min': '[0.15,0.25,0.15,0.55,0.35,0.55,0.25,0.35,0.25]',
        'prob_max': '[0.25,0.55,0.35,0.85,0.65,0.85,0.55,0.75,0.65]'
    },
    {
        'temperature_min': '[1,2,1,3,1,2,3,2,4]',
        'temperature_mean': '[2,3,2,3,3,4,5,4,3]',
        'temperature_max': '[4,5,4,5,5,4,6,7,8]',
        'wind_mean': '[3,6,5,7,3,4,6,3,2]',
        'wind_direction': '[\'СЗ\',\'З\',\'З\',\'СЗ\',\'С\',\'В\',\'Ю\',\'ЮВ\',\'В\']',
        'gust_max': '[7,13,5,11,11,10,9,10,10]',
        'phenomenon': '[\'[пасмурно]\',\'[дождь,малооблачно]\',\'[малооблачно]\',\'[дождь,пасмурно]\',\'[ясно]\',\'[пасмурно]\',\'[пасмурно]\',\'[ясно]\',\'[пасмурно]\']',
        'pressure_min': '[733,734,733,735,735,733,738,735,733]',
        'pressure_max': '[739,740,739,751,739,744,746,744,739]',
        'humidity_mean': '[64,63,22,34,44,71,33,54,57]',
        'uv_index_mean': '[3,3,3,3,5,4,3,2,1]',
        'moon': '[1,4,7,14,21,28,33,40]',
        'moon_direction': '[1,1,1,1,1,1,1,1,1]',
        'date': datetime.strptime('05.04.2020', '%d.%m.%Y'),
        'areal': 'ленинградская область',
        'city': 'санкт-петербург',
        'fish': 'сом',
        'prob_min': '[0.15,0.25,0.15,0.55,0.35,0.55,0.25,0.35,0.25]',
        'prob_max': '[0.25,0.55,0.35,0.85,0.65,0.85,0.55,0.75,0.65]'
    },
]
names = list(dict_of_params[0])
cols = ', '.join(map(escape_name, names))  # assumes the keys are *valid column names*.

with con:
    cur = con.cursor()
    for _ in dict_of_params:
        placeholders = ', '.join(['\"{}\"'.format(str(_[name])) for name in names])
        query = 'INSERT INTO prediction_predictionten ({}) VALUES ({})'.format(cols, placeholders)
        print(query)
        cur.execute(query)