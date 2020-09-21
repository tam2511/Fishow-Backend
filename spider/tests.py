from spider.correct import Corrector
from spider.gismeteo import WeatherParser
from spider.minmax import get_mean_data


def main():
    import logging
    logging.basicConfig(level=logging.INFO)
    config_path = 'config.json'
    url_base = 'https://www.gismeteo.ru/weather-mamayeva-235014/'
    with WeatherParser(config_path=config_path, logger=logging) as parser:
        result = parser.parse_urls(url_base)
        print(result)
        for key in result[1]:
            result[1][key] = None
        corrector = Corrector(config_path)
        corrector.correct(data=result)
        print(result)
        mean_result = get_mean_data(result)
        print(mean_result)


if __name__ == '__main__':
    main()