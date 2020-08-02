def strong(text):
    return '<strong>{}</strong>'.format(text)


def red_strong(text):
    return '<span class="red strong">{}</span>'.format(text)


def blue_strong(text):
    return '<span class="blue strong">{}</span>'.format(text)


cases = {
    'щука': {
        'r': 'щуки', 'd': 'щуку', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение')),
        'pressure+': '{} и {}'.format(blue_strong('спад'), strong('стабильность')),
        'pressure-': 'резкий {}'.format('рост')
    },
    'сом': {
        'r': 'сома', 'd': 'сома', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'судак': {
        'r': 'судака', 'd': 'судака', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'окунь': {
        'r': 'окуня', 'd': 'окуня', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'берш': {
        'r': 'берша', 'd': 'берша', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'речная форель': {
        'r': 'речной форели', 'd': 'ручную форель', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение')),
        'pressure+': None,
        'pressure-': None
    },
    'озерная форель': {
        'r': 'озерной форели', 'd': 'озерную форель', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение')),
        'pressure+': None,
        'pressure-': None
    },
    'елец': {
        'r': 'ельца', 'd': 'ельца', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'чехонь': {
        'r': 'чехони', 'd': 'чехонь', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'голавль': {
        'r': 'голавля', 'd': 'голавля', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'язь': {
        'r': 'язя', 'd': 'язя', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'карп': {
        'r': 'карпа', 'd': 'карпа', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'жерех': {
        'r': 'жереха', 'd': 'жереха', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'лещ': {
        'r': 'леща', 'd': 'леща', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'карась': {
        'r': 'карася', 'd': 'карася', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'линь': {
        'r': 'линя', 'd': 'линя', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'пескарь': {
        'r': 'пескаря', 'd': 'пескаря', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'ротан': {
        'r': 'ротана', 'd': 'ротана', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'плотва': {
        'r': 'плотвы', 'd': 'плотву', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'красноперка': {
        'r': 'красноперки', 'd': 'красноперку', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'налим': {
        'r': 'налима', 'd': 'налима', 'temperature+': blue_strong('понижение'), 'temperature-': 'повышение',
        'pressure+': None,
        'pressure-': None
    },
    'густера': {
        'r': 'густеры', 'd': 'густеру', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'амур': {
        'r': 'амура', 'd': 'амура', 'temperature+': red_strong('повышение'), 'temperature-': 'понижение',
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'ерш': {
        'r': 'ерша', 'd': 'ерша', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'сазан': {
        'r': 'сазана', 'd': 'сазана', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'подуст': {
        'r': 'подуста', 'd': 'подуста', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'толстолобик': {
        'r': 'толстолобика', 'd': 'толстолобика', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'вобла': {
        'r': 'воблы', 'd': 'воблу', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
}
