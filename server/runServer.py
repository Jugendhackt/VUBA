import hashlib
from flask import Flask, request, send_from_directory, send_file
import json
from PIL import Image

from interface.provider.call_a_bike import CallABike
from interface.provider.nextbike import Nextbike
from server.image_util import serve_pil_image, replace_color, get_rgb_from_int
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


@app.route('/res/icon/<string:provider>', methods=['GET'])
def res(provider):
    hash = hashlib.md5((provider+"a").encode("utf-8")).hexdigest()[:6]
    color = int(f"0x{hash}", 16)
    img_template = Image.open("res/marker_template.png")
    img = replace_color(img_template, (35, 32, 31), get_rgb_from_int(color))
    return serve_pil_image(img)


app.run(port=8080)
