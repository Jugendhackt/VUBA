from interface.utils.coordinate_helper import haversine
from interface.provider_interface import ProviderInterface, Bike
import requests


class JumpbikeUSA(ProviderInterface):

    def get_bikes(self, lat: float, lon: float, limit: int) -> [Bike]:
        r = requests.get(f"https://dc.jumpmobility.com/opendata/free_bike_status.json")
        data = r.json()
        bikes = []
        for bike in data["data"]["bikes"]:
            bike_id = bike["bike_id"]
            info = bike["jump_ebike_battery_level"]
            lon = bike["lon"]
            lat = bike["lat"]
            provider = "Jump"
            stationary = False
            station_id = "non"

            bikes.append(Bike(lon, lat, provider, 0, info, bike_id, stationary, station_id))
        bikes = self.limit(bikes, lat, lon, limit)
        return bikes




