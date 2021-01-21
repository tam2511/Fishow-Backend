import datetime
import logging
from time import sleep

from gismeteo import WeatherParser
from minmax import get_mean_data
from mysql_utils import MysqlConnector
from predictor import Predictor
from utils import read_config, setup_logger, FISHS


class Client:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = read_config(config_path)
        setup_logger('gismeteo', self.config['log']['gismeteo'])
        setup_logger('predict', self.config['log']['predict'])
        setup_logger('client', self.config['log']['client'])
        self.gismeteo_log = logging.getLogger('gismeteo')
        self.predict_log = logging.getLogger('predict')
        self.client_log = logging.getLogger('client')
        self.client_log.propagate = False
        self.predictor = Predictor(model_path=self.config['prediction']['model_path'], logger=self.predict_log,
                                   num_days=self.config['prediction']['num_days'],
                                   num_hours=self.config['gismeteo']['num_hours'])

    def predict_(self, data):
        num_extra_dates = self.config['prediction']['num_days'] - len(data)
        extra_dates = [data[0]['date'] - datetime.timedelta(days=i) for i in range(num_extra_dates)]
        extra_dates = [_.strftime("%Y.%m.%d") for _ in extra_dates]
        mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                               password=self.config['database']['password'],
                               database=self.config['database']['database'])
        response = mysql.select(table_name=self.config['database']['prediction_table'],
                                where={'areal': data[0]['areal'], 'city': data[0]['city'],
                                       'date': extra_dates, 'fish': 'щука'})
        response = sorted(response, key=lambda x: x['date'])
        predict_data = response + data
        return self.predictor(predict_data)

    def handle_(self, city, areal):
        base_url = self.config['urls'][areal][city]
        parser = WeatherParser(config=self.config, logger=self.gismeteo_log)
        data = parser.parse_urls(base_url=base_url)
        for i in range(len(data)):
            data[i]['city'] = city
            data[i]['areal'] = areal
        probs = self.predict_(data)
        for fish in probs:
            for i in range(len(data)):
                data[i]['fish'] = fish
                data[i]['prob'] = ','.join(list(map(str, probs[fish][i: i + self.config['gismeteo']['num_hours']])))
            self.write_predictions_(self.config['database']['prediction_table'], data)
            mean_data = get_mean_data(data[:self.config['gismeteo']['num_days'] - 1])
            self.write_predictions_(self.config['database']['mean_prediction_table'], [mean_data])
            mean_data = get_mean_data(data[1:self.config['gismeteo']['num_days']])
            self.write_predictions_(self.config['database']['mean_prediction_table'], [mean_data])

    def write_predictions_(self, table_name, data):
        mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                               password=self.config['database']['password'],
                               database=self.config['database']['database'])
        for row in data:
            crow = row.copy()
            crow['date'] = crow['date'].strftime('%Y.%m.%d')
            response = mysql.select(table_name=table_name, where={'areal': crow['areal'], 'city': crow['city'],
                                                                  'date': crow['date'], 'fish': crow['fish']})
            if len(response) > 0:
                crow['id'] = response[0]['id']
                print('updating')
                mysql.update(table_name=table_name, row=crow)
                del crow['id']
            else:
                print('inserting')
                mysql.insert_row(table_name=table_name, row=crow)

    def start(self):
        while True:
            flag_start = False
            urls = self.config['urls']
            for areal in urls:
                for city in urls[areal]:
                    if flag_start:
                        with open(self.config['current_city'], 'w') as c_f:
                            c_f.write("{},{}".format(areal, city))
                    else:
                        with open(self.config['current_city'], 'r') as c_f:
                            self.current_city = c_f.readline().strip().split(',')
                        if not city == self.current_city[1] or not areal == self.current_city[0]:
                            self.client_log.info(
                                "Passing {} Current areal: {}, city: {}.".format(city, self.current_city[0],
                                                                                 self.current_city[1]))
                            continue
                        else:
                            flag_start = True
                    self.client_log.info("Start handle areal {} and city {}".format(areal, city))
                    self.handle_(city=city, areal=areal)
                    sleep(7)
            sleep(1000)
            self.config = read_config(self.config_path)
            
            
if __name__ == '__main__':
    c = Client('config.json')
    c.start()
