from interface.utils.coordinate_helper import haversine
from interface.provider_interface import ProviderInterface, Bike
import requests


class Nextbike(ProviderInterface):

    def __init__(self):
        r = requests.get("https://api.nextbike.net/maps/nextbike-live.json")
        self.data = r.json()

    def get_city_uid(self, lat : float, lon : float):
        best_dist = -1
        best_uid = -1
        for country in self.data["countries"]:
            for city in country["cities"]:
                dist = abs(haversine(lat, lon, float(city["lat"]), float(city["lng"])))
                if dist < best_dist or best_dist<0:
                    best_dist = dist
                    best_uid = int(city["uid"])

        return best_uid

    def get_bikes(self, lat: float, lon: float, limit: int) -> [Bike]:
        uid = self.get_city_uid(lat, lon)
        r = requests.get(f"https://api.nextbike.net/maps/nextbike-live.json?city={uid}")
        city_data = r.json()
        places = city_data["countries"][0]["cities"][0]["places"]
        bikes = []
        for place in places:
            place_lon = place["lng"]
            place_lat = place["lat"]
            provider = "nextbike"
            if place["bike"]:
                bike_id = place["bike_list"][0]["number"]
                b = Bike(place_lon, place_lat, provider, 0.0, additional_info="", bike_id=bike_id,
                         is_stationary=False, station_id=None)
                bikes.append(b)
            else:
                bikes_on_station = place["bike_list"]
                for bike in bikes_on_station:
                    bike_id = bike["number"]
                    b = Bike(place_lon, place_lat, provider, 0.0, additional_info="", bike_id=bike_id,
                             is_stationary=True, station_id=str(place["number"]))
                    bikes.append(b)
        bikes = self.limit(bikes, lat, lon, limit)
        return bikes
