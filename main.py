from motor import Motor
from direction import Direction as Dir

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

IN1 = 22
IN2 = 27
IN3 = 23
IN4 = 24

leftMotor = Motor(IN1, IN2)
rightMotor = Motor(IN3, IN4)

leftMotor.setDirection(Dir.FORWARD)
rightMotor.setDirection(Dir.FORWARD)
time.sleep(2)
leftMotor.setDirection(Dir.STOPPED)
rightMotor.setDirection(Dir.STOPPED)