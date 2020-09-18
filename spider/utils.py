import json


def read_config(config_path):
    with open(config_path, 'r', encoding='UTF-8') as config_file:
        return json.load(config_file)
