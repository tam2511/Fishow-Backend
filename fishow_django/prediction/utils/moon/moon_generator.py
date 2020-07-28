import datetime
import numpy as np

from .phenomenon_helper import *
from ..helper.text import cases
from ..helper.date import parse_date


class PhenomenonTextGenerator:

    @staticmethod
    def get_warning(areal, fish):
        return warning_text.format(cases[fish]['r']).format()
