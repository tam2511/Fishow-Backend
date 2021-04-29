import pandas as pd
import torch

from utils import FISHS

MANY_KEYS = ['temperature', 'wind', 'wind_direction', 'gust', 'phenomenon', 'pressure', 'humidity', 'uv_index']
ONE_KEYS = ['moon', 'moon_direction']

KEY_DICT = {
    'wind_direction': ['Ю', 'ЮЗ', 'З', 'СЗ', 'С', 'СВ', 'В', 'ЮВ'],
    'moon_direction': [-1, 1],
    'time': [0, 3, 6, 9, 12, 15, 18, 21]
}


class FeaturePreprocessing:
    def __init__(self, config):
        self.config = config
        self.features = torch.load(config['prediction']['feature_path'])
        self.scaler = torch.load(config['prediction']['scaler_path'])
        self.phenomenons = []

    def init_phenomenons(self, temp):
        if len(self.phenomenons) > 0:
            return
        for key in self.features:
            if not key in temp:
                self.phenomenons.append(key)

    def one_hot_phenomenon(self, temp):
        self.init_phenomenons(temp)
        phenomenons = temp['phenomenon'].split('.')
        for phenomenon in self.phenomenons:
            temp[phenomenon] = int(phenomenon in phenomenons)
        del temp['phenomenon']
        return temp

    def prepare_types(self, temp):
        temp['temperature'] = int(temp['temperature'])
        try:
            temp['wind'] = int(temp['wind'])
        except Exception:
            temp['wind'] = 0
        try:
            temp['gust'] = int(temp['gust'])
        except Exception:
            temp['gust'] = 0
        temp['pressure'] = int(temp['pressure'])
        temp['humidity'] = int(temp['humidity'])
        temp['uv_index'] = int(temp['uv_index'])
        temp['moon'] = int(temp['moon'])
        return temp

    def __call__(self, data):
        data_ = []
        for row in data:
            for i in range(self.config['prediction']['num_hours']):
                temp = {}
                temp['time'] = KEY_DICT['time'][i]
                for key in MANY_KEYS:
                    temp[key] = row[key].split(',')[i]
                for key in ONE_KEYS:
                    temp[key] = row[key]
                date = row['date']
                temp['month'] = date.month
                temp['day_year'] = date.timetuple().tm_yday
                for key in KEY_DICT:
                    for wind_key in KEY_DICT[key]:
                        temp['{}_{}'.format(key, wind_key)] = int(temp[key] == wind_key)
                    del temp[key]
                temp = self.one_hot_phenomenon(temp)
                data_.append(self.prepare_types(temp))
        dt = pd.DataFrame(data_)
        return (dt[self.features] - self.scaler['mean']) / self.scaler['std']

