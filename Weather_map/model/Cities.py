class City:
    def __init__(self, data):
        self.city_id: int = data["city"]["id"]
        self.name: str = data["city"]["name"]
        self.latitude: float = data["city"]["coord"]["lat"]
        self.longitude: float = data["city"]["coord"]["lon"]

