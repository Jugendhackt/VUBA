class Coordinates:
    lon: float
    lat: float

    def __init__(self, lon: float, lat: float) -> None:
        super().__init__()
        self.lon = lon
        self.lat = lat


class Bike:
    coordinates: Coordinates
    provider: str
    accuracy: float
    additional_info: str
    bike_id: str
    is_stationary: bool
    station_id: str

    def __init__(self, lon: float, lat: float, provider: str, accuracy: float, additional_info: str,
                 bike_id: str, is_stationary: bool, station_id: str) -> None:
        self.coordinates = Coordinates(lon, lat)
        self.provider = provider
        self.accuracy = accuracy
        self.additional_info = additional_info
        self.bike_id = bike_id
        self.is_stationary = is_stationary
        self.station_id = station_id
        super().__init__()


class ProviderInterface:
    def get_bikes(self, lat: float, lon: float, limit: int) -> [Bike]:
        return []


