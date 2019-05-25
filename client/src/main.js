map = new OpenLayers.Map("mapdiv");
map.addLayer(new OpenLayers.Layer.OSM());

let setMarker = function(position){
    let lonLat = new OpenLayers.LonLat(position.coords.longitude, position.coords.latitude)
        .transform(
            new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
            map.getProjectionObject() // to Spherical Mercator Projection
        );
    markers.addMarker(new OpenLayers.Marker(lonLat));

    let xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState === XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
           if (xmlhttp.status === 200) {
               bikes = JSON.parse(xmlhttp.responseText);
               for(let i = 0; i < bikes.length; i++){
                   let lat = bikes[i]["coordinates"]["lat"];
                   let lon = bikes[i]["coordinates"]["lon"];
                   let bikelonLat = new OpenLayers.LonLat(lon, lat)
                       .transform(
                           new OpenLayers.Projection("EPSG:4326"),
                           map.getProjectionObject()
                       );
                   let icon = new OpenLayers.Icon('/res/icon/' +bikes[i].provider, new OpenLayers.Size(20, 20), new OpenLayers.Pixel(-6, -10));
                   let marker = new OpenLayers.Marker(bikelonLat, icon.clone());

                   marker.events.register('click', marker, function() {
                        popup = new OpenLayers.Popup.FramedCloud(bikes[i].bikeID,
                            marker.lonlat,
                            new OpenLayers.Size(200, 200),
                            "Fahrrad von<br/>"+bikes[i].provider,
                            null, true);
                        map.addPopup(popup);
                    });
                   markers.addMarker(marker);
               }
           }
           else if (xmlhttp.status === 400) {
              console.log('There was an error 400');
           }
           else {
               console.log('something else other than 200 was returned');
               console.log(xmlhttp.status);
               console.log(xmlhttp.responseText);
           }
        }
    };

    let req_url = "getBikes?lon=" + position.coords.longitude + "&lat="
        + position.coords.latitude + "&limit=100";
    xmlhttp.open("GET", req_url, true);
    xmlhttp.send();

    map.setCenter (lonLat, zoom);
};

navigator.geolocation.getCurrentPosition(setMarker);

var zoom=16;
var markers = new OpenLayers.Layer.Markers( "Markers" );
map.addLayer(markers);