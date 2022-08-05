from motor import Motor
from direction import Direction

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

IN1 = 27
IN2 = 22
IN3 = 23
IN4 = 24


leftMotor = Motor(IN1, IN2)
rightMotor = Motor(IN3, IN4)

def forward():
    leftMotor.setDirection(Direction.FORWARD)
    rightMotor.setDirection(Direction.BACKWARD)
def stop():
    leftMotor.setDirection(Direction.STOPPED)
    rightMotor.setDirection(Direction.STOPPED)

forward()
stop()
