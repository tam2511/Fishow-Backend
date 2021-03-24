def strong(text):
    return '<strong>{}</strong>'.format(text)


def red_strong(text):
    return '<span class="red strong">{}</span>'.format(text)


def blue_strong(text):
    return '<span class="blue strong">{}</span>'.format(text)


cases = {
    'Щука': {
        'r': 'щуки', 'd': 'щуку', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение')),
        'pressure+': '{} и {}'.format(blue_strong('спад'), strong('стабильность')),
        'pressure-': 'резкий {}'.format('рост')
    },
    'Сом': {
        'r': 'сома', 'd': 'сома', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Судак': {
        'r': 'судака', 'd': 'судака', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Окунь': {
        'r': 'окуня', 'd': 'окуня', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Берш': {
        'r': 'берша', 'd': 'берша', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Речная форель': {
        'r': 'речной форели', 'd': 'ручную форель', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение')),
        'pressure+': None,
        'pressure-': None
    },
    'Озерная форель': {
        'r': 'озерной форели', 'd': 'озерную форель', 'temperature+': blue_strong('понижение'),
        'temperature-': 'резкое {}'.format(red_strong('повышение')),
        'pressure+': None,
        'pressure-': None
    },
    'Елец': {
        'r': 'ельца', 'd': 'ельца', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Чехонь': {
        'r': 'чехони', 'd': 'чехонь', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Голавль': {
        'r': 'голавля', 'd': 'голавля', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Язь': {
        'r': 'язя', 'd': 'язя', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Карп': {
        'r': 'карпа', 'd': 'карпа', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Жерех': {
        'r': 'жереха', 'd': 'жереха', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Лещ': {
        'r': 'леща', 'd': 'леща', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Карась': {
        'r': 'карася', 'd': 'карася', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Линь': {
        'r': 'линя', 'd': 'линя', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Пескарь': {
        'r': 'пескаря', 'd': 'пескаря', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Ротан': {
        'r': 'ротана', 'd': 'ротана', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Плотва': {
        'r': 'плотвы', 'd': 'плотву', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Красноперка': {
        'r': 'красноперки', 'd': 'красноперку', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Налим': {
        'r': 'налима', 'd': 'налима', 'temperature+': blue_strong('понижение'), 'temperature-': 'повышение',
        'pressure+': None,
        'pressure-': None
    },
    'Густера': {
        'r': 'густеры', 'd': 'густеру', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Амур': {
        'r': 'амура', 'd': 'амура', 'temperature+': red_strong('повышение'), 'temperature-': 'понижение',
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Ерш': {
        'r': 'ерша', 'd': 'ерша', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Сазан': {
        'r': 'сазана', 'd': 'сазана', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Подуст': {
        'r': 'подуста', 'd': 'подуста', 'temperature+': None, 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    },
    'Толстолобик': {
        'r': 'толстолобика', 'd': 'толстолобика', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Вобла': {
        'r': 'воблы', 'd': 'воблу', 'temperature+': red_strong('повышение'),
        'temperature-': 'резкое {}'.format(blue_strong('понижение')),
        'pressure+': None,
        'pressure-': 'резкий {}'.format('спад')
    },
    'Хариус': {
        'r': 'жереха', 'd': 'жереха', 'temperature+': red_strong('повышение'), 'temperature-': None,
        'pressure+': None,
        'pressure-': None
    }
}
