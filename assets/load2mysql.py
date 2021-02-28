import pymysql
import pickle
from mysql_utils import MysqlConnector
import os
from json import load, dumps
from django.utils.text import slugify

import random
import string

ALPHANUMERIC_CHARS = string.ascii_lowercase + string.digits
STRING_LENGTH = 6


def generate_random_string(chars=ALPHANUMERIC_CHARS, length=STRING_LENGTH):
    return "".join(random.choice(chars) for _ in range(length))


config_path = "/root/Fishow/fishow_rest_vue/fishow_django/fishow_django/config.json"
data_path = "/tmp/timofeev/rivers_stat.json"

with open(config_path, 'r') as f:
    config = load(f)

with open(data_path, 'rb') as f:
    data = pickle.load(f)

connector = MysqlConnector(database=config['database_name'], password=config['password'], host="localhost",
                           username=config['user'])

i = 0
while True:
    row = data[i]
    slug = slugify(row['name'])
    random_string = generate_random_string()
    slug = slug + '-' + random_string
    if 'stat' in row:
        rows = data[i:i + 12]
        row = {
            'name': row['name'],
            'type': row['type'],
            'stat': dumps({
                'main': {'x': [_['month'] + 1 for _ in rows], 'y': [_['stat'] for _ in rows]}
            }),
            'slug': slug
        }
        connector.insert_row('space_waterplace_nature', row)
        i += 12
    else:
        row = {
            'name': row['name'],
            'type': row['type'],
            'slug': slug
        }
        if row['name']:
            connector.insert_row('space_waterplace_nature', row)
        i += 1

    if i >= len(data):
        break
