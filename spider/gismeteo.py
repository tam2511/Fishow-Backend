import re

from selenium import webdriver
import selenium
import datetime
from time import sleep, time

from utils import read_config


class WeatherParser:
    def __init__(self, config, logger):
        self.config = config
        self.num_days = self.config['gismeteo']['num_days']
        self.logger = logger
        self.driver_path = self.config['gismeteo']['driver_path']
        self.num_attempts = self.config['gismeteo']['num_attempts']
        self.timeout = self.config['gismeteo']['timeout']
        self.max_wait = self.config['gismeteo']['max_wait']

    def init(self):
        self.driver = webdriver.PhantomJS(executable_path=self.driver_path)
        self.driver.implicitly_wait(self.max_wait)

    def close(self):
        self.driver.close()
        del self.driver

    def temperature_(self, driver):
        temps = driver.find_elements_by_class_name('unit_temperature_c')[-8:]
        temps = ','.join([_.text.replace('−', '-') for _ in temps])
        return {'temperature': temps}

    def wind_(self, driver):
        winds = driver.find_elements_by_class_name('unit_wind_m_s')
        if len(winds) > 20:
            winds = winds[-16:-8]
        else:
            winds = winds[-8:]
        winds = ','.join([_.text for _ in winds])
        return {'wind': winds}

    def gust_(self, driver):
        gusts = driver.find_elements_by_class_name('unit_wind_m_s')[-8:]
        gusts = ','.join([_.text.replace('—', '0') for _ in gusts])
        return {'gust': gusts}

    def wind_direction_(self, driver):
        winds_derections = driver.find_elements_by_class_name('w_wind__direction')
        winds_derections = ','.join([_.text.strip() for _ in winds_derections])
        return {'wind_direction': winds_derections}

    def phenomenon_(self, driver):
        phenomenon = driver.find_elements_by_class_name('tooltip')[3:11]
        phenomenon = [_.get_attribute("data-text").strip().lower().replace('&nbsp;', ' ').split(',') for _ in
                      phenomenon]
        for i in range(len(phenomenon)):
            for j in range(len(phenomenon[i])):
                phenomenon[i][j] = phenomenon[i][j].strip()
            phenomenon[i] = '.'.join(phenomenon[i])
        phenomenon = ','.join(phenomenon)
        return {'phenomenon': phenomenon}

    def pressure_(self, driver):
        pressure = driver.find_elements_by_class_name('unit_pressure_mm_hg_atm')[-8:]
        pressure = ','.join([_.text for _ in pressure])
        return {'pressure': pressure}

    def humidity_(self, driver):
        humidity = driver.find_elements_by_class_name('w-humidity')
        humidity = ','.join([_.text for _ in humidity])
        return {'humidity': humidity}

    def uv_index_(self, driver):
        UV_index = driver.find_element_by_class_name('widget__row_uvb').find_elements_by_class_name(
            'widget__value')
        UV_index = [_.text.replace('—', '0') for _ in UV_index]
        if len(UV_index) == 0:
            UV_index = ['0', '0', '0', '1', '2', '1', '0', '0']
        UV_index = ','.join(UV_index)
        return {'uv_index': UV_index}

    def moon_(self, driver):
        moon = driver.find_element_by_class_name('_moon').find_element_by_class_name('title').text
        moon = moon.strip().lower().split(',')
        moon_desc = {'moon': None, 'moon_direction': None}
        if moon[0].find('растущ') > -1:
            moon_desc['moon_direction'] = 1
            moon_desc['moon'] = int(moon[1].replace('%', ''))
        elif moon[0].find('стар') > -1:
            moon_desc['moon_direction'] = -1
            moon_desc['moon'] = int(moon[1].replace('%', ''))
        else:
            moon_desc['moon_direction'] = 0
            moon_desc['moon'] = 0
        return moon_desc

    def sun_(self, driver):
        sun = driver.find_element_by_class_name('_sun').find_elements_by_class_name('id_item')[1:]
        sun = [_.text.split(':') for _ in sun]
        for i in range(len(sun)):
            sun[i][0] = re.sub('\D', '', sun[i][0])
            sun[i][1] = re.sub('\D', '', sun[i][1])
            sun[i] = ':'.join(sun[i])
        return {'sun_up': sun[0], 'sun_down': sun[1]}

    def parse_page_(self, driver):
        res = {'temperature': None, 'wind': None, 'wind_direction': None, 'gust': None, 'phenomenon': None,
               'pressure': None, 'humidity': None, 'uv_index': None, 'moon': None, 'moon_direction': None,
               'sun_up': None, 'sun_down': None}
        methods = [self.temperature_, self.wind_, self.wind_direction_, self.gust_, self.pressure_, self.phenomenon_,
                   self.moon_, self.sun_, self.humidity_, self.uv_index_]
        for i in range(len(methods)):
            try:
                subres = methods[i](driver)
                res.update(subres)
            except Exception as e:
                self.logger.error('Error until parsing {}. Message: {}'.format(str(methods[i]), e))
                raise ValueError
        return res

    def parse_urls(self, base_url):
        urls = [base_url, base_url + 'tomorrow/'] + [base_url + '{}-day/'.format(day) for day in
                                                     range(3, self.num_days + 1)]
        today = datetime.datetime.today()
        dates = [today + datetime.timedelta(days=i) for i in range(self.num_days)]
        result = []
        for i, url in enumerate(urls):
            self.logger.info('Start parsing url: {}'.format(url))
            start_time = time()
            step = 0
            while step < self.num_attempts:
                try:
                    sleep(self.timeout)
                    self.init()
                    self.driver.get(url)
                    driver = self.driver.find_element_by_class_name('__frame_sm')
                    break
                except Exception as e:
                    self.logger.error("Exception request for url {} on step {} : {}".format(url, step, e))
                    step += 1
            if step == self.num_attempts:
                self.close()
                return None
            self.logger.info('Url {} parsed. Elapsed time: {}'.format(url, time() - start_time))
            try:
                res = self.parse_page_(driver)
            except Exception:
                self.close()
                return None
            self.close()
            res.update({'date': dates[i]})
            result.append(res)
        return result

