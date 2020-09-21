import json

DIGIT_KEYS = {'temperature', 'wind', 'gust', 'pressure', 'humidity', 'uv_index'}
CATEGORY_KEYS = {'phenomenon', 'wind_direction'}
MOON_KEYS = {'moon', 'moon_direction'}
SUN_KEYS = {'sun_up', 'sun_down'}

PHENOMENONS = ['ясно', 'малооблачно', 'облачно', 'пасмурно', 'небольшой дождь', 'дождь', 'сильный дождь',
               'небольшой снег', 'снег', 'снег с дождём', 'сильный снег', 'гроза', 'мокрый снег']

WIND_DIRECTIONS = ['Ю', 'ЮЗ', 'З', 'СЗ', 'С', 'СВ', 'В', 'ЮВ']


def read_config(config_path):
    with open(config_path, 'r', encoding='UTF-8') as config_file:
        return json.load(config_file)


def average_time(left_time, right_time):
    time1 = left_time.split(':')
    time2 = right_time.split(':')
    time1 = int(time1[0]) * 60 + int(time1[1])
    time2 = int(time2[0]) * 60 + int(time2[1])
    mean_time = (time2 - time1) // 2 + time1
    mean_time = ':'.join(map(str, [mean_time // 60, mean_time % 60]))
    return mean_time
