import json

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

    def __repr__(self) -> str:
        return json.dumps({
            "coordinates": {
                "lon": self.coordinates.lon,
                "lat": self.coordinates.lat
            },
            "provider": self.provider,
            "accuracy": self.accuracy,
            "additionalInfo": self.additional_info,
            "bikeId": self.bike_id,
            "isStationary":  self.is_stationary,
            "stationId": self.station_id
        })

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


