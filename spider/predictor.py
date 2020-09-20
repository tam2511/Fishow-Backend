from joblib import load

class Model:
    def __init__(self, model, mean_layer, std_layer):
        self.model = model
        self.mean = mean_layer
        self.std = std_layer

    def __call__(self, vector):
        if self.normalize_layer:
            vector = (vector - self.mean) / self.std
        return self.model.predict_proba(vector)[0][1]

class Predictor:
    def __init__(self, model_path, logger):
        self.logger = logger
        self.model = load(model_path)

    def preprocess_(self, data):
        pass

    def __call__(self, data):
        vec = self.preprocess_(data)
        pass