[![Build Status](https://dev.azure.com/TheMinefighter/VUBA/_apis/build/status/VUBA-CI?branchName=master)](https://dev.azure.com/TheMinefighter/VUBA/_build/latest?definitionId=5&branchName=master)
# VUBA
##### Vereinigte Übersicht aller Bikesharing Anbieter
#### Find the nearest bike.
## What is VUBA?
VUBA is a webapp to find the nearest bike from many bike sharing apps.
## Why?
Sometimes you need to find the nearest bike.
Without VUBA you had to look through every bike sharing app to find the nearest.
With VUBA you just open VUBA, find the nearest bike and afterwards open the corresponding bike app.
## How?
First of all there are the Providers.
Most of them provide an API.
These APIs will be contacted by our server when needed.
The server will (in the future) provide caching for these information.
Then there is an OAS3 specified interface for the clients.
## Install and run!
After you have configured you have to have a look at some important things:
 - The working directory should be /server directory.
 - PYTHONPATH should be /.
 - For HTTPS support (which is recommend due to browser security reasons with location access) you need to either host OpenLayers yourself (recommend) or
 use the following mirror in the index.html https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js.
## Supported bike providers
 - nextbike
 - Call-a-bike
 - Mobike
 - Jump (USA only)
 
 
##### Licenses
[The Marker Icon](https://www.iconfinder.com/icons/383108/map_marker_icon) is licensed under "Free for commercial use".

[Loading Animation](https://tobiasahlin.com/spinkit/) is licensed under the [MIT License](https://github.com/tobiasahlin/SpinKit/blob/master/LICENSE)
