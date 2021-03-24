import datetime
import logging
from time import sleep
from random import randint

from mysql_utils import MysqlConnector
from utils import read_config, setup_logger


class Client:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = read_config(config_path)
        setup_logger('main_statistics', self.config['main_statistics']['log'])
        self.log = logging.getLogger('main_statistics')
        self.mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                                    password=self.config['database']['password'],
                                    database=self.config['database']['database'])

    def update_(self):
        article_count = self.mysql.length(self.config['database']['article_table'])
        report_count = self.mysql.length(self.config['database']['report_table'])
        user_count = self.mysql.length(self.config['database']['user_table'])
        if self.mysql.length(self.config['database']['target_table']) == 0:
            self.mysql.insert_row(self.config['database']['target_table'], {
                'prediction_quality_current': '75',
                'prediction_quality_old': '73',
                'count_reports': str(report_count),
                'count_blogs': str(article_count),
                'counts_users': str(user_count),
            })
            return
        data = self.mysql.select(self.config['database']['target_table'])[0]
        data.update({
            'count_reports': str(report_count),
            'count_blogs': str(article_count),
            'counts_users': str(user_count),
        })
        self.mysql.update(self.config['database']['target_table'], data)

    def start(self):
        while True:
            self.update_()
            sleep(self.config['main_statistics']['timeout'])
            self.config = read_config(self.config_path)

if __name__ == '__main__':
    c = Client('config.json')
    c.start()
