import torch
import torch.nn as nn
from .model_config import model_config


class FCNBlock(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, output_dim, bias=True)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        return self.relu(self.fc(inputs))


class FCN(nn.Module):
    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super().__init__()
        self.start_block = FCNBlock(input_dim, hidden_dim)
        self.blocks = nn.Sequential()
        for _ in range(layer_dim):
            self.blocks.add_module('block_{}'.format(_), FCNBlock(hidden_dim, hidden_dim))
        self.final_block = FCNBlock(hidden_dim, output_dim)

    def forward(self, inputs):
        return self.final_block(self.blocks(self.start_block(inputs)))


class LSTM(nn.Module):

    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.rnn = nn.LSTM(input_dim, hidden_dim, layer_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.batch_size = None
        self.hidden = None

    def forward(self, x):
        h0, c0 = self.init_hidden(x)
        out, (hn, cn) = self.rnn(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

    def init_hidden(self, x):
        h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim)
        c0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim)
        return [t for t in (h0, c0)]


class FCNBlock(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.fc = nn.Linear(input_dim, output_dim, bias=True)
        self.relu = nn.ReLU()

    def forward(self, inputs):
        return self.relu(self.fc(inputs))


class FCN(nn.Module):
    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super().__init__()
        self.start_block = FCNBlock(input_dim, hidden_dim)
        self.blocks = nn.Sequential()
        for _ in range(layer_dim):
            self.blocks.add_module('block_{}'.format(_), FCNBlock(hidden_dim, hidden_dim))
        self.final_block = FCNBlock(hidden_dim, output_dim)

    def forward(self, inputs):
        return self.final_block(self.blocks(self.start_block(inputs)))


class LSTM(nn.Module):
    """Very simple implementation of LSTM-based time-series classifier."""

    def __init__(self, input_dim, hidden_dim, layer_dim, output_dim):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.rnn = nn.LSTM(input_dim, hidden_dim, layer_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)
        self.batch_size = None
        self.hidden = None

    def forward(self, x):
        h0, c0 = self.init_hidden(x)
        out, (hn, cn) = self.rnn(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

    def init_hidden(self, x):
        h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim)
        c0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim)
        return [t for t in (h0, c0)]


class MainModel(nn.Module):
    def __init__(self, config=model_config):
        super().__init__()
        self.fcn = FCN(config['fcn_input'], config['fcn_hidden'], config['fcn_layers'], config['fcn_output'])
        self.embedder = FCN(config['emb_input'], config['emb_hidden'], config['emb_layers'], config['emb_output'])
        self.lstm = LSTM(config['lstm_input'], config['lstm_hidden'], config['lstm_layers'], config['lstm_output'])
        self.fc = nn.Linear(config['fcn_output'] + config['lstm_output'], config['output'])

    def forward(self, x):
        fcn_output = self.fcn(x.contiguous().view(x.size(0), -1))
        embeddings = self.embedder(x.contiguous().view(-1, x.shape[-1])).reshape(x.shape[0], x.shape[1], -1)[:, :-1, :]
        #         print(embeddings.shape)
        lstm_output = self.lstm(embeddings)
        output = self.fc(torch.cat((fcn_output, lstm_output), dim=1))
        return output, fcn_output, lstm_output

