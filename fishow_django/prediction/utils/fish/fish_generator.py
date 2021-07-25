import datetime
import numpy as np

from .fish_helper import *
from ..helper.text import cases
from ..helper.date import parse_date, get_dates_tex


class FishTextGenerator:

    @staticmethod
    def get_day_desc(data, date, fish):
        return fish_static_describe[fish]

    @staticmethod
    def get_tenday_desc(data, date, fish):
        return fish_static_describe[fish]
