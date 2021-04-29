from collections import Counter

import numpy as np

fish_time_rec = {
    'Щука': [0.1, 0.5, 1.2, 1.1, 1.0, 0.9, 1.15, 1.0],
    'Судак': [1.1, 1.0, 1.1, 1.0, 1.0, 0.9, 1.0, 1.1],
    'Окунь': [0.1, 0.5, 1.2, 1.1, 1.0, 1.0, 1.0, 0.9],
    'Берш': [1.1, 1.0, 1.1, 1.0, 1.0, 0.9, 1.0, 1.1],
    'Речная форель': [0.1, 0.1, 1.1, 1.0, 1.0, 0.9, 0.8, 0.5],
    'Озерная форель': [0.1, 0.1, 1.1, 1.0, 1.0, 0.9, 0.8, 0.5],
    'Елец': [0.1, 0.1, 0.9, 1.0, 1.1, 1.1, 0.8, 0.3],
    'Чехонь': [0.1, 0.1, 1.1, 1.0, 1.1, 1.0, 0.7, 0.3],
    'Сом': [1.1, 1.2, 0.8, 0.6, 0.5, 0.4, 0.6, 0.9],
    'Голавль': [0.7, 0.7, 1.1, 1.0, 1.0, 1.0, 0.8, 0.7],
    'Язь': [0.9, 0.9, 1.1, 1.0, 1.0, 1.0, 1.1, 0.9],
    'Карп': [0.9, 0.9, 1.1, 1.0, 1.0, 1.0, 1.1, 0.9],
    'Жерех': [0.3, 0.5, 1.1, 1.0, 1.0, 1.0, 1.1, 0.7],
    'Лещ': [1.1, 1.1, 1.0, 0.9, 0.8, 0.8, 1.0, 1.1],
    'Карась': [0.1, 0.4, 1.1, 1.1, 0.9, 0.9, 1.0, 0.6],
    'Линь': [0.1, 0.4, 1.1, 1.1, 0.9, 0.9, 1.0, 0.6],
    'Пескарь': [0.1, 0.4, 0.8, 1.0, 1.1, 1.1, 1.0, 0.6],
    'Ротан': [0.5, 0.7, 1.1, 1.1, 1.0, 1.0, 1.1, 0.9],
    'Плотва': [0.2, 0.5, 1.1, 1.1, 1.0, 1.0, 1.1, 0.6],
    'Красноперка': [0.2, 0.5, 1.1, 1.1, 1.0, 1.0, 1.1, 0.6],
    'Налим': [1.1, 1.1, 1.0, 0.8, 0.4, 0.6, 0.9, 1.0],
    'Густера': [0.8, 0.9, 1.1, 1.1, 1.0, 1.0, 1.1, 0.9],
    'Амур': [0.8, 0.9, 1.1, 1.1, 1.0, 1.0, 1.1, 1.1],
    'Ерш': [1.1, 1.1, 1.0, 0.8, 0.7, 0.7, 0.9, 1.0],
    'Сазан': [0.8, 0.9, 1.1, 1.1, 1.0, 1.0, 1.1, 0.9],
    'Подуст': [0.6, 0.7, 1.1, 1.1, 0.9, 0.9, 0.8, 0.7],
    'Толстолобик': [0.4, 0.5, 1.1, 1.1, 0.9, 0.9, 0.7, 0.5],
    'Вобла': [0.3, 0.4, 1.1, 1.1, 1.0, 1.0, 0.9, 0.6],
    'Хариус': [0.3, 0.4, 1.1, 1.1, 1.0, 1.0, 0.9, 0.6]
}


def minmax_temperature(data):
    temps = data['temperature'].split(',')
    temps = list(map(int, temps))
    max_ = np.max(temps)
    min_ = np.min(temps)
    mean_ = int(np.mean(temps))
    return {'max': str(max_), 'min': str(min_), 'mean': str(mean_)}


def minmax_wind(data):
    wind = data['wind'].split(',')
    wind = list(map(int, wind))
    mean_ = int(np.mean(wind))
    return {'mean': str(mean_)}


def minmax_wind_direction(data):
    wind_directions = data['wind_direction'].split(',')
    mean_ = Counter(wind_directions).most_common(1)[0][0]
    return {'mean': str(mean_)}


def minmax_gust(data):
    gust = data['gust'].split(',')
    gust = list(map(int, gust))
    max_ = np.max(gust)
    mean_ = int(np.mean(gust))
    return {'max': str(max_), 'mean': str(mean_)}


def minmax_phenomenon(data):
    phenomenon = data['phenomenon'].split(',')
    mean_ = Counter(phenomenon).most_common(1)[0][0]
    return {'mean': str(mean_)}


def minmax_pressure(data):
    pressure = data['pressure'].split(',')
    pressure = list(map(int, pressure))
    max_ = np.max(pressure)
    min_ = np.min(pressure)
    mean_ = int(np.mean(pressure))
    return {'max': str(max_), 'min': str(min_), 'mean': str(mean_)}


def minmax_humidity(data):
    humidity = data['humidity'].split(',')
    humidity = list(map(int, humidity))
    mean_ = int(np.mean(humidity))
    return {'mean': str(mean_)}


def minmax_uv_index(data):
    uv_index = data['uv_index'].split(',')
    uv_index = list(map(int, uv_index))
    mean_ = int(np.max(uv_index))
    return {'mean': str(mean_)}


def minmax_prob(data):
    prob = data['prob'].split(',')
    fish = data['fish']
    prob = list(map(int, prob))
    min_ = np.min(prob)
    max_ = np.max(prob)
    # raise ValueError
    mean_ = int(np.mean([int(prob[i] / fish_time_rec[fish][i]) for i in range(len(prob))]))
    return {'max': str(max_), 'min': str(min_), 'mean': str(mean_)}


def get_mean_data(data):
    mean_data = [{
        'temperature': minmax_temperature(row),
        'wind': minmax_wind(row),
        'wind_direction': minmax_wind_direction(row),
        'gust': minmax_gust(row),
        'pressure': minmax_pressure(row),
        'phenomenon': minmax_phenomenon(row),
        'humidity': minmax_humidity(row),
        'uv_index': minmax_uv_index(row),
        'moon': str(row['moon']),
        'moon_direction': str(row['moon_direction']),
        'prob': minmax_prob(row)
    } for row in data]
    mean_data = {
        'temperature_min': ','.join([_['temperature']['min'] for _ in mean_data]),
        'temperature_max': ','.join([_['temperature']['max'] for _ in mean_data]),
        'wind_mean': ','.join([_['wind']['mean'] for _ in mean_data]),
        'wind_direction': ','.join([_['wind_direction']['mean'] for _ in mean_data]),
        'gust_max': ','.join([_['gust']['max'] for _ in mean_data]),
        'phenomenon': ','.join([_['phenomenon']['mean'] for _ in mean_data]),
        'pressure_min': ','.join([_['pressure']['min'] for _ in mean_data]),
        'pressure_max': ','.join([_['pressure']['max'] for _ in mean_data]),
        'humidity_mean': ','.join([_['humidity']['mean'] for _ in mean_data]),
        'uv_index_mean': ','.join([_['uv_index']['mean'] for _ in mean_data]),
        'moon': ','.join([_['moon'] for _ in mean_data]),
        'moon_direction': ','.join([_['moon_direction'] for _ in mean_data]),
        'prob_min': ','.join([_['prob']['min'] for _ in mean_data]),
        'prob_max': ','.join([_['prob']['max'] for _ in mean_data]),
        'prob_mean': ','.join([_['prob']['mean'] for _ in mean_data]),
    }
    mean_data.update({'date': data[0]['date']})
    mean_data.update({'city': data[0]['city']})
    mean_data.update({'areal': data[0]['areal']})
    mean_data.update({'fish': data[0]['fish']})
    return mean_data
