from joblib import load
from spider.utils import DIGIT_KEYS, MOON_KEYS, PHENOMENONS, WIND_DIRECTIONS


class Model:
    def __init__(self, model, mean_layer, std_layer):
        self.model = model
        self.mean = mean_layer
        self.std = std_layer

    def __call__(self, vector):
        if self.mean and self.std:
            vector = (vector - self.mean) / self.std
        return self.model.predict_proba(vector)[0][1]


class Predictor:
    def __init__(self, model_path, logger, num_rows=3 * 8):
        self.logger = logger
        self.model = load(model_path)
        self.num_rows = num_rows

    def preprocess_(self, data):
        vec = {}
        for i in range(len(data)):
            for key in DIGIT_KEYS:
                splitted = data[i][key].split(',')
                assert len(data) * len(splitted) == 8
                for j in range(8):
                    key_name = '{}_{}'.format(key, i * 8 + j)
                    vec.update({key_name: int(splitted[j])})
            for key in MOON_KEYS:
                for j in range(8):
                    key_name = '{}_{}'.format(key, i * 8 + j)
                    vec.update({key_name: int(data[i][key])})
            phenomenons_ = [_.split(',') for _ in data[i]['phenomenon'].split('.')]
            assert len(data) * len(phenomenons_) == 8
            for phenomenon in PHENOMENONS:
                for j in range(8):
                    key_name = '{}_{}'.format(phenomenon, i * 8 + j)
                    vec.update({key_name: int(phenomenon in phenomenons_[j])})
            wind_directions_ = data[i]['wind_directions'].split(',')
            assert len(data) * len(wind_directions_) == 8
            for wind_direction in WIND_DIRECTIONS:
                for j in range(8):
                    key_name = '{}_{}'.format(wind_direction, i * 8 + j)
                    vec.update({key_name: int(wind_direction == wind_directions_[j])})
        return vec

    def __call__(self, data):
        vec = self.preprocess_(data)
        for i in range(len(data)):
            for j in range(8):
                key_name = 'day_{}'.format(i * 8 + j)
                vec.update({key_name: int(data[i]['date'].timetuple().tm_yday)})

        # TODO: добавить вид рыбы и название региона в вектор

        vec = [vec[key] for key in sorted(vec)]
        prob = self.model(vec)
        return prob
