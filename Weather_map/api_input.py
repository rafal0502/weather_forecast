from typing import List

import GetForecast
from model.Cities import City


class InputOperations:
    def __init__(self, adapter: GetForecast):
        data: List[City] = adapter.get_basic_forecast_data()
        self.cities_names = [city.name for city in data]
        self.possible_dates = [forecast.datetime_txt for forecast in data[0].forecast.by_hour_forecast]

