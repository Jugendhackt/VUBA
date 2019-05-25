from flask import Flask, request
import json

from interface.provider.call_a_bike import CallABike
from interface.provider.nextbike import Nextbike

app = Flask(__name__)
provider = [CallABike(), Nextbike()]


@app.route('/getBikes', methods=['GET'])
def getBikes():
    lat = float(request.args['lat'])
    lon = float(request.args['lon'])
    limit = int(request.args['limit'])
    if not (lat is None or lon is None or limit is None):
        bike_list = "["
        for service in provider:
            bikes = service.get_bikes(lat, lon, limit)
            for bike in bikes:
                bike_list += bike.__repr__() + ","
        bike_list = bike_list[:-1]
        bike_list += "]"
        return bike_list
    return json.dumps({"message": "Not everything provided!"})


app.run(port=8080)
