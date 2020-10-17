import datetime
import numpy as np

from ..prediction.prediction_helper import get_day_times, get_date_time_text
from .temperature_helper import *
from ..helper.text import cases
from ..helper.date import parse_date
from ..helper.extra import deserialize


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
            return pos_fish.format(fish_case['temperature+'], fish_case['r'])
        elif fish_case['temperature-'] and not fish_case['temperature+']:
            return neg_fish.format(fish_case['temperature-'], fish_case['r'])
        else:
            return none_fish.format(fish_case['r'])

    @staticmethod
    def get_tenday_fish(fish):
        fish_case = cases[fish]
        if fish_case['temperature+'] and fish_case['temperature-']:
            return pos_neg_fish.format(fish_case['d'], fish_case['temperature+'], fish_case['temperature-'])
        elif fish_case['temperature+'] and not fish_case['temperature-']:
            return pos_fish.format(fish_case['temperature+'], fish_case['r'])
        elif fish_case['temperature-'] and not fish_case['temperature+']:
            return neg_fish.format(fish_case['temperature-'], fish_case['r'])
        else:
            return none_fish.format(fish_case['r'])

    @staticmethod
    def get_day_desc(data, date, fish):
        filtred_data = sorted(sum([deserialize(_.temperature) for _ in data if _.date == date and _.fish == fish], []),
                              key=lambda x: x[1])
        temps = [_[0] for _ in filtred_data]
        min_temp = np.min(temps)
        max_temp = np.max(temps)
        mean_temp = np.mean(temps)
        return {
            'mean': mean_temp, 'min': min_temp, 'max': max_temp, 'min_times': parse_date(date),
            'max_times': parse_date(date)
        }

    @staticmethod
    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {
            observe_date: sum([deserialize(_.temperature) for _ in data if _.date == observe_date and _.fish == fish], []) for
            observe_date in observe_dates}
        night_winds = [[_[0] for _ in filtred_data[d] if _[1] in [0, 3]] for d in filtred_data]
        day_winds = [[_[0] for _ in filtred_data[d] if _[1] in [12, 15, 18]] for d in filtred_data]
        mean_temps_night = [np.mean(_) for _ in night_winds]
        min_temps_night = [np.min(_) for _ in night_winds]
        max_temps_night = [np.max(_) for _ in night_winds]
        mean_temps_day = [np.mean(_) for _ in day_winds]
        min_temps_day = [np.min(_) for _ in day_winds]
        max_temps_day = [np.max(_) for _ in day_winds]
        low_date = hard_dates(mean_temps_day, observe_dates, 'low')
        up_date = hard_dates(mean_temps_day, observe_dates, 'up')
        text_builder = ''
        if low_date:
            text_builder += hard_low_desc.format(low_date)
        if up_date:
            text_builder += hard_up_desc.format(up_date)
        if text_builder == '':
            text_builder += hard_no_desc.format(get_dates_by_intervals(observe_dates, [[0, -1]]))
        min_temp_night = np.min(min_temps_night)
        max_temp_night = np.max(max_temps_night)
        mean_temp_night = np.mean(mean_temps_night)
        min_temp_day = np.min(min_temps_day)
        max_temp_day = np.max(max_temps_day)
        mean_temp_day = np.mean(mean_temps_day)
        min_date_night = parse_date(observe_dates[min_temps_night.index(min_temp_night)])
        max_date_night = parse_date(observe_dates[max_temps_night.index(max_temp_night)])
        min_date_day = parse_date(observe_dates[min_temps_day.index(min_temp_day)])
        max_date_day = parse_date(observe_dates[max_temps_day.index(max_temp_day)])
        return {
            'desc': text_builder,
            'day': {
                'mean': mean_temp_day, 'min': min_temp_day, 'max': max_temp_day, 'min_date': min_date_day,
                'max_date': max_date_day
            },
            'night': {
                'mean': mean_temp_night, 'min': min_temp_night, 'max': max_temp_night, 'min_date': min_date_night,
                'max_date': max_date_night
            }
        }
