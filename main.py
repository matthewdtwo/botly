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
IN3 = 23
IN4 = 24

leftMotor = Motor(IN1, IN2)
rightMotor = Motor(IN3, IN4)

@app.route("/forward")
def forward():
    leftMotor.setDirection(Dir.FORWARD)
    rightMotor.setDirection(Dir.FORWARD)

@app.route("/stopped")
def stop():
    leftMotor.setDirection(Dir.STOPPED)
    rightMotor.setDirection(Dir.STOPPED)

@app.route("/left")
def left():
    leftMotor.setDirection(Dir.FORWARD)
    rightMotor.setDirection(Dir.BACKWARD)

@app.route("/right")
def right():
    leftMotor.setDirection(Dir.BACKWARD)
    rightMotor.setDirection(Dir.FORWARD)

@app.route("/backward")
def backward():
    leftMotor.setDirection(Dir.BACKWARD)
    rightMotor.setDirection(Dir.BACKWARD)