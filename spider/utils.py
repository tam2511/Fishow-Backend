import json
import logging
ALONE_KEYS = {'time', 'day', 'month', 'humidity', 'uv_index', 'moon', 'moon_direction'}
DIGIT_KEYS = {'temperature', 'wind', 'gust', 'pressure', 'humidity', 'uv_index'}
CATEGORY_KEYS = {'phenomenon', 'wind_direction'}
MOON_KEYS = {'moon', 'moon_direction'}
SUN_KEYS = {'sun_up', 'sun_down'}

PHENOMENONS = ['ясно', 'малооблачно', 'облачно', 'пасмурно', 'небольшой дождь', 'дождь', 'сильный дождь',
               'небольшой снег', 'снег', 'снег с дождём', 'сильный снег', 'гроза', 'мокрый снег']

WIND_DIRECTIONS = ['Ю', 'ЮЗ', 'З', 'СЗ', 'С', 'СВ', 'В', 'ЮВ']
FISHS = ['Щука', 'Судак', 'Окунь', 'Берш', 'Речная форель', 'Озерная форель', 'Елец', 'Чехонь', 'Сом', 'Голавль', 'Язь',
         'Карп', 'Жерех', 'Лещ', 'Карась', 'Линь', 'Пескарь', 'Ротан', 'Плотва', 'Красноперка', 'Налим', 'Густера',
         'Амур', 'Ерш', 'Сазан', 'Подуст', 'Толстолобик', 'Вобла', 'Хариус']

FISH_MAP = {'pike': 'щука', 'sudak': 'судак', 'okun': 'окунь', 'bersh': 'берш',
            'forel reka': 'речная форель', 'forel ozero': 'озерная форель', 'elec': 'елец', 'chexon': 'чехонь',
            'som': 'сом', 'golavl': 'голавль', 'iaz': 'язь', 'carp': 'карп', 'shereh': 'жерех',
            'lesh': 'лещ', 'caras': 'карась', 'lin': 'линь', 'peskar': 'пескарь', 'rotan': 'ротан',
            'plotva': 'плотва', 'kranoperka': 'красноперка', 'nalim': 'налим', 'gustera': 'густера',
            'amur': 'амур', 'ersh': 'ерш', 'sazan': 'сазан', 'podust': 'подуст', 'tolstolob': 'толстолобик',
            'vobla': 'вобла', 'harius': 'хариус'}

FISH_UNMAP = {FISH_MAP[key]: key for key in FISH_MAP}

REGIONS = ['Алтайский край', 'Амурская область', 'Архангельская область', 'Астраханская область',
           'Белгородская область', 'Брянская область', 'Владимирская область', 'Волгоградская область',
           'Вологодская область', 'Воронежская область', 'Еврейская автономная область', 'Забайкальский край',
           'Ивановская область', 'Иркутская область', 'Кабардино-Балкарская республика', 'Калининградская область',
           'Калужская область', 'Камчатский край', 'Карачаево-Черкесская республика', 'Кемеровская область',
           'Кировская область', 'Костромская область', 'Краснодарский край', 'Красноярский край', 'Курганская область',
           'Курская область', 'Ленинградская область', 'Липецкая область', 'Магаданская область', 'Московская область']


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


def setup_logger(logger_name, log_file, level=logging.INFO):
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
