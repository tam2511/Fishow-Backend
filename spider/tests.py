from spider.gismeteo import WeatherParser
from spider.minmax import minmax_temperature


def main():
    import logging
    logging.basicConfig(level=logging.INFO)
    config_path = 'config.json'
    url_base = 'https://www.gismeteo.ru/weather-mamayeva-235014/'
    with WeatherParser(config_path=config_path, logger=logging) as parser:
        result = parser.parse_urls(url_base)
        print(result)
        for _ in result:
            print(minmax_temperature(_))

if __name__ == '__main__':
    main()