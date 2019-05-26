from interface.utils.coordinate_helper import haversine
from interface.provider_interface import ProviderInterface, Bike
import requests


class Jumpbike(ProviderInterface):

    def __init__(self, city, lon: float, lat: float) -> None:
        super().__init__()
        self.city = city
        self.lon = lon
        self.lat = lat

    def get_bikes(self, lat: float, lon: float, limit: int) -> [Bike]:
        if haversine(self.lon, self.lat, lon, lat) > 50:
            return []
        r = requests.get("https://" + self.city + ".com/opendata/free_bike_status.json")
        data = r.json()
        bikes = []
        for bike in data["data"]["bikes"]:
            bike_id = bike["bike_id"]
            info = bike["jump_ebike_battery_level"] + ' Battery'
            lon = bike["lon"]
            lat = bike["lat"]
            provider = "jump"
            stationary = False
            station_id = None
            bikes.append(Bike(lon, lat, provider, 0, info, bike_id, stationary, station_id))
        bikes = self.limit(bikes, lat, lon, limit)

        return bikes




