import pandas as pd
import torch

MANY_KEYS = ['temperature', 'wind', 'wind_direction', 'gust', 'phenomenon', 'pressure', 'humidity', 'uv_index']
ONE_KEYS = ['moon', 'moon_direction']


class FeaturePreprocessing:
    def __init__(self, config):
        self.config = config
        self.features = torch.load(config['prediction']['feature_path'])

    def __call__(self, data):
        data_ = []
        for row in data:
            for i in range(self.config['prediction']['num_hours']):
                temp = {}
                for key in MANY_KEYS:
                    temp[key] = row[key].split(',')[i]
                for key in ONE_KEYS:
                    temp[key] = row[key]
                date = temp['date']
                temp['month'] = date.month
                temp['day_year'] = date.timetuple().tm_yday
                data_.append(temp)
        dt = pd.DataFrame(data_)
        return dt

