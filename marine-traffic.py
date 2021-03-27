""" Test Marine Traffic API with key """

import os
from marinetrafficapi import MarineTrafficApi
from decouple import config

api_key = config('MARINE_TRAFFIC_API_KEY')
api = MarineTrafficApi(api_key=api_key)

vessel = api.single_vessel_positions(time_span=240, mmsi=353136000)

vessel = vessel.models[0]

latitude = vessel.latitude.value
longitude = vessel.longitude.value
speed = vessel.speed.value

print(latitude, longitude, speed)
