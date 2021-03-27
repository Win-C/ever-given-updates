import os

from flask import Flask
from marinetrafficapi import MarineTrafficApi
from twilio.twiml.messaging_response import MessagingResponse
from decouple import config

api_key = config('MARINE_TRAFFIC_API_KEY')
api = MarineTrafficApi(api_key=api_key)

app = Flask(__name__)


@app.route("/sms", methods=["GET", "POST"])
def boat():
    """ Handle incoming text messages, responding with vessel status update"""
    resp = MessagingResponse()

    vessel = api.single_vessel_positions(time_span=240, mmsi=353136000)
    vessel = vessel.models[0]

    latitude = vessel.latitude.value
    longitude = vessel.longitude.value
    speed = vessel.speed.value

    stuck_latitude = 30.01765
    stuck_longitude = 32.5802
    stuck_speed = 0

    if speed != stuck_speed and latitude != stuck_latitude and longitude != stuck_longitude:
        resp.message("It's moving!")
    else:
        resp.message("Still suck 😔")

    return str(resp)
