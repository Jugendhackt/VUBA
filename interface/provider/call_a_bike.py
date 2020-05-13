from interface.provider_interface import ProviderInterface, Bike
from random import randint
import json
import requests


class CallABike(ProviderInterface):
    def get_bikes(self, lat: float, lon: float, limit: int) -> [Bike]:
        request_data = {
            "method": "Map.listBikes",
            "id": randint(9999, 9999999),
            "params": [
                {
                    "lat": lat,
                    "long": lon,
                    "maxItems": limit,
                    "radius": 10000,
                    "name": ""
                }
            ]
        }
        response = requests.post('https://www.callabike.de/de/rpc', data=json.dumps(request_data))
        bikes = []
        data = response.json()
        for location in data['result']['data']['Locations']:
            lon = float(location['Position']['Longitude'])
            lat = float(location['Position']['Latitude'])
            info = location['Description']
            stationary = False
            station_id = None
            if location['isStation']:
                stationary = True
                station_id = location['objectId']
            for bike in location['availableVehicles']:
                provider = bike['MarkeName'].replace(' ', '_').lower()
                bikes.append(Bike(lon, lat, provider, 0, info, bike['Number'], stationary, station_id))
        return bikes



