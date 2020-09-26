import datetime
import logging

from spider.gismeteo import WeatherParser
from spider.minmax import get_mean_data
from spider.mysql_utils import MysqlConnector
from spider.predictor import Predictor
from spider.utils import read_config, setup_logger, FISHS


class Client:
    def __int__(self, config_path):
        self.config = read_config(config_path)
        setup_logger('gismeteo', self.config['log']['gismeteo'])
        setup_logger('predict', self.config['log']['predict'])
        setup_logger('client', self.config['log']['client'])
        self.gismeteo_log = logging.getLogger('gismeteo')
        self.predict_log = logging.getLogger('predict')
        self.client_log = logging.getLogger('client')
        self.client_log.propagate = False
        self.predictor = Predictor(self.config['model_path'], self.predict_log,
                                   num_rows=self.config['prediction']['num_days'] * self.config['gismeteo']['num_hours'])

    def predict_(self, data, requered_extra=False):
        if requered_extra:
            num_extra_dates = self.config['prediction']['num_days'] - len(data)
            extra_dates = [data[0]['date'] - datetime.timedelta(days=i) for i in range(num_extra_dates)]
            mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                                   password=self.config['database']['password'],
                                   database=self.config['database']['database'])
            response = mysql.select(table_name=self.config['database']['table_name1'],
                                    where={'areal': data[0]['areal'], 'city': data[0]['city'],
                                           'date': extra_dates, 'fish': data[0]['fish']})
            response = sorted(response, key=lambda x: x['date'])
            predict_data = response + data
        else:
            predict_data = data
        return self.predictor(data)

    def handle_(self, city, areal):
        base_url = self.config['urls'][areal][city]
        with WeatherParser(config=self.config, logger=self.gismeteo_log) as parser:
            data = parser.parse_urls(base_url=base_url)
            mean_data = get_mean_data(data)
            all_data = [data[:] for _ in range(FISHS)]
            all_mean_data = [mean_data[:] for _ in range(FISHS)]
            for fish_idx, fish in enumerate(FISHS):
                for i in range(len(all_data[fish_idx])):
                    all_data[fish_idx][i]['city'] = city
                    all_data[fish_idx][i]['areal'] = areal
                    all_data[fish_idx][i]['fish'] = fish
                    if i > 1:
                        all_data[fish_idx][i]['prob'] = self.predict_(all_data[fish_idx][i])
                    else:
                        all_data[fish_idx][i]['prob'] = self.predict_(all_data[fish_idx][i], requered_extra=True)
                min_pro


    def write_predictions_(self, table_name, row):
        mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                               password=self.config['database']['password'],
                               database=self.config['database']['database'])
        response = mysql.select(table_name=table_name, where={'areal': row['areal'], 'city': row['city'],
                                                              'date': row['date'], 'fish': row['fish']})
        if len(response) > 0:
            row['id'] = response[0]['id']
            mysql.update(table_name=table_name, row=row)
            del row['id']
        else:
            mysql.insert_row(table_name=table_name, row=row)
        mysql.close()

    def start(self):
        pass
