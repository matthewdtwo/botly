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

gpio.setup(IN1, gpio.OUT)
gpio.setup(IN2, gpio.OUT)
gpio.setup(IN3, gpio.OUT)
gpio.setup(IN4, gpio.OUT)

gpio.output(IN1, gpio.LOW)
gpio.output(IN2, gpio.HIGH)
gpio.output(IN3, gpio.LOW)
gpio.output(IN4, gpio.HIGH)


time.sleep(2)

gpio.output(IN1, gpio.LOW)
gpio.output(IN2, gpio.LOW)
gpio.output(IN3, gpio.LOW)
gpio.output(IN4, gpio.LOW)