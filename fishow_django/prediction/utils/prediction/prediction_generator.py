import datetime
import numpy as np

from .prediction_helper import *
from ..helper.text import cases
from ..helper.date import parse_date, get_dates_tex


class PredictTextGenerator:

    @staticmethod
    def get_day_brief(date, fish):
        return brief_text.format(cases[fish]['r'], date)

    @staticmethod
    def get_tenday_brief(date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        return brief_text.format(cases[fish]['r'], get_dates_tex(observe_dates))

    @staticmethod
    def get_day_desc(data, date, fish):
        filtred_data = sorted([(_.prob, _.time) for _ in data if _.date == date and _.fish == fish],
                              key=lambda x: x[0])
        min_prob = filtred_data[0][0]
        max_prob = filtred_data[-1][0]
        min_times = [_[1] for _ in filtred_data if _[0] == min_prob]
        max_times = [_[1] for _ in filtred_data if _[0] == max_prob]
        min_times = get_day_times(min_times)
        max_times = get_day_times(max_times)
        min_prob = '{} %'.format(int(min_prob * 100))
        max_prob = '{} %'.format(int(max_prob * 100))
        return minmax_day_text.format(parse_date(date), cases[fish]['r'], max_times, max_prob, min_times, min_prob)

    @staticmethod
    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {observe_date: [(_.prob, _.time) for _ in data if
                                       _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
        min_prob = 1
        max_prob = 0
        for d in filtred_data:
            for prob, time in filtred_data[d]:
                if prob < min_prob:
                    min_prob = prob
                    min_date = (d, time)
                if prob > max_prob:
                    max_prob = prob
                    max_date = (d, time)

        min_prob = '{} %'.format(int(min_prob * 100))
        max_prob = '{} %'.format(int(max_prob * 100))
        return {'min': min_prob, 'max': max_prob, 'min_date': get_time_text(*min_date),
                'max_date': get_time_text(*max_date)}
