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
                                   num_rows=self.config['prediction']['num_days'] * self.config['gismeteo'][
                                       'num_hours'])

    def predict_(self, data):
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
        return self.predictor(predict_data)

    def handle_(self, city, areal):
        base_url = self.config['urls'][areal][city]
        with WeatherParser(config=self.config, logger=self.gismeteo_log) as parser:
            data = parser.parse_urls(base_url=base_url)
            for i in range(len(data)):
                data[i]['city'] = city
                data[i]['areal'] = areal
            probs = self.predict_(data)
            for fish in probs:
                for i in range(len(data)):
                    data[i]['fish'] = fish
                    data[i]['prob'] = ','.join(probs[fish][i: i + self.config['gismeteo']['num_hours']])
                self.write_predictions_(self.config['database']['prediction_table'], data)
                mean_data = get_mean_data(data[:self.config['gismeteo']['num_days'] - 1])
                self.write_predictions_(self.config['database']['mean_prediction_table'], mean_data)
                mean_data = get_mean_data(data[1:self.config['gismeteo']['num_days']])
                self.write_predictions_(self.config['database']['mean_prediction_table'], mean_data)

    def write_predictions_(self, table_name, data):
        mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                               password=self.config['database']['password'],
                               database=self.config['database']['database'])
        for row in data:
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
        urls = self.config['urls']
        for areal in urls:
            for city in urls[areal]:
                self.handle_(city=city, areal=areal)
