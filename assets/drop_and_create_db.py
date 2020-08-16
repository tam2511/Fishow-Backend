import pymysql
import os
#ПАРОЛЬ В СЕТТИНГЕ СВОЕМ ПОСМОТРИТЕ И НАПИШИТЕ ('081099ASDasd') или какой-то там у вас

try:
    con = pymysql.connect('localhost', 'tam2511_fishow','081099ASDasd')
    cur = con.cursor()
except:
    try:
        con = pymysql.connect('localhost', 'tam2511_fishow','081099')
        cur = con.cursor()
    except:
        pass
try:
    query = ('DROP DATABASE tam2511_fishow;')
    cur.execute(query)
    print('OK: you drop db')
except:
    print('ERROR: you have not droped db')
try:
    query = ('CREATE DATABASE tam2511_fishow;')
    cur.execute(query)
    print('OK: you create db')
except:
    print('ERROR: you have not created db')

try:
    os.system('cd fishow_django')
    os.system('python3 manage.py migrate --run-syncdb')
    os.system('cd ..')
    print('OK migrate syncdb')
except:
    print('error: migrate syncdb')
    pass
try:
    os.system('cd fishow_django')
    os.system('python3 manage.py migrate')
    os.system('cd ..')
    print('OK migrate')
except:
    print('error: migrate')
    pass
