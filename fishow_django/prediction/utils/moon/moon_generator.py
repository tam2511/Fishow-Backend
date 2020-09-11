import datetime
import numpy as np

from .moon_helper import *
from ..helper.text import cases
from ..helper.date import parse_date, get_dates_text


class MoonTextGenerator:

    @staticmethod
    def get_day_desc(data, date, fish):
        filtred_data = sorted([(_.moon_direction, _.moon, _.time) for _ in data if _.date == date and _.fish == fish],
                              key=lambda x: x[1])
        moon_direction = filtred_data[0][0]
        moon = filtred_data[0][1]
        moon_stage = stage_flag(moon_direction, moon)
        if moon_stage == 'bad':
            return bad_day_desc_text.format(parse_date(date), moon_cases[moon_direction], int(moon * 100), fish)
        if moon_stage == 'good':
            return good_day_desc_text.format(parse_date(date), moon_cases[moon_direction], int(moon * 100), fish)
        if moon_stage == 'neutral':
            return neutral_day_desc_text.format(parse_date(date), moon_cases[moon_direction], int(moon * 100), fish)

    @staticmethod
    def get_tenday_desc(data, date, fish):
        observe_dates = [date + datetime.timedelta(days=day) for day in range(9)]
        filtred_data = {observe_date: [(_.moon_direction, _.moon, _.time) for _ in data if
                                       _.date == observe_date and _.fish == fish] for observe_date in observe_dates}
        moon_directions = [filtred_data[d][0][0] for d in filtred_data]
        moons = [filtred_data[d][0][1] for d in filtred_data]
        moon_stages = [stage_flag(moon_directions[i], moons[i]) for i in range(len(moons))]
        bad_dates = [observe_dates[i] for i in range(len(moon_stages)) if moon_stages[i] == 'bad']
        good_dates = [observe_dates[i] for i in range(len(moon_stages)) if moon_stages[i] == 'good']
        neutral_dates = [observe_dates[i] for i in range(len(moon_stages)) if moon_stages[i] == 'neutral']

        if len(bad_dates) > 0 and len(good_dates) > 0 and len(neutral_dates) > 0:
            return {
                'bad': bad_desc_text.format(get_dates_text(bad_dates), cases[fish]['r']),
                'neutral': neutral_desc_text.format(get_dates_text(neutral_dates), cases[fish]['r']),
                'good': good_desc_text.format(get_dates_text(good_dates), cases[fish]['r'])
            }

        if len(bad_dates) > 0 and len(good_dates) > 0 and len(neutral_dates) == 0:
            return {
                'bad': bad_desc_text.format(get_dates_text(bad_dates), cases[fish]['r']),
                'neutral': neutral_desc_text_extra.format(cases[fish]['r']),
                'good': good_desc_text.format(get_dates_text(good_dates), cases[fish]['r'])
            }

        if len(bad_dates) > 0 and len(good_dates) == 0 and len(neutral_dates) > 0:
            return {
                'bad': bad_desc_text.format(get_dates_text(bad_dates), cases[fish]['r']),
                'neutral': neutral_desc_text.format(get_dates_text(neutral_dates), cases[fish]['r']),
                'good': good_desc_text_extra.format(cases[fish]['r'])
            }
        if len(bad_dates) > 0 and len(good_dates) == 0 and len(neutral_dates) == 0:
            return {
                'bad': bad_desc_text.format(get_dates_text(bad_dates), cases[fish]['r']),
                'neutral': neutral_desc_text_extra.format(cases[fish]['r']),
                'good': good_desc_text_extra.format(cases[fish]['r'])
            }
        if len(bad_dates) == 0 and len(good_dates) > 0 and len(neutral_dates) > 0:
            return {
                'bad': bad_desc_text_extra.format(cases[fish]['r']),
                'neutral': neutral_desc_text.format(get_dates_text(neutral_dates), cases[fish]['r']),
                'good': good_desc_text.format(get_dates_text(good_dates), cases[fish]['r'])
            }
        if len(bad_dates) == 0 and len(good_dates) > 0 and len(neutral_dates) == 0:
            return {
                'bad': bad_desc_text_extra.format(cases[fish]['r']),
                'neutral': neutral_desc_text_extra.format(cases[fish]['r']),
                'good': good_desc_text.format(get_dates_text(good_dates), cases[fish]['r'])
            }
        if len(bad_dates) == 0 and len(good_dates) == 0 and len(neutral_dates) > 0:
            return {
                'bad': bad_desc_text_extra.format(cases[fish]['r']),
                'neutral': neutral_desc_text.format(get_dates_text(neutral_dates), cases[fish]['r']),
                'good': good_desc_text_extra.format(cases[fish]['r'])
            }
