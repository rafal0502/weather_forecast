import json
import pickle
from typing import List

import requests

from model.Cities import City
import API

class GetForecast:

    def get_forecast_for_city(self, city_name):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, API.api_key)
        resp = requests.get(url=url)
        data = resp.json()
        return data




    def get_forecast_data(self, cities: List):
            for city in cities:
                url = 'http://api.openweathermap.org/data/2.5/forecast'

                params = dict(
                    id=city["id"],
                    APPID=API.api_key
                )

                resp = requests.get(url=url, params=params)
                weather = resp.json()

            return weather



    def get_basic_forecast_data(self):
        with open('data_config.json') as f:
            data = json.load(f)
        return self.get_forecast_data(data["cities"])

