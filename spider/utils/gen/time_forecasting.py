from random import randint
from numpy.random import choice
from scipy.stats import binom

times = [0, 3, 6, 9, 12, 15, 18, 21]

def gen_forecast(forecast, time, fish):
    if fish in ['Сом', 'Налим']:
        if time == 21:
            return forecast * 1.1
        elif time == 6:
            return forecast * 1.1
        elif time in [0, 3]:
            return forecast * 1.5
        else:
            return forecast * 0.7
    if time in [6, 18]:
        return forecast * 1.3
    elif time == 9:
        return forecast * 1.2
    elif time == 12:
        return forecast * 1.1
    elif time == 15:
        return forecast * 1.0
    else:
        return forecast * 0.7

class DayGenerator:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.times = [12, 15, 18, 21, 0, 3, 6, 9]
        self.dirs = {
            'С': {'values': ['СЗ', 'СВ'], 'p': [0.2, 0.3]},
            'СЗ': {'values': ['С', 'З'], 'p': [0.25, 0.25]},
            'З': {'values': ['СЗ', 'ЮЗ'], 'p': [0.2, 0.3]},
            'ЮЗ': {'values': ['З', 'Ю'], 'p': [0.25, 0.25]},
            'Ю': {'values': ['ЮЗ', 'ЮВ'], 'p': [0.3, 0.2]},
            'ЮВ': {'values': ['Ю', 'В'], 'p': [0.2, 0.3]},
            'В': {'values': ['СВ', 'ЮВ'], 'p': [0.3, 0.2]},
            'СВ': {'values': ['С', 'В'], 'p': [0.3, 0.2]},
        }

        self.phens = {
            'snow': {'values': ['небольшой снег', 'снег', 'снег с дождём', 'сильный снег', 'мокрый снег'],
                     'p': [0.35, 0.25, 0.15, 0.1, 0.15]},
            'rain': {'values': ['небольшой дождь', 'дождь', 'сильный дождь'], 'p': [0.45, 0.35, 0.2]},
            'storm': {'values': ['небольшой дождь', 'дождь', 'гроза', 'сильный дождь'], 'p': [0.15, 0.25, 0.3, 0.3]},
        }

        self.obl = {
            'dull': {'values': ['пасмурно', 'облачно'], 'p': [0.7, 0.3]},
            'suncl': {'values': ['облачно', 'малооблачно', 'пасмурно'], 'p': [0.6, 0.3, 0.1]},
            'sun': {'values': ['ясно', 'малооблачно'], 'p': [0.7, 0.3]},
            'sunc': {'values': ['малооблачно', 'ясно', 'облачно'], 'p': [0.6, 0.2, 0.2]},
        }

        self.fishs = ['Щука', 'Судак', 'Окунь', 'Берш', 'Речная форель', 'Озерная форель', 'Елец', 'Чехонь', 'Сом',
                      'Голавль', 'Язь',
                      'Карп', 'Жерех', 'Лещ', 'Карась', 'Линь', 'Пескарь', 'Ротан', 'Плотва', 'Красноперка', 'Налим',
                      'Густера',
                      'Амур', 'Ерш', 'Сазан', 'Подуст', 'Толстолобик', 'Вобла', 'Хариус']

    def __getitem__(self, idx):
        day_priew = self.dataframe.iloc[idx - 1]
        day = self.dataframe.iloc[idx]
        day_next = self.dataframe.iloc[idx + 1]
        pressure = ','.join(
            map(str, self.gen_pressure(day_priew['day_pressure'], day['day_pressure'], day_next['day_pressure'])))
        temperature = ','.join(
            map(str, self.gen_temperature(day_priew['day_temp'], day['day_temp'], day_next['day_temp'])))
        wind_, gust_ = self.gen_wind(day_priew['day_wind'], day['day_wind'], day_next['day_wind'])
        wind = ','.join(map(str, wind_))
        gust = ','.join(map(str, gust_))
        wind_direction = ','.join(self.gen_dir(day['day_dir']))
        phenomen_ = self.gen_phenomen(day['day_obl'], day['day_phen'])
        humidity = ','.join(map(str, self.gen_hum(phenomen_)))
        phenomen = ','.join(phenomen_)
        uv_index = ','.join(map(str, self.gen_uv(day['month'])))
        moon_direction, moon = self.gen_moon(sum(day[fish].item() for fish in self.fishs) / len(self.fishs))
        return {
            'pressure': pressure,
            'temperature': temperature,
            'wind': wind,
            'gust': gust,
            'wind_direction': wind_direction,
            'humidity': humidity,
            'phenomenon': phenomen,
            'uv_index': uv_index,
            'moon_direction': moon_direction,
            'moon': moon,
            'month': day['month'].item(),
            'day': day['day'].item(),

        }

    def dist_(self, left, right, len_):
        is_revert = False
        if left > right:
            left, right = right, left
            is_revert = True
        result = []
        current = left
        for _ in range(len_ - 1):
            sub = binom.rvs(right - current, 1 / len_)
            current += sub
            result.append(current)
        result.append(right)
        return result[::-1] if is_revert else result

    def gen_pressure(self, pressure_priew, pressure, pressure_next):
        pressure_ = {}
        priew_sub = pressure - pressure_priew
        next_sub = pressure_next - pressure
        current_pressure = pressure_priew
        for time in [15, 18, 21]:
            sub = randint(-2, 0) if priew_sub < 0 else randint(-1, 1)
            current_pressure += sub
        dist = self.dist_(current_pressure, pressure, 5)
        for idx, time in enumerate([0, 3, 6, 9, 12]):
            pressure_.update({time: dist[idx]})
        current_pressure = pressure
        for time in [15, 18, 21]:
            sub = randint(-2, 0) if next_sub < 0 else randint(-1, 1)
            current_pressure += sub
            pressure_.update({time: current_pressure})
        return [pressure_[key] for key in sorted(pressure_)]

    def gen_wind(self, wind_priew, wind, wind_next):
        wind_ = {}
        priew_sub = wind - wind_priew
        next_sub = wind_next - wind
        current_wind = randint(0, randint(wind_priew, wind)) if priew_sub > 0 else 0
        dist = self.dist_(current_wind, wind, 5)
        for idx, time in enumerate([0, 3, 6, 9, 12]):
            wind_.update({time: dist[idx]})
        current_wind = wind_[12] + randint(-1, 2)
        current_wind = max(0, current_wind)
        wind_.update({15: current_wind})
        current_wind += randint(-1, 2)
        current_wind = max(0, current_wind)
        wind_.update({18: current_wind})
        current_wind += randint(-3, 0)
        current_wind = max(0, current_wind)
        wind_.update({21: current_wind})
        gust_ = {time: wind_[time] + randint(3, 8) for time in self.times}
        return [wind_[key] for key in sorted(wind_)], [gust_[key] for key in sorted(gust_)]

    def gen_dir(self, direction):
        dir_ = {}
        if direction == '-':
            direction = choice(list(self.dirs.keys()))
        dist = list(choice([direction] + self.dirs[direction]['values'], 8, p=[0.5] + self.dirs[direction]['p']))
        for idx, time in enumerate(self.times):
            dir_.update({time: dist[idx]})
        return [dir_[key] for key in sorted(dir_)]

    def gen_temperature(self, temp_priew, temp, temp_next):
        temp_ = {}
        priew_sub = temp - temp_priew
        next_sub = temp_next - temp
        current_temp = temp_priew
        for time in [15, 18, 21]:
            sub = randint(-3, -1) if priew_sub < 0 else randint(-2, 0)
            current_temp += sub
        dist = self.dist_(current_temp, temp, 5)
        for idx, time in enumerate([0, 3, 6, 9, 12]):
            temp_.update({time: dist[idx]})
        current_temp = temp
        for time in [15, 18, 21]:
            sub = randint(-3, -1) if next_sub < 0 else randint(-2, 0)
            current_temp += sub
            temp_.update({time: current_temp})
        return [temp_[key] for key in sorted(temp_)]

    def gen_phenomen(self, obl, phen):
        phens_ = {}
        if obl == '-':
            obl = 'sun'
        dist_olb = list(choice(self.obl[obl]['values'], 8, p=self.obl[obl]['p']))
        if phen == '-':
            for idx, time in enumerate(self.times):
                phens_.update({time: dist_olb[idx]})
            return [phens_[key] for key in sorted(phens_)]
        dist_phens = list(choice(self.phens[phen]['values'], 8, p=self.phens[phen]['p']))
        for idx, time in enumerate(self.times):
            phens_.update({time: '.'.join((dist_olb[idx], dist_phens[idx]))})
        return [phens_[key] for key in sorted(phens_)]

    def gen_hum(self, phens):
        hum_ = []
        current_hum = randint(30, 70)
        for phen in phens:
            if 'дождь' in phen:
                current_hum += randint(0, 20)
                current_hum = min(current_hum, randint(93, 99))
            else:
                current_hum += randint(-10, 5)
                current_hum = max(current_hum, randint(10, 29))
            hum_.append(current_hum)
        return hum_

    def gen_uv(self, month):
        uv_ = {}
        if month in [12, 1, 2]:
            uv_ = {0: 0, 3: 0, 6: 0, 9: 0, 12: randint(1, 2), 15: 1, 18: 0, 21: 0}
        elif month in [3, 11, 10, 4]:
            uv_ = {0: 0, 3: 0, 6: 0, 9: 1, 12: randint(2, 3), 15: randint(1, 2), 18: 1, 21: 0}
        elif month in [5, 9]:
            uv_ = {0: 0, 3: 0, 6: randint(0, 1), 9: randint(1, 2), 12: randint(2, 4), 15: randint(2, 3),
                   18: randint(1, 2), 21: randint(0, 1)}
        else:
            uv_ = {0: 0, 3: 0, 6: randint(1, 2), 9: randint(1, 3), 12: randint(2, 4), 15: randint(1, 3),
                   18: randint(1, 3), 21: randint(1, 2)}
        return [uv_[key] for key in sorted(uv_)]

    def gen_moon(self, forecast):
        if forecast > 0.5:
            return 2 * randint(0, 1) - 1, randint(35, 70)
        else:
            if randint(0, 1):
                return 2 * randint(0, 1) - 1, randint(0, 35)
            else:
                return 2 * randint(0, 1) - 1, randint(70, 99)
