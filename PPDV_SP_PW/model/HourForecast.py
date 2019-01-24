from datetime import datetime
from typing import Dict

from model.Weather import WeatherDetails


def to_celsius(kelvin_degrees: float) -> float:
    return kelvin_degrees - 273.15


class HourForecast:
    def __init__(self, hour_prediction: Dict):
        self.datetime = hour_prediction["dt"]
        try:
            self.datetime_txt = hour_prediction["dt_txt"]
        except KeyError:
            self.datetime_txt = datetime.utcfromtimestamp(self.datetime).strftime('%Y-%m-%d %H:%M:%S')
        self.temp: float = to_celsius(hour_prediction["main"]["temp"])
        self.temp_min: float = to_celsius(hour_prediction["main"]["temp_min"])
        self.temp_max: float = to_celsius(hour_prediction["main"]["temp_max"])
        self.pressure: float = hour_prediction["main"]["pressure"]
        try:
            self.sea_level: float = hour_prediction["main"]["sea_level"]
            self.grnd_level: float = hour_prediction["main"]["grnd_level"]
        except KeyError:
            self.sea_level = self.pressure
            self.grnd_level = self.pressure
        self.humidity: int = hour_prediction["main"]["humidity"]
        self.weather_details: WeatherDetails = WeatherDetails(hour_prediction["weather"])
        self.cloud_percentage: int = hour_prediction["clouds"]["all"]
        self.wind_speed: float = hour_prediction["wind"]["speed"]
        self.wind_direction: float = hour_prediction["wind"]["deg"]
        try:
            self.rain_in_last_3_hours: float = hour_prediction["rain"]["3h"]
        except KeyError:
            self.rain_in_last_3_hours: float = 0.0
        try:
            self.snow_in_last_3_hours: float = hour_prediction["snow"]["3h"]
        except KeyError:
            self.snow_in_last_3_hours: float = 0.0
