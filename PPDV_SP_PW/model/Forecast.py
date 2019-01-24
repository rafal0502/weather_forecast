from typing import Dict, List

from model.HourForecast import HourForecast
from datetime import datetime

epoch = datetime.utcfromtimestamp(0)


def unix_time_s(dt):
    return (dt - epoch).total_seconds()


class Forecast:

    def __init__(self, data: Dict):
        self.by_hour_forecast: List[HourForecast] = list()
        for hour_forecast in data["list"]:
            self.by_hour_forecast.append(HourForecast(hour_forecast))

    def get_forecast(self, datetime_from, datetime_to) -> List[HourForecast]:
        chosen_forecast = list()
        unix_time_from = unix_time_s(datetime_from)
        unix_time_to = unix_time_s(datetime_to)

        for hour_forecast in self.by_hour_forecast:
            if unix_time_from < hour_forecast.datetime < unix_time_to:
                chosen_forecast.append(hour_forecast)
        return chosen_forecast



