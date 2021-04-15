from random import randint
from fishs_config import *

obl_map = {
    'suncl': 'облачно',
    'sunc': 'малооблачно',
    'dull': 'пасмурно',
    'sun': 'ясно',
    '-': '-'
}
phen_map = {
    'snow': 'снег',
    'rain': 'дождь',
    'storm': 'шторм',
    '-': '-'
}
month_map = {
    1: 'январь',
    2: 'февраль',
    3: 'март',
    4: 'апрель',
    5: 'май',
    6: 'июнь',
    7: 'июль',
    8: 'август',
    9: 'сентябрь',
    11: 'ноябрь',
    12: 'декабрь',
    10: 'октябрь',
}

moon_intervals = {
    -1: {
        (0.8, 1.0): -1,
        (-0.001, 0.07): -1,
        (0.2, 0.5): -1,
        (0.5, 0.8): 0,
        (0.07, 0.2): 0,
    },
    1: {
        (-0.001, 0.2): -1,
        (0.95, 1.0): -1,
        (0.5, 0.75): 1,
        (0.2, 0.5): 0,
        (0.75, 0.95): 0,
    },
    0: {
        (-0.001, 0.2): -1,
        (0.95, 1.0): -1,
        (0.5, 0.75): 1,
        (0.2, 0.5): 0,
        (0.75, 0.95): 0,
    }
}


def stage_flag(moon_direction, moon):
    for left_right in moon_intervals[moon_direction]:
        if moon / 100 > left_right[0] and moon / 100 <= left_right[1]:
            return moon_intervals[moon_direction][left_right]


def gen_moon(days):
    moon = randint(0, 99)
    moon_dir = randint(0, 1)
    moons, moon_dirs = [], []
    for _ in range(days):
        if moon_dir:
            moon += 7
            if moon > 100:
                moon = 200 - moon
                moon_dir = 0
        else:
            moon -= 7
            if moon < 0:
                moon = -moon
                moon_dir = 1
        moons.append(moon)
        moon_dirs.append(moon_dir)
    return moons, moon_dirs


def moon_forecast(moon, moon_dir):
    forecast = []
    for moon_, dir_ in zip(moon, moon_dir):
        forecast.append(stage_flag(dir_, moon_))
    return forecast


def wind_forecast(fish, winds, wind_dirs):
    forecast = []
    for wind, wind_dir in zip(winds, wind_dirs):
        if fish == 'окунь':
            forecast.append(int(wind <= 3))
            continue
        if wind_dir in ['В', 'СВ', 'С']:
            forecast.append(-1 + int(wind <= 2))
        elif wind_dir in ['СЗ', 'ЮВ']:
            if wind <= 1:
                forecast.append(1)
            elif wind <= 3:
                forecast.append(0)
            else:
                forecast.append(-1)
        else:
            if wind <= 4:
                forecast.append(1)
            else:
                forecast.append(0)
    return forecast


def temp_forecast(fish, temps, obls, phens):
    forecast = []
    for temp, obl, phen in zip(temps, obls, phens):
        if fish in fishs_bel:
            if obl == 'dull':
                if phen == '-':
                    if temp > 30:
                        forecast.append(0)
                    elif temp > 21:
                        forecast.append(1)
                    elif temp > 15:
                        forecast.append(0)
                    else:
                        forecast.append(-1)
                else:
                    if temp > 32:
                        forecast.append(0)
                    elif temp > 25:
                        forecast.append(1)
                    else:
                        forecast.append(-1)
            else:
                if phen == 'rain':
                    if temp > 23:
                        forecast.append(1)
                    else:
                        forecast.append(0)
                elif phen == '-':
                    if temp > 15:
                        forecast.append(1)
                    else:
                        forecast.append(0)
                else:
                    if temp > 25:
                        forecast.append(0)
                    else:
                        forecast.append(-1)
        else:
            if obl == 'dull':
                if phen == 'storm':
                    if temp > 30:
                        forecast.append(0)
                    elif temp > 21:
                        forecast.append(1)
                    else:
                        forecast.append(0)
                else:
                    if temp > 10:
                        forecast.append(1)
                    else:
                        forecast.append(0)
            else:
                if temp > 30:
                    forecast.append(-1)
                elif temp > 15:
                    forecast.append(0)
                else:
                    forecast.append(1)
    return forecast


def pressure_forecast(fish, pressure):
    forecast = [0, 0, 0]
    for i in range(3, len(pressure)):
        subs = [pressure[i] - pressure[i - 1], pressure[i - 1] - pressure[i - 2], pressure[i - 2] - pressure[i - 3]]
        if fish in fishs_bel:
            if subs[0] < -3:
                forecast.append(-1)
                continue
            elif subs[0] + subs[1] < -9:
                forecast.append(1)
                continue
        else:
            if subs[0] > 3:
                forecast.append(-1)
                continue
            elif subs[0] + subs[1] > 9:
                forecast.append(1)
                continue
        sum_ = sum(map(abs, subs))
        if sum_ < 5:
            forecast.append(1)
            continue
        sum_ = sum(map(abs, subs[:-1]))
        if sum_ < 3:
            forecast.append(1)
            continue
        sum_ = sum(map(abs, subs[:-2]))
        forecast.append(0)
    return forecast


def time_forecast(fish, months, days):
    forecast = []
    for month, day in zip(months, days):
        temp = fish_rec[fish][month]
        temp = {key: temp[key] for key in sorted(temp.keys())}
        for key in temp:
            if day <= key:
                forecast.append(temp[key])
                break
    return forecast
