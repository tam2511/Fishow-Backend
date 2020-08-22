import pymysql
from datetime import datetime


def serialize_value(value):
    if isinstance(value, str):
        temp = value.replace("'", "\\'")
        temp = "'{}'".format(temp)
    else:
        temp = value
    return temp


def serialize_key(key):
    return "`{}`".format(key)


class MysqlConnector:
    def __init__(self, username, password, host, database):
        self.connector = pymysql.connect(host, username, password, database)

    def escape_name(self, s):
        return '`{}`'.format(s.replace('`', '``'))

    def insert_row(self, table_name, row):
        new_row = {key: row[key] for key in row}
        if isinstance(row['date'], str):
            new_row['date'] = datetime.strptime(row['date'], '%Y-%m-%d')
        names = list(new_row)
        cols = ', '.join(map(self.escape_name, names))
        placeholders = ', '.join(['%({})s'.format(name) for name in names])
        query = 'INSERT INTO {} ({}) VALUES ({})'.format(table_name, cols, placeholders)
        #with self.connector:
        cur = self.connector.cursor()
        cur.execute(query, new_row)
        self.connector.commit()

    def select(self, table_name, where=None):
        if where:
            query = "SELECT * FROM {} WHERE".format(table_name)
            for key in where:
                if isinstance(where[key], list):
                    if len(where[key]) > 0:
                        query += " {} IN ({}".format(serialize_key(key), serialize_value(where[key][0]))
                        for index in range(1, len(where[key])):
                            query += ", {}".format(serialize_value(where[key][index]))
                        query += ") AND"
                else:
                    query += " {} = {} AND".format(serialize_key(key), serialize_value(where[key]))
            query = query[:-3]
        else:
            query = "SELECT * FROM {}".format(table_name)
        with self.connector:
            cur = self.connector.cursor(pymysql.cursors.DictCursor)
            cur.execute(query)
            return cur.fetchall()

    def update(self, table_name, row):
        id = row['id']
        data_row = {key: row[key] for key in row if not key == 'date'}
        query = "UPDATE {} SET ".format(table_name)
        for key in data_row:
            query += "{} = {}, ".format(serialize_key(key), serialize_value(data_row[key]))
        query = query[:-2] + "WHERE id = {}".format(id)
        print(query)
        with self.connector:
            cur = self.connector.cursor()
            cur.execute(query)
