from motor import Motor
from direction import Direction as Dir

import RPi.GPIO as gpio
import time
from flask import Flask, request, send_from_directory
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

IN1 = 22
IN2 = 27
M1_SPEED = 10
IN3 = 23
IN4 = 24
M2_SPEED = 9

leftMotor = Motor(IN1, IN2, M1_SPEED)
rightMotor = Motor(IN3, IN4, M2_SPEED)

@app.route("/")
def send_index():
    return send_from_directory("static", "index.html")

@app.route("/gamepad", methods=["POST"])
def axis0():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json
        print(f"json: {json}")
    return "axis0"
