import json


def read_config(config_path):
    with open(config_path, 'r', encoding='UTF-8') as config_file:
        return json.load(config_file)


def average_time(left_time, right_time):
    time1 = left_time.split(':')
    time2 = right_time.split(':')
    time1 = int(time1[0]) * 60 + int(time1[1])
    time2 = int(time2[0]) * 60 + int(time2[1])
    mean_time = (time2 - time1) // 2 + time1
    mean_time = ':'.join(map(str, [mean_time // 60, mean_time % 60]))
    return mean_time
