import os

import argparse
import pymysql

from json import load


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser(description='Script for manipulation with database.')
parser.add_argument('--cp', type=str, metavar='config_path', nargs=1,
                    help='path to config file(.json), default: "../fishow_django/fishow_django/config.json"',
                    default="../fishow_django/fishow_django/config.json")
parser.add_argument('--ddb', type=str2bool, metavar='delete_db', nargs=1,
                    help='if True database will be deleted, else if False database will not be deleted, default: False',
                    default=False)
parser.add_argument('--cdb', type=str2bool, metavar='create_db', nargs=1,
                    help='if True database will be created, else if False database will not be created, default: False',
                    default=False)
parser.add_argument('--mdb', type=str2bool, metavar='migrate_db', nargs=1,
                    help='if True database will be migrated, else if False database will not be migrated, default: False',
                    default=False)
parser.add_argument('--pv', type=str, metavar='python_version', nargs=1,
                    help='python version, default: python3',
                    default='python3')

args = parser.parse_args()
config_path = args.cp[0] if isinstance(args.cp, list) else args.cp
delete_db = args.ddb[0] if isinstance(args.ddb, list) else args.ddb
create_db = args.cdb[0] if isinstance(args.cdb, list) else args.cdb
migrate_db = args.mdb[0] if isinstance(args.mdb, list) else args.mdb
python_version = args.pv[0] if isinstance(args.pv, list) else args.pv

with open(config_path, 'r') as f:
    config = load(f)

# DROP DATABASE
if delete_db:
    print('Start droping database {}...'.format(config['database_name']))
    try:
        con = pymysql.connect('localhost', config['user'], config['password'])
        cur = con.cursor()
        query = ('DROP DATABASE {};'.format(config['database_name']))
        cur.execute(query)
        print('OK: database is dropped.')
    except Exception as e:
        print(e)
        print('Impossible connect with user={} and password={}'.format(config['user'], config['password']))

# CREATE DATABASE
if create_db:
    print('Start creating database {}...'.format(config['database_name']))
    try:
        con = pymysql.connect('localhost', config['user'], config['password'])
        cur = con.cursor()
        query = ('CREATE DATABASE {};'.format(config['database_name']))
        cur.execute(query)
        print('OK: database is creating.')
    except Exception as e:
        print(e)
        print('Impossible connect with user={} and password={}'.format(config['user'], config['password']))

# MIGRATE DATABASE
if migrate_db:
    print('Start migrate database {}...'.format(config['database_name']))
    try:
        os.system('cd ../fishow_django')
        os.system('{} manage.py migrate --run-syncdb'.format(python_version))
        os.system('cd ../assets')
        os.system('cd ../fishow_django')
        os.system('python3 manage.py migrate')
        os.system('cd ../assets')
        print('OK: database is migrated.')
    except Exception as e:
        print(e)
