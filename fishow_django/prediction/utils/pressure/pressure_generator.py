import datetime
import numpy as np

from .pressure_helper import *
from ..helper.text import cases
from ..helper.date import parse_date


class PressureTextGenerator:

    @staticmethod
    def get_day_fish(fish):
        fish_case = cases[fish]
        if fish_case['pressure+'] and fish_case['pressure-']:
            return pos_neg_fish.format(fish_case['d'], fish_case['pressure+'], fish_case['pressure-'])
        elif fish_case['pressure+'] and not fish_case['pressure-']:
            return pos_fish.format(fish_case['pressure+'], fish_case['r'])
        elif fish_case['pressure-'] and not fish_case['pressure+']:
            return neg_fish.format(fish_case['pressure-'], fish_case['r'])
        else:
            return none_fish.format(fish_case['r'])

    @staticmethod
    def get_tenday_fish(fish):
        fish_case = cases[fish]
        if fish_case['pressure+'] and fish_case['pressure-']:
            return pos_neg_fish.format(fish_case['d'], fish_case['pressure+'], fish_case['pressure-'])
        elif fish_case['pressure+'] and not fish_case['pressure-']:
            return pos_fish.format(fish_case['pressure+'], fish_case['r'])
        elif fish_case['pressure-'] and not fish_case['pressure+']:
            return neg_fish.format(fish_case['pressure-'], fish_case['r'])
        else:
            return none_fish.format(fish_case['r'])

    @staticmethod
    def get_day_desc(data, date, fish):
        filtred_data = sorted([(_.pressure, _.time) for _ in data if _.date == date and _.fish == fish],
                              key=lambda x: x[1])
        temps = [_[0] for _ in filtred_data]
        min_temp = min(temps)
        max_temp = max(temps)
        return minmax_desc.format(min_temp, max_temp)

    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {observe_date: [(_.pressure, _.time) for _ in data if
                                       _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
        mean_temps = [np.mean([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        min_temps = [min([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        max_temps = [max([_[0] for _ in filtred_data[d]]) for d in filtred_data]
        text_builder = ''
        low_date = hard_dates(mean_temps, observe_dates, 'low')
        up_date = hard_dates(mean_temps, observe_dates, 'up')
        if low_date:
            text_builder += hard_low_desc.format(low_date)
        if up_date:
            text_builder += hard_up_desc.format(up_date)
        min_temp = min(min_temps)
        max_temp = max(max_temps)
        min_date = parse_date(observe_dates[min_temps.index(min_temp)])
        max_date = parse_date(observe_dates[max_temps.index(max_temp)])
        return text_builder + ten_minmax_desc.format(min_date, min_temp, max_date, max_temp)
