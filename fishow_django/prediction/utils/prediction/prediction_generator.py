import datetime
import numpy as np

from ..helper.text import cases
from ..helper.date import parse_date


class PredictTextGenerator:

    @staticmethod
    def get_warning(data, date, fish):
        return 'Заглушка'
