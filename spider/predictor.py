from joblib import load
from catboost import CatBoostClassifier, CatBoostRegressor

from utils import DIGIT_KEYS, MOON_KEYS, PHENOMENONS, WIND_DIRECTIONS, FISHS, REGIONS, CATEGORY_KEYS, ALONE_KEYS

class Predictor:
    def __init__(self, model_path, logger, num_hours=8, num_days=3):
        self.logger = logger
        self.model = load(model_path)
        self.num_hours = num_hours
        self.num_days = num_days

    def preprocess_(self, data):
        all_data = {}
        for d in data:
            for key in DIGIT_KEYS:
                temp = list(map(int, d[key].split(',')))
                if key in all_data:
                    all_data[key] = all_data[key] + temp
                else:
                    all_data[key] = temp
            for key in MOON_KEYS:
                temp = [d[key] for _ in range(self.num_hours)]
                if key in all_data:
                    all_data[key] = all_data[key] + temp
                else:
                    all_data[key] = temp
            for key in CATEGORY_KEYS:
                if key in all_data:
                    all_data[key] = all_data[key] + d[key].split(',')
                else:
                    all_data[key] = d[key].split(',')
            days = [d['date'].day for _ in range(self.num_hours)]
            months = [d['date'].month for _ in range(self.num_hours)]
            if 'day' in all_data:
                all_data['day'] = all_data['day'] + days
            else:
                all_data['day'] = days
            if 'month' in all_data:
                all_data['month'] = all_data['month'] + months
            else:
                all_data['month'] = months
            if 'time' in all_data:
                all_data['time'] = all_data['time'] + list(range(0, self.num_hours * 3, 3))
            else:
                all_data['time'] = list(range(0, self.num_hours * 3, 3))
        return all_data

    def preprocess_batch_(self, data):
        vec = {}
        for key in data:
            if key in DIGIT_KEYS and not key in ALONE_KEYS:
                for i in range(len(data[key])):
                    key_name = '{}_{}'.format(key, i)
                    vec.update({key_name: data[key][i]})
            elif key == 'phenomenon':
                phenomenons_ = [_.split('.') for _ in data[key]]
                for phenomenon in PHENOMENONS:
                    for i in range(len(phenomenons_)):
                        key_name = '{}_{}'.format(phenomenon, i)
                        vec.update({key_name: int(phenomenon in phenomenons_[i])})
            elif key == 'wind_direction':
                for wind_direction in WIND_DIRECTIONS:
                    for i in range(len(data[key])):
                        key_name = '{}_{}'.format(wind_direction, i)
                        vec.update({key_name: int(wind_direction == data[key][i])})
            elif key == 'month':
                for month in range(1, 13):
                    key_name = 'month_{}'.format(month)
                    vec.update({key_name: int(month == data[key][-1])})
            elif key == 'time':
                for time in range(0, 24, 3):
                    key_name = 'time_{}'.format(time)
                    vec.update({key_name: int(time == data[key][-1])})
            elif key == 'moon_direction':
                for moon_direction in [-1, 1]:
                    key_name = 'moon_direction_{}'.format(moon_direction)
                    vec.update({key_name: int(moon_direction == data[key][-1])})
            elif key in ALONE_KEYS:
                key_name = '{}'.format(key)
                vec.update({key_name: data[key][-1]})
        return vec

    def slice_(self, data, left_bound, righ_bound):
        slice_data = {
            key: data[key][left_bound: righ_bound] for key in data
        }
        return slice_data

    def __call__(self, data):
        all_data = self.preprocess_(data)
        len_data = len(all_data['moon'])
        probs = {fish: [] for fish in FISHS}
        # region_vec = {}
        # for region in REGIONS:
        #     region_vec.update({region: int(data[0]['areal'] == region)})
        for fish in FISHS:
            for i in range(self.num_hours * self.num_days, len_data + 1):
                slice_data = self.slice_(all_data, i - self.num_hours * self.num_days, i)
                vec = self.preprocess_batch_(slice_data)
                for fish_ in FISHS:
                    vec.update({fish_: int(fish_ == fish)})
                # vec.update(region_vec)
                vec = [vec[key] for key in sorted(vec)]
                try:
                    prob = self.model.predict_proba(vec)[1]
                except AttributeError:
                    prob = min(1.0, max(0.0, self.model.predict(vec)))
                probs[fish].append(int(prob * 100))
        return probs
