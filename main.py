from motor import Motor
from direction import Direction as Dir

import RPi.GPIO as gpio
import time
from flask import Flask, request
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



@app.route("/axis0", methods=["POST"])
def axis0():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json
        print(f"json: {json}")
    return "axis0"

@app.route("/axis1", methods=["POST"])
def axis1():
    content_type = request.headers.get('Content-Type')
    if(content_type == 'application/json'):
        json = request.json
        print(f"json: {json}")
    return "axis1"
@app.route("/forward")
def forward():
    leftMotor.setDirection(Dir.FORWARD)
    rightMotor.setDirection(Dir.FORWARD)
    leftMotor.setSpeed(100)
    rightMotor.setSpeed(100)
    return "forward"

@app.route("/stopped")
def stop():
    leftMotor.setDirection(Dir.STOPPED)
    rightMotor.setDirection(Dir.STOPPED)
    leftMotor.setSpeed(0)
    rightMotor.setSpeed(0)
    return "stopped"

@app.route("/left")
def left():
    leftMotor.setDirection(Dir.FORWARD)
    rightMotor.setDirection(Dir.BACKWARD)
    return "left"

@app.route("/right")
def right():
    leftMotor.setDirection(Dir.BACKWARD)
    rightMotor.setDirection(Dir.FORWARD)
    return "right"

@app.route("/backward")
def backward():
    leftMotor.setDirection(Dir.BACKWARD)
    rightMotor.setDirection(Dir.BACKWARD)
    return "backward"