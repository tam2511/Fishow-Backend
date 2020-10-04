'''
desc block
'''

bad_day_desc_text = '''<strong>{}</strong> луна находится в стадии {} на <strong>{}</strong>%. В данной стадии <strong>{}</strong>, как правило, мало активна. '''

good_day_desc_text = '''<strong>{}</strong> луна находится в стадии {} на <strong>{}</strong>%. В данной стадии <strong>{}</strong> проявляет активность. '''

neutral_day_desc_text = '''<strong>{}</strong> луна находится в стадии {} на <strong>{}</strong>%. В данной стадии клев <strong>{}</strong> больше зависит от других факторов. '''

bad_desc_text_extra = '''За рассматриваемый период снижения клева <strong>{}</strong> по лунному календарю не наблюдается. '''

bad_desc_text = '''<strong>{}</strong> возможно ухудшение клева <strong>{}</strong> по лунному календарю. '''

neutral_desc_text_extra = '''За рассматриваемый период умеренный клев <strong>{}</strong> по лунному календарю не прогнозируется. '''

neutral_desc_text = '''<strong>{}</strong> луна не оказывает значительного влияния на клев рыбы. Стоит обратить внимание на другие факторы клева. '''

good_desc_text_extra = '''За рассматриваемый период хорошего клева <strong>{}</strong> по лунному календарю не прогнозируется. '''

good_desc_text = '''<strong>{}</strong> луна находится в благоприятной стадии и способствуют хорошему клеву <strong>{}</strong>. '''

'''
utils
'''

moon_cases = {
    -1: 'убывания',
    1: 'роста',
    0: 'роста'
}

moon_intervals = {
    -1: {
        (0.8, 1.0): 'bad',
        (-0.001, 0.07): 'bad',
        (0.2, 0.5): 'good',
        (0.5, 0.8): 'neutral',
        (0.07, 0.2): 'neutral',
    },
    1: {
        (-0.001, 0.2): 'bad',
        (0.95, 1.0): 'bad',
        (0.5, 0.75): 'good',
        (0.2, 0.5): 'neutral',
        (0.75, 0.95): 'neutral',
    },
    0: {
        (-0.001, 0.2): 'bad',
        (0.95, 1.0): 'bad',
        (0.5, 0.75): 'good',
        (0.2, 0.5): 'neutral',
        (0.75, 0.95): 'neutral',
    }
}


def stage_flag(moon_direction, moon):
    for left_right in moon_intervals[moon_direction]:
        if moon / 100 > left_right[0] and moon / 100 <= left_right[1]:
            return moon_intervals[moon_direction][left_right]
