def strong(text):
    return '<strong>{}</strong>'.format(text)


def red_strong(text):
    return '<span class="red strong">{}</span>'.format(text)


def blue_strong(text):
    return '<span class="blue strong">{}</span>'.format(text)


cases = {
    'щука': {
        'r': 'щуки', 'd': 'щуку', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение'))
    },
    'сом': {
        'r': 'сома', 'd': 'сома', 'temperature+': None, 'temperature-': None
    },
    'судак': {
        'r': 'судака', 'd': 'судака', 'temperature+': None, 'temperature-': None
    },
    'окунь': {
        'r': 'окуня', 'd': 'окуня', 'temperature+': red_strong('повышение'), 'temperature-': None
    },
    'берш': {
        'r': 'берша', 'd': 'берша', 'temperature+': None, 'temperature-': None
    },
    'речная форель': {
        'r': 'речной форели', 'd': 'ручную форель', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение'))
    },
    'озерная форель': {
        'r': 'озерной форели', 'd': 'озерную форель', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение'))
    },
    'елец': {
        'r': 'ельца', 'd': 'ельца', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'чехонь': {
        'r': 'чехони', 'd': 'чехонь', 'temperature+': red_strong('повышение'), 'temperature-': None
    },
    'голавль': {
        'r': 'голавля', 'd': 'голавля', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'язь': {
        'r': 'язя', 'd': 'язя', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'карп': {
        'r': 'карпа', 'd': 'карпа', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'жерех': {
        'r': 'жереха', 'd': 'жереха', 'temperature+': red_strong('повышение'), 'temperature-': None
    },
    'лещ': {
        'r': 'леща', 'd': 'леща', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'карась': {
        'r': 'карася', 'd': 'карася', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'линь': {
        'r': 'линя', 'd': 'линя', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'пескарь': {
        'r': 'пескаря', 'd': 'пескаря', 'temperature+': red_strong('повышение'), 'temperature-': None
    },
    'ротан': {
        'r': 'ротана', 'd': 'ротана', 'temperature+': None, 'temperature-': None
    },
    'плотва': {
        'r': 'плотвы', 'd': 'плотву', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'красноперка': {
        'r': 'красноперки', 'd': 'красноперку', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'налим': {
        'r': 'налима', 'd': 'налима', 'temperature+': blue_strong('понижение'), 'temperature-': 'повышение'
    },
    'густера': {
        'r': 'густеры', 'd': 'густеру', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'амур': {
        'r': 'амура', 'd': 'амура', 'temperature+': red_strong('повышение'), 'temperature-': 'понижение'
    },
    'ерш': {
        'r': 'ерша', 'd': 'ерша', 'temperature+': None, 'temperature-': None
    },
    'сазан': {
        'r': 'сазана', 'd': 'сазана', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'подуст': {
        'r': 'подуста', 'd': 'подуста', 'temperature+': None, 'temperature-': None
    },
    'толстолобик': {
        'r': 'толстолобика', 'd': 'толстолобика', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
    'вобла': {
        'r': 'воблы', 'd': 'воблу', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение'))
    },
}
