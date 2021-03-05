from collections import Counter

import numpy as np


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
    prob = list(map(int, prob))
    min_ = np.min(prob)
    max_ = np.max(prob)
    return {'max': str(max_), 'min': str(min_)}


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
    }
    mean_data.update({'date': data[0]['date']})
    mean_data.update({'city': data[0]['city']})
    mean_data.update({'areal': data[0]['areal']})
    mean_data.update({'fish': data[0]['fish']})
    return mean_data
