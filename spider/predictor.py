from joblib import load

from utils import DIGIT_KEYS, MOON_KEYS, PHENOMENONS, WIND_DIRECTIONS, FISHS, REGIONS, CATEGORY_KEYS


class Model:
    def __init__(self, model, mean_layer, std_layer):
        self.model = model
        self.mean = mean_layer
        self.std = std_layer

    def __call__(self, vector):
        vector = (vector - self.mean) / self.std
        return self.model.predict_proba(vector.reshape(1, -1))[0][1]


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
            temp = [d['date'].timetuple().tm_yday for _ in range(self.num_hours)]
            if 'day' in all_data:
                all_data['day'] = all_data['day'] + temp
            else:
                all_data['day'] = temp
            if 'time' in all_data:
                all_data['time'] = all_data['time'] + list(range(0, self.num_hours * 3, 3))
            else:
                all_data['time'] = temp

        return all_data

    def preprocess_batch_(self, data):
        vec = {}
        for key in data:
            if key in DIGIT_KEYS | MOON_KEYS | {'day', 'time'}:
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
        region_vec = {}
        for region in REGIONS:
            region_vec.update({region: int(data[0]['areal'] == region)})
        for fish in FISHS:
            for i in range(self.num_hours * self.num_days, len_data + 1):
                slice_data = self.slice_(all_data, i - self.num_hours * self.num_days, i)
                vec = self.preprocess_batch_(slice_data)
                for fish_ in FISHS:
                    vec.update({fish_: int(fish_ == fish)})
                vec.update(region_vec)
                vec = [vec[key] for key in sorted(vec)]
                prob = self.model(vec)
                probs[fish].append(int(prob * 100))
        return probs
