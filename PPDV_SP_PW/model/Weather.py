from typing import Dict


class WeatherDetails:

    def __init__(self, data: Dict):
        self.weather_id: int = data[0]["id"]
        self.main: str = data[0]["main"]
        self.description: str = data[0]["description"]
        self.icon: str = data[0]["icon"]
