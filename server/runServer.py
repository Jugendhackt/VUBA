from flask import Flask, request, send_from_directory
import json

from interface.provider.call_a_bike import CallABike
from interface.provider.nextbike import Nextbike
from interface.provider.jumpbike_USA import JumpbikeUSA
from interface.provider.mobike import Mobike

app = Flask(__name__)
provider = [CallABike(), Nextbike(), JumpbikeUSA(), Mobike()]


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


# Static file serving

@app.route('/', methods=['GET'])
def index():
    return send_from_directory('../client', 'index.html')


@app.route('/lib/<string:file>', methods=['GET'])
def lib(file):
    return send_from_directory('../client/src', file)


app.run(port=8080)
