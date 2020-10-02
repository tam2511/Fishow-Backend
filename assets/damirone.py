import pandas as pd
from mysql_utils import MysqlConnector

connector = MysqlConnector("tam2511_fishow", "081099", "localhost", "tam2511_fishow")

# data = connector.select('prediction_predictionten')

# for i in range(len(data)):
#     del data[i]['id']

# dt = pd.DataFrame(data)
# dt.to_csv("damir10.csv", sep=';', encoding='utf-8-sig', index=False)

dt = pd.read_csv("./daa/damir_.csv", sep=';')
data = list(dt.T.to_dict().values())

for row in data:
    #try:
    connector.insert_row('prediction_prediction', row)
    #except Exception:
    #    print(row)
    #    break
