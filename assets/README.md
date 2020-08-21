# Вспомогательные утилиты для работы с сайтом

## drop_and_create_db

Для того, чтобы скрипт корректно работал с базой данный необходимо,
 чтобы в конфиг файле (*./fishow_django/config.json*) были следующие поля:
 * **database_name** - название базы данных (*tam2511_fishow*)
 * **password** - пароль пользователя (*081099ASDasd*)
 * **user** - имя пользователя (*tam2511_fishow*)
 
Если нужно записать данные в файл в папке *./assets* дожны лежать два файла *damir10.csv*, *damirone.py*.
 А так же в этой папке должен присутствовать файл *mysql_utils.py*.
 
Интерфейс программы выглядит следующим образом:

```
usage: drop_and_create_db.py [-h] [--cp config_path] [--ddb delete_db]
                             [--cdb create_db] [--mdb migrate_db]
                             [--pv python_version] [--fp fill_prediction]

Script for manipulation with database.

optional arguments:
  -h, --help            show this help message and exit
  --cp config_path      path to config file(.json), default:
                        "../fishow_django/fishow_django/config.json"
  --ddb delete_db       if True database will be deleted, else if False
                        database will not be deleted, default: False
  --cdb create_db       if True database will be created, else if False
                        database will not be created, default: False
  --mdb migrate_db      if True database will be migrated, else if False
                        database will not be migrated, default: False
  --pv python_version   python version, default: python3
  --fp fill_prediction  if True prediction table will be migrated, else if
                        False prediction table will not be migrated, default:
                        False
```

Примеры использования:
* Заполняет таблицы прогноза для базы данных, указанной в файле *your_config_path/config.json*, используя версию питон
 команд - *python2*.
```
python3 drop_and_create_db.py -cp your_config_path/config.json --pv python2 --fp True
```

* Сносит, создает и мигрирует базу данных. Использует версию питон команд - *python3* (по умолчанию).
```
python3 drop_and_create_db.py --ddb True --cdb True --mdb True
```

* Делает все итерации, что выше.
```
python3 drop_and_create_db.py --ddb True --cdb True --mdb True -cp your_config_path/config.json --pv python3 --fp True
```