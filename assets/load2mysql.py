import pymysql
import pickle
from tqdm import tqdm
import os
from json import load

config_path = ""
data_path = ""

with open(config_path, 'r') as f:
    config = load(f)


with open(data_path, 'wb') as f:
    data = pickle.load(f)

print(data)