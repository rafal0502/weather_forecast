import json
import pickle
from typing import List

import requests

from model.Cities import City
import API

class GetForecast:

    def get_forecast_data(self, cities: List):
            for city in cities:
                url = 'http://api.openweathermap.org/data/2.5/forecast'

                params = dict(
                    id=city["id"],
                    APPID=API.api_key
                )

                resp = requests.get(url=url, params=params)
                new_City = resp.json()

            return new_City



    def get_basic_forecast_data(self):
        with open('data_config.json') as f:
            data = json.load(f)
        return self.get_forecast_data(data["cities"])

