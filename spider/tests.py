from spider.correct import Corrector
from spider.gismeteo import WeatherParser
from spider.minmax import get_mean_data
from spider.predictor import Predictor
from spider.utils import read_config


def main():
    import logging
    logging.basicConfig(level=logging.INFO)
    config_path = 'config.json'
    config = read_config(config_path)
    url_base = 'https://www.gismeteo.ru/weather-mamayeva-235014/'
    with WeatherParser(config=config, logger=logging) as parser:
        result = parser.parse_urls(url_base)
        for idx, res in enumerate(result):
            print('{}: {}'.format(idx, res))
        # for key in result[1]:
        #     result[1][key] = None
        corrector = Corrector(config_path)
        corrector.correct(data=result)
        for idx, res in enumerate(result):
            result[idx]['areal'] = 'Московская область'
            print('{}: {}'.format(idx, res))
        mean_result = get_mean_data(result)
        print(mean_result)

        predictor = Predictor('', None, num_days=3, num_hours=8)

        probs = predictor(result)

        print(probs)


if __name__ == '__main__':
    main()