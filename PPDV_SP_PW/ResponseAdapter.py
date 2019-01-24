import json
import pickle
from typing import List

import requests

from model.City import City
from model.HourForecast import HourForecast


class ResponseAdapter:
    def __init__(self):
        self.updated_cities = None

    def get_forecast_data(self, cities: List):
        if self.updated_cities is not None:
            return pickle.loads(self.updated_cities)
        else:
            updated_cities: List[City] = list()
            for city in cities:
                url = 'http://api.openweathermap.org/data/2.5/forecast'

                params = dict(
                    id=city["id"],
                    APPID='8cd51f46447ea2ce220ddce9e3265007'
                )

                resp = requests.get(url=url, params=params)
                new_city = City(resp.json())
                city = self.add_current_weather_conditions(new_city)
                updated_cities.append(city)

            # TODO: add resp code check
            self.updated_cities = pickle.dumps(updated_cities)
            return updated_cities

    def get_basic_forecast_data(self):
        with open('input_data_config.json') as f:
            data = json.load(f)
        return self.get_forecast_data(data["cities"])

    def add_current_weather_conditions(self, city: City):
        url = 'http://api.openweathermap.org/data/2.5/weather'

        params = dict(
            id=city.city_id,
            APPID='8cd51f46447ea2ce220ddce9e3265007'
        )
        resp = requests.get(url=url, params=params)
        hour_forecast = HourForecast(resp.json())
        addition: List[HourForecast] = list()
        addition.append(hour_forecast)
        city.forecast.by_hour_forecast = addition + city.forecast.by_hour_forecast
        return city
