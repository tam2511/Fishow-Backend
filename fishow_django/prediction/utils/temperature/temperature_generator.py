import datetime
import numpy as np

from .temperature_helper import *
from ..helper.text import cases
from ..helper.date import parse_date


class TemperatureTextGenerator:

    @staticmethod
    def get_day_brief(fish):
        return brief_dict[fish].format(cases[fish]['r'])

    @staticmethod
    def get_tenday_brief(fish):
        return brief_dict[fish].format(cases[fish]['r'])

    @staticmethod
    def get_day_fish(fish):
        fish_case = cases[fish]
        if fish_case['temperature+'] and fish_case['temperature-']:
            return pos_neg_fish.format(fish_case['d'], fish_case['temperature+'], fish_case['temperature-'])
        elif fish_case['temperature+'] and not fish_case['temperature-']:
            return pos_fish.format(fish_case['r'], fish_case['temperature+'])
        elif fish_case['temperature-'] and not fish_case['temperature+']:
            return neg_fish.format(fish_case['r'], fish_case['temperature-'])
        else:
            return none_fish.format(fish_case['r'])

    @staticmethod
    def get_tenday_fish(fish):
        fish_case = cases[fish]
        if fish_case['temperature+'] and fish_case['temperature-']:
            return pos_neg_fish.format(fish_case['d'], fish_case['temperature+'], fish_case['temperature-'])
        elif fish_case['temperature+'] and not fish_case['temperature-']:
            return pos_fish.format(fish_case['r'], fish_case['temperature+'])
        elif fish_case['temperature-'] and not fish_case['temperature+']:
            return neg_fish.format(fish_case['r'], fish_case['temperature-'])
        else:
            return none_fish.format(fish_case['r'])

    @staticmethod
    def get_day_desc(data, date, fish):
        filtred_data = sorted([(_.temperature, _.time) for _ in data if _.date == date and _.fish == fish],
                              key=lambda x: x[1])
        temps = [_[0] for _ in filtred_data]
        min_temp = min(temps)
        max_temp = max(temps)
        return minmax_desc.format(max_temp, min_temp)

    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {observe_date: [(_.temperature, _.time) for _ in data if
                                       _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
        mean_temps = [np.mean([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        min_temps = [min([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        max_temps = [max([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        text_builder = hard_low_desc.format(hard_dates(mean_temps, observe_dates, 'low')) + hard_up_desc.format(
            hard_dates(mean_temps, observe_dates, 'up'))
        min_temp = min(min_temps)
        max_temp = max(max_temps)
        min_date = parse_date(observe_dates[min_temps.index(min_temp)])
        max_date = parse_date(observe_dates[max_temps.index(max_temp)])
        return text_builder + ten_minmax_desc.format(min_date, min_temp, max_date, max_temp)
