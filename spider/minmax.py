from collections import Counter

import numpy as np


def minmax_temperature(data):
    temps = data['temperature'].split(',')
    temps = list(map(int, temps))
    max_ = np.max(temps)
    min_ = np.min(temps)
    mean_ = np.mean(temps)
    return {'max': max_, 'min': min_, 'mean': mean_}


def minmax_wind(data):
    wind = data['wind'].split(',')
    wind = list(map(int, wind))
    mean_ = np.mean(wind)
    return {'mean': mean_}


def minmax_wind_direction(data):
    wind_directions = data['wind_direction'].split(',')
    mean_ = Counter(wind_directions).most_common(1)[0][0]
    return {'mean': mean_}


def minmax_gust(data):
    gust = data['gust'].split(',')
    gust = list(map(int, gust))
    max_ = np.max(gust)
    mean_ = np.mean(gust)
    return {'max': max_, 'mean': mean_}


def minmax_phenomenon(data):
    phenomenon = data['phenomenon'].split(',')
    mean_ = Counter(phenomenon).most_common(1)[0][0]
    return {'mean': mean_}


def minmax_pressure(data):
    pressure = data['pressure'].split(',')
    pressure = list(map(int, pressure))
    max_ = np.max(pressure)
    min_ = np.min(pressure)
    mean_ = np.mean(pressure)
    return {'max': max_, 'min': min_, 'mean': mean_}


def minmax_humidity(data):
    humidity = data['humidity'].split(',')
    humidity = list(map(int, humidity))
    mean_ = np.mean(humidity)
    return {'mean': mean_}


def minmax_uv_index(data):
    uv_index = data['uv_index'].split(',')
    uv_index = list(map(int, uv_index))
    mean_ = np.max(uv_index)
    return {'mean': mean_}

def minmax_prob(data):
    pass


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
        'moon': row['moon'],
        'moon_direction': row['moon_direction']
    } for row in data]
    mean_data = {
        'temperature_min': [_['temperature']['min'] for _ in mean_data],
        'temperature_max': [_['temperature']['max'] for _ in mean_data],
        'wind_mean': [_['wind']['mean'] for _ in mean_data],
        'wind_direction': [_['wind_direction']['mean'] for _ in mean_data],
        'gust_max': [_['gust']['max'] for _ in mean_data],
        'phenomenon': [_['phenomenon']['mean'] for _ in mean_data],
        'pressure_min': [_['pressure']['min'] for _ in mean_data],
        'pressure_max': [_['pressure']['max'] for _ in mean_data],
        'humidity_mean': [_['humidity']['mean'] for _ in mean_data],
        'uv_index_mean': [_['uv_index']['mean'] for _ in mean_data],
        'moon': [_['moon'] for _ in mean_data],
        'moon_direction': [_['moon_direction'] for _ in mean_data]
    }
    return mean_data
