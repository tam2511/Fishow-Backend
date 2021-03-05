from pytils.translit import slugify
from django.conf import settings
import django

settings.configure()
django.setup()
from rest_framework.generics import get_object_or_404
from tqdm import tqdm
from core.utils import generate_random_string
from space.models import Region, Waterplace_nature
##from users.models import CustomUser
import pymysql
from mysql_utils import MysqlConnector
import pandas as pd
from json import load


def get_waterplace_slug(type_, name):
    slug1 = slugify(type_)
    slug2 = slugify(name)
    random_string = generate_random_string()
    return slug1 + '-' + slug2 + '-' + random_string


# curr_region = get_object_or_404(Region, slug='')
# curr_waterplace_nature = get_object_or_404(Waterplace_nature, slug='').region_list.add(curr_region)
config_path = "/root/Fishow/fishow_rest_vue/fishow_django/fishow_django/config.json"
data_path = "/tmp/timofeev/waterplaces_v2.csv"

with open(config_path, 'r') as f:
    config = load(f)

connector = MysqlConnector(database=config['database_name'], password=config['password'], host="localhost",
                           username=config['user'])
data = pd.read_csv(data_path).values
##print(get_object_or_404(CustomUser, username= "tam2512"))
for i in tqdm(range(len(data))):
    row = {
        'name': data[i][0],
        'type': data[i][1],
        'stat': data[i][2] if not pd.isnull(data[i][2]) else "{}",
        'slug': get_waterplace_slug(data[i][1], data[i][0])
    }
    connector.insert_row('space_waterplace_nature', row)
