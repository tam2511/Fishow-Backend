import datetime

from spider.utils import read_config


class DataError(Exception):
    def __init__(self, *args):
        self.message = args[0]

    def __str__(self):
        return 'DataError: {}'.format(self.message)


class Corrector:
    def __init__(self, config_path):
        self.config = read_config(config_path)
        try:
            from spider.mysql_utils import MysqlConnector
            self.mysql = MysqlConnector(host=self.config['database']['host'],
                                        username=self.config['database']['username'],
                                        password=self.config['database']['password'],
                                        database=self.config['database']['database'])
        except Exception:
            self.mysql = None

    def correct_mysql_(self, data, key, idx):
        date = data[idx]['date']
        city = data[idx]['city']
        extra_data = self.mysql.select(table_name='prediction_prediction',
                                       where={'date': [date, date + datetime.timedelta(days=1)], 'city': city})

        if len(extra_data) == 0:
            raise DataError('DataError: can\'t find data in table for date = {}, city = .'.format(date, city))

    def correct_(self, data, key):
        if not data[0][key]:
            if not self.mysql:
                raise DataError('Don\'t find key {} for first day and mysql corrector.'.format(key))
            else:
