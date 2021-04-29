import datetime
import logging
from time import sleep
from random import randint

from archivator import Archivator
from gismeteo import WeatherParser
from minmax import get_mean_data
from mysql_utils import MysqlConnector
from correct import Corrector
from predictor import Predictor
from utils import read_config, setup_logger, FISHS
from preprocessing import FeaturePreprocessing


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
        self.archivator = Archivator(config=self.config, logger=self.client_log)
        self.preprocessor = FeaturePreprocessing(self.config)


    def predict_(self, data):
        num_extra_dates = self.config['prediction']['num_days'] + 1
        extra_dates = [data[0]['date'] - datetime.timedelta(days=i + 1) for i in range(num_extra_dates)]
        extra_dates = [_.strftime("%Y.%m.%d") for _ in extra_dates]
        mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                               password=self.config['database']['password'],
                               database=self.config['database']['database'])
        response = mysql.select(table_name=self.config['database']['prediction_table'],
                                where={'areal': data[0]['areal'], 'city': data[0]['city'],
                                       'date': extra_dates, 'fish': 'Щука'})
        response = sorted(response, key=lambda x: x['date'])
        predict_data = response + data
        return self.predictor(self.preprocessor(predict_data))

    def handle_(self, city, areal):
        base_url = self.config['urls'][areal][city]
        parser = WeatherParser(config=self.config, logger=self.gismeteo_log)
        data = parser.parse_urls(base_url=base_url)
        corrector = Corrector(self.config_path)
        corrector.correct(data=data)
        for i in range(len(data)):
            data[i]['city'] = city
            data[i]['areal'] = areal
        probs = self.predict_(data)
        for fish in probs:
            if not len(probs[fish]) == self.config['gismeteo']['num_hours'] * len(data):
                extra_ = self.config['gismeteo']['num_hours'] * len(data) - len(probs[fish])
                extra_ = [max(min(probs[fish][0], 100), 0) + randint(-10, 10) for _ in range(extra_)]
                probs[fish] = extra_ + probs[fish]
            for i in range(len(data)):
                data[i]['fish'] = fish
                left = i * self.config['gismeteo']['num_hours']
                right = (i + 1) * self.config['gismeteo']['num_hours']
                data[i]['prob'] = ','.join(list(map(str, probs[fish][left: right])))
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
                mysql.update(table_name=table_name, row=crow)
                del crow['id']
            else:
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
                    sleep(20)
            self.archivator.archive()
            sleep(10800)
            self.config = read_config(self.config_path)
            with open(self.config['current_city'], 'w') as c_f:
                areal = list(urls.keys())[0]
                city = list(urls[areal].keys())[0]
                c_f.write("{},{}".format(areal, city))


if __name__ == '__main__':
    c = Client('/usr/local/bin/spider/config.json')
    c.start()
