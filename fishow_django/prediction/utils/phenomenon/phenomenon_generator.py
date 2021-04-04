import datetime
import numpy as np

from .phenomenon_helper import *
from ..helper.text import cases
from ..helper.date import parse_date


class PhenomenonTextGenerator:

    @staticmethod
    def get_warning(areal, fish):
        return warning_text.format(cases[fish]['r'], areal)

    @staticmethod
    def get_day_desc(data, date, fish):
        observe_dates = [date - datetime.timedelta(days=day) for day in range(1, 3)]
        day_data = [(_.temperature, _.phenomenon) for _ in data if _.date == date and _.fish == fish]
        filtred_data = [(_.temperature, _.phenomenon) for _ in data if _.date in observe_dates and _.fish == fish]
        print('day_data: {}'.format(day_data))
        print('filtred_data: {}'.format(filtred_data))
        return {}


