from pytils.translit import slugify
from django.conf import settings
import django

settings.configure()
django.setup()
from rest_framework.generics import get_object_or_404
from tqdm import tqdm
from core.utils import generate_random_string
from space.models import Region, Waterplace_nature
import pymysql
from mysql_utils import MysqlConnector
import pandas as pd
from json import load, loads


def get_waterplace_slug(type_, name):
    slug1 = slugify(type_)
    slug2 = slugify(name)
    random_string = generate_random_string()
    return slug1 + '-' + slug2 + '-' + random_string


# curr_region = get_object_or_404(Region, slug='')
# curr_waterplace_nature = get_object_or_404(Waterplace_nature, slug='').region_list.add(curr_region)
config_path = "/root/Fishow/fishow_rest_vue/fishow_django/fishow_django/config.json"
data_path = "/tmp/timofeev/regions_v2.csv"

with open(config_path, 'r') as f:
    config = load(f)

connector = MysqlConnector(database=config['database_name'], password=config['password'], host="localhost",
                           username=config['user'])
data = pd.read_csv(data_path).values

for i in tqdm(range(len(data))):
    slug = slugify(data[i][0])
    random_string = generate_random_string()
    slug = slug + '-' + random_string
    row = {
        'name': data[i][0],
        'stat': data[i][1],
        'sities': data[i][2],
        'slug': slug
    }
    waterplaces = loads(data[i][3])
    # for waterplace in waterplaces:
    #     curr_region = Waterplace_nature.objects.get(name=waterplace['waterplace'])
        # curr_region = get_object_or_404(Waterplace_nature, name=waterplace['waterplace'], type=waterplace['type'])
    #     print(curr_region)
    # print(waterplaces)
    # break
    connector.insert_row('space_region', row)
