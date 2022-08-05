from motor import Motor
from direction import Direction

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)


IN1 = 27
IN2 = 22
IN3 = 23
IN4 = 24


leftMotor = Motor(IN1, IN2)
leftMotor.setDirection(Direction.FORWARD)
time.sleep(.25)
leftMotor.setDirection(Direction.BACKWARD)
