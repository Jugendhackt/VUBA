import hashlib
from flask import Flask, request, send_from_directory, Response
import json
from PIL import Image

from interface.provider.call_a_bike import CallABike
from interface.provider.nextbike import Nextbike
from server.image_util import serve_pil_image, replace_color, get_rgb_from_int
from interface.provider.jumpbike import Jumpbike
from interface.provider.mobike import Mobike

app = Flask(__name__)
provider = [CallABike(),
            Nextbike(),
            Jumpbike("atl.jumpbikes", -84.349255, 33.79799666666667),
            Jumpbike("atx.jumpbikes", -97.74560666666666, 30.250985),
            Jumpbike("bt.jumpbikes", -76.678591, 39.259353),
            Jumpbike("bts.jumpbikes", -76.678591, 39.259353),
            Jumpbike("bxl.jumpbikes", 4.438058333333333, 50.84443666666667),
            Jumpbike("dc.jumpbikes", -77.06582, 38.894286),
            Jumpbike("den.jumpbikes", -105.00064166666667, 39.77574),
            Jumpbike("la.jumpbikes", -118.48565666666667, 34.045186666666666),
            Jumpbike("lou.jumpbikes", -83.12633333333333, 42.549166666666665),
            Jumpbike("mia.jumpbikes", -80.186885, 25.783151),
            Jumpbike("nyc.jumpbikes", -74.08365333333333, 40.64044),
            Jumpbike("pvd.jumpbikes", -71.39172, 41.82959666666667),
            Jumpbike("sc.jumpbikes", -122.022995, 36.98526),
            Jumpbike("sf.jumpbikes", -122.390595, 37.74791166666667),
            Jumpbike("sac.jumpbikes", -121.48072166666667, 38.55402),
            Jumpbike("san.jumpbikes", -117.133975, 32.7024),
            Jumpbike("sea.jumpbikes", -122.348495, 47.61465666666667),
            Mobike()]


@app.route('/getBikes', methods=['GET'])
def getBikes():
    response = Response()
    response.headers['Content-Type'] = 'application/json'
    try:
        lat = float(request.args['lat'])
        lon = float(request.args['lon'])
        limit = int(request.args['limit'])
    except ValueError:
        response.data = json.dumps({"message": "Please provide real numbers!"})
        response.status_code = 449
        return response

    if not (lat is None or lon is None or limit is None or limit < 1 or lat < -90 or lat > 90 or lon < -180 or lon > 180):
        bike_list = "["
        for service in provider:
            bikes = []
            try:
                bikes = service.get_bikes(lat, lon, limit)
            except Exception as e:
                print(e)
            finally:
                for bike in bikes:
                    bike_list += bike.__repr__() + ","
        if bike_list != "[":
            bike_list = bike_list[:-1]
        bike_list += "]"
        response.data = bike_list
        return response
    else:
        response.data = json.dumps({"message": "Not everything or something wrong provided!"})
        response.status_code = 449
        return response


# Static file serving
@app.route('/', methods=['GET'])
def index():
    return send_from_directory('../client', 'index.html')


@app.route('/lib/<string:file>', methods=['GET'])
def lib(file):
    return send_from_directory('../client/src', file)


@app.route('/res/<string:file>', methods=["GET"])
def res(file):
    return send_from_directory('res', file)


@app.route('/res/icon/<string:provider>', methods=['GET'])
def createicon(provider):
    hash = hashlib.md5((provider+"a").encode("utf-8")).hexdigest()[:6]
    color = int("0x"+str(hash), 16)
    img_template = Image.open("../server/res/marker_template.png")
    img = replace_color(img_template, (35, 32, 31), get_rgb_from_int(color))
    return serve_pil_image(img)


if __name__ == '__main__':
    app.run(port=8080)
