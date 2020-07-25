import pandas as pd
from mysql_utils import MysqlConnector
from tqdm import tqdm

connector = MysqlConnector("tam2511_fishow", "081099ASDasd", "localhost", "tam2511_fishow")

# data = connector.select('prediction_predictionten')

# for i in range(len(data)):
#     del data[i]['id']

# dt = pd.DataFrame(data)
# dt.to_csv("damir10.csv", sep=';', encoding='utf-8-sig', index=False)

dt = pd.read_csv("damir_ten.csv", sep=';')
data = list(dt.T.to_dict().values())
#connector.truncate_table('prediction_predictionten')
for row in tqdm(data):
    if pd.isnull(row['wind_direction']):
        row['wind_direction'] = '-'
    connector.insert_row('prediction_predictionten', row)

dt = pd.read_csv("damir_one.csv", sep=';')
data = list(dt.T.to_dict().values())
#connector.truncate_table('prediction_prediction')
for row in tqdm(data):
    if pd.isnull(row['wind_direction']):
        row['wind_direction'] = '-'
    connector.insert_row('prediction_prediction', row)
