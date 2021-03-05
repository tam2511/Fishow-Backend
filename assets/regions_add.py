from pytils.translit import slugify
from rest_framework.generics import get_object_or_404
from tqdm import tqdm
from fishow_django.core.utils import generate_random_string
from fishow_django.space.models import Region, Waterplace_nature
import pymysql
from mysql_utils import MysqlConnector
import pandas as pd
from json import load


def get_waterplace_slug(type, name):
    slug1 = slugify(type)
    slug2 = slugify(name)
    random_string = generate_random_string()
    return slug1 + '-' + slug2 + '-' + random_string


# curr_region = get_object_or_404(Region, slug='')
# curr_waterplace_nature = get_object_or_404(Waterplace_nature, slug='').region_list.add(curr_region)
config_path = "/root/Fishow/fishow_rest_vue/fishow_django/fishow_django/config.json"
data_path = "/tmp/timofeev/regions_v1.csv"

with open(config_path, 'r') as f:
    config = load(f)

connector = MysqlConnector(database=config['database_name'], password=config['password'], host="localhost",
                           username=config['user'])
data = pd.read_csv(data_path).values

for i in tqdm(range(len(data))):
    row = {
        'name': data[i][0],
        'stat': data[i][1],
        'sities': data[i][2]
    }
    connector.insert_row('space_region', row)
