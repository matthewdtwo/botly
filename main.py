from motor import Motor
from direction import Direction as Dir

import RPi.GPIO as gpio
import time
from flask import Flask
import flask_cors


app = Flask(__name__)

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

@app.route("/forward")
def forward():
    leftMotor.setDirection(Dir.FORWARD)
    rightMotor.setDirection(Dir.FORWARD)
    return "forward"

@app.route("/stopped")
def stop():
    leftMotor.setDirection(Dir.STOPPED)
    rightMotor.setDirection(Dir.STOPPED)
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