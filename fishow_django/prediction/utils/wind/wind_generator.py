import datetime
import numpy as np
from collections import Counter

from .wind_helper import *
from ..helper.text import cases
from ..helper.date import parse_date
from ..helper.extra import deserialize2, deserialize, deserialize0


class WindTextGenerator:

    @staticmethod
    def get_day_fish(fish):
        fish_case = cases[fish]
        return pos_neg_fish.format(fish_case['r'])

    @staticmethod
    def get_tenday_fish(fish):
        fish_case = cases[fish]
        return pos_neg_fish.format(fish_case['r'])

    @staticmethod
    def get_day_desc(data, date, fish):
        filtred_data = sorted(
            sum([deserialize2(_.wind, _.wind_direction) for _ in data if _.date == date and _.fish == fish], []),
            key=lambda x: x[1])
        winds = [_[0] for _ in filtred_data]
        mean_wind = np.mean(winds)
        wind_directions = [_[1] for _ in filtred_data]
        freq_direction = Counter(wind_directions).most_common(1)[0][0]
        if mean_wind > 5:
            return hard_wind_desc.format(mean_wind, wind_cases[freq_direction])
        elif mean_wind < 2:
            return low_wind_desc.format(wind_cases[freq_direction])
        else:
            return mean_wind_desc.format(mean_wind, wind_cases[freq_direction])

    @staticmethod
    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {
            observe_date: sum([deserialize(_.wind) for _ in data if _.date == observe_date and _.fish == fish], []) for
            observe_date in observe_dates}
        mean_temps = [np.mean([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        min_temp = min(mean_temps)
        max_temp = max(mean_temps)
        min_date = parse_date(observe_dates[mean_temps.index(min_temp)])
        max_date = parse_date(observe_dates[mean_temps.index(max_temp)])
        return ten_minmax_desc.format(min_date, min_temp, max_date, max_temp)

    @staticmethod
    def get_wind_roza(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {observe_date: sum(
            [deserialize0(_.wind_direction) for _ in data if _.date == observe_date and _.fish == fish], []) for
                        observe_date in observe_dates}
        winds = sum([filtred_data[d] for d in filtred_data], [])
        null_roza = {'З': 0, 'СЗ': 0, 'ЮЗ': 0, 'В': 0, 'СВ': 0, 'ЮВ': 0, 'Ю': 0, 'С': 0, }
        roza = dict(Counter(winds))
        for key in null_roza:
            if key in roza:
                null_roza[key] = roza[key]
        return null_roza
