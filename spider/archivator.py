import datetime
import logging
import json
import os

from mysql_utils import MysqlConnector
from utils import read_config, setup_logger
import zipfile

try:
    import zlib

    COMPRESSION = zipfile.ZIP_DEFLATED
except:
    COMPRESSION = zipfile.ZIP_STORED


class Archivator:
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.path = self.config['database']['archives_path']
        if not os.path.isdir(self.path):
            os.mkdir(self.path)

    def archive(self):
        today_str = datetime.date.today().strftime("%Y_%m_%d")
        shift = self.config['prediction']['num_days'] + 1
        dates = [datetime.date.today() - datetime.timedelta(days=i + 1) for i in range(shift, shift + 5)]
        dates = [_.strftime("%Y.%m.%d") for _ in dates]
        mysql = MysqlConnector(host=self.config['database']['host'], username=self.config['database']['username'],
                               password=self.config['database']['password'],
                               database=self.config['database']['database'])
        response_one = mysql.select(table_name=self.config['database']['prediction_table'],
                                    where={'date': dates})
        response_ten = mysql.select(table_name=self.config['database']['mean_prediction_table'],
                                    where={'date': dates})
        if len(response_one) == 0 and len(response_ten) == 0:
            return
        file = zipfile.ZipFile(os.path.join(self.path, today_str + '.zip'), mode='w')
        try:
            for row in response_one:
                row['date'] = row['date'].strftime("%Y.%m.%d")
                file.writestr("prediction_one.jsonl", json.dumps(row) + '\n')
            self.logger.info(
                'Archived prediction one table for date: {}. Number of lines: {}'.format(today_str, len(response_one)))
            for row in response_ten:
                row['date'] = row['date'].strftime("%Y.%m.%d")
                file.writestr("prediction_ten.jsonl", json.dumps(row) + '\n')
            self.logger.info(
                'Archived prediction ten table for date: {}. Number of lines: {}'.format(today_str, len(response_ten)))
        finally:
            file.close()
        mysql.delete(table_name=self.config['database']['prediction_table'],
                     where={'date': dates})
        self.logger.info('Delete rows of prediction one table for dates in {}'.format(dates))
        mysql.delete(table_name=self.config['database']['mean_prediction_table'],
                     where={'date': dates})
        self.logger.info('Delete rows of prediction ten table for dates in {}'.format(dates))
