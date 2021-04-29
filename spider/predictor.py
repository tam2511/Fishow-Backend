import torch
from predict_utils.models import MainModel
from utils import FISHS


class Predictor:
    def __init__(self, model_path, logger, num_hours=8, num_days=3):
        self.logger = logger
        self.model = MainModel()
        self.model.load_state_dict(torch.load(model_path))
        self.num_hours = num_hours
        self.num_days = num_days

    @torch.no_grad()
    def __call__(self, data):
        probs = {fish: [] for fish in FISHS}
        for i in range(self.num_hours * self.num_days, len(data)):
            slice_data = data[i - self.num_hours * self.num_days + 1: i + 1].values
            outputs, _, _ = self.model(torch.from_numpy(slice_data).unsqueeze(0).float())
            outputs = outputs[0]
            for fish_idx in range(len(outputs)):
                probs[FISHS[fish_idx]].append(int(outputs[fish_idx] * 100))
        return probs
