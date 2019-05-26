map = new OpenLayers.Map("mapdiv");
map.addLayer(new OpenLayers.Layer.OSM());

document.getElementById('setLocation').onclick = function () {
    location.hash = document.getElementById('locationInput').value;
    location.reload();
};

document.getElementById('locationInput').addEventListener("keyup", function(event){
    if(event.key === "Enter"){document.getElementById("setLocation").click()}
});

let setMarker = function (lat, lon, isGPS) {
    console.log(lat);
    console.log(lon);
    let lonLat = new OpenLayers.LonLat(lon, lat)
        .transform(
            new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
            map.getProjectionObject() // to Spherical Mercator Projection
        );
    if(isGPS){
        let gpsIcon = new OpenLayers.Icon('/res/gpsIcon.png', new OpenLayers.Size(10, 10    ), new OpenLayers.Pixel(-6, -10));
        markers.addMarker(new OpenLayers.Marker(lonLat, gpsIcon.clone()));
    }else{
        markers.addMarker(new OpenLayers.Marker(lonLat));
    }

    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
            if (xmlhttp.status === 200) {
                bikes = JSON.parse(xmlhttp.responseText);
                for (let i = 0; i < bikes.length; i++) {
                    let lat = bikes[i]["coordinates"]["lat"];
                    let lon = bikes[i]["coordinates"]["lon"];
                    let bikelonLat = new OpenLayers.LonLat(lon, lat)
                        .transform(
                            new OpenLayers.Projection("EPSG:4326"),
                            map.getProjectionObject()
                        );
                    let icon = new OpenLayers.Icon('/res/icon/' + bikes[i].provider, new OpenLayers.Size(20, 20), new OpenLayers.Pixel(-6, -10));
                    let marker = new OpenLayers.Marker(bikelonLat, icon.clone());

                    marker.events.register('click', marker, function () {
                        popup = new OpenLayers.Popup.FramedCloud(bikes[i].bikeID,
                            marker.lonlat,
                            new OpenLayers.Size(200, 200),
                            bikes[i].additionalInfo + "<br>" +
                            (bikes[i].isStationary + "").replace('true', 'Das Fahrrad ist in einer Station.').replace('false', 'Das Fahrrad befindet sich nicht in einer Station.') + "<br>" +
                            "Angeboten von " + bikes[i].provider,
                            null, true);
                        map.addPopup(popup);
                    });
                    markers.addMarker(marker);
                }
            } else if (xmlhttp.status === 400) {
                console.log('There was an error 400');
            } else {
                console.log('something else other than 200 was returned');
                console.log(xmlhttp.status);
                console.log(xmlhttp.responseText);
            }
        }
    };

    let req_url = "getBikes?lon=" + lon + "&lat="
        + lat + "&limit=100";
    xmlhttp.open("GET", req_url, true);
    xmlhttp.send();

    map.setCenter(lonLat, zoom);
};
var zoom = 16;
var markers = new OpenLayers.Layer.Markers("Markers");

let params = location.hash.substr(1);
if (params.includes(',')) {
    let coords = params.split(",");
    if (coords.length === 2) {
        let lat = parseFloat(coords[0]);
        let lon = parseFloat(coords[1]);
        if (!isNaN(lat) && !isNaN(lon)) {
            setMarker(lat, lon, false);
        } else {
            navigator.geolocation.getCurrentPosition(function(position){
                setMarker(position.coords.latitude, position.coords.longitude, true)
            });
        }
    } else {
        navigator.geolocation.getCurrentPosition(function(position){
            setMarker(position.coords.latitude, position.coords.longitude, true)
        });
    }
} else if (params !== "") {
    http = new XMLHttpRequest();
    http.onreadystatechange = function () {
        if (http.readyState === XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
            if (http.status === 200) {
                var data = JSON.parse(http.responseText)[0];
                setMarker(parseFloat(data['lat']), parseFloat(data['lon']), false);
            }
        }
    };
    http.open('GET', 'https://nominatim.openstreetmap.org/search/' + params + '?format=json&limit=1');
    http.send();

} else {
    navigator.geolocation.getCurrentPosition(function(position){
        setMarker(position.coords.latitude, position.coords.longitude, true)
    });
}

map.addLayer(markers);