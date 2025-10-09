# Home assistant setup



## Features

 - Heating schedules for infrequent rooms, such as study and playroom.
 - Monitor energy usage
 - Control study environment (lights, heating).


## Build/deploy

The `Dockerfile` builds a custom HA docker image, that includes
[pyglowmarkt](https://github.com/cybermaggedon/pyglowmarkt), a Python API for accessing the Bright
API for energy usage.

The `docker-compose.yml` exposes the devices necessary for Zigbee.

## Configuration

## Hardware

 - Zigbee coordinator
 - Zigbee TRVs
 - Lightswitch in study
 - Plugs (e.g. study radiator, Christmas tree)
 - Philips Hue Play PC lightstrip
 - Sonos
