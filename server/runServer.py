import hashlib
from flask import Flask, request, send_from_directory, Response
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
    response = Response()
    response.headers['Content-Type'] = 'application/json'
    try:
        lat = float(request.args['lat'])
        lon = float(request.args['lon'])
        limit = int(request.args['limit'])
    except ValueError:
        response.response = json.dumps({"message": "Please provide real numbers!"})
        response.status_code = 449
        return response

    if not (lat is None or lon is None or limit is None or limit < 1 or lat < -90 or lat > 90 or lon < -180 or lon > 180):
        bike_list = "["
        for service in provider:
            bikes = []
            try:
                bikes = service.get_bikes(lat, lon, limit)
            except Exception:
                pass
            finally:
                for bike in bikes:
                    bike_list += bike.__repr__() + ","
        bike_list = bike_list[:-1]
        bike_list += "]"
        response.response = bike_list
        return response
    else:
        response.response = json.dumps({"message": "Not everything or something wrong provided!"})
        response.status_code = 449
        return response


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
