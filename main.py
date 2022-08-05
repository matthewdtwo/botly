from motor import Motor
from direction import Direction

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

IN1 = 22
IN2 = 27
IN3 = 23
IN4 = 24

leftMotor = Motor(IN1, IN2)
leftMotor.setDirection(Direction.FORWARD)
time.sleep(2)
leftMotor.setDirection(Direction.STOPPED)