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
Fist of all there are the Providers.
Most of them provide an API.
These APIs will be contacted by our server when needed.
The server will (in the future) Provide caching for these information.
Then there is an OAS3 specified interface for the clients.

## Supported bike providers
 - nextbike
 - Call-a-bike