from typing import List

import ResponseAdapter
from model.City import City


class InputOperations:
    def __init__(self, adapter: ResponseAdapter):
        data: List[City] = adapter.get_basic_forecast_data()
        self.cities_names = [city.name for city in data]
        self.possible_dates = [forecast.datetime_txt for forecast in data[0].forecast.by_hour_forecast]


