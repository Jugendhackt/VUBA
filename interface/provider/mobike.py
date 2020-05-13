from interface.provider_interface import ProviderInterface, Bike
from random import randint
import json
import requests


class Mobike(ProviderInterface):

    def get_bikes(self, lat: float, lon: float, limit: int) -> [Bike]:
        data = {
            "latitude": lat,
            "Longitude": lon
        }
        header= {
            "platform": "1",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Android 7.1.2; Pixel Build/NHG47Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.9 NTENTBrowser/3.7.0.496 (IWireless-US) Mobile Safari/537.36 (or whatever)"
        }
        response = requests.post("http://global-n-mobike-g.mobike.com/api/nearby/v4/nearbyBikeInfo",
                                 headers=header,
                                 data=data)
        bikes = []
        for bike in response.json()["bike"]:
            bike_id = bike["bikeIds"]
            lon = bike["distX"]
            lat = bike["distY"]
            provider = "mobike"
            stationary = False
            station_id = None

            bikes.append(Bike(lon, lat, provider, 0, "", bike_id, stationary, station_id))
        bikes = self.limit(bikes, lat, lon, limit)
        return bikes
