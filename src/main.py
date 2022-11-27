from motor import Motor
from direction import Direction as Dir

import time
import serial
import RPi.GPIO as gpio


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# PIN delcarations
IN1 = 22
IN2 = 27
M1_SPEED = 10
IN3 = 23
IN4 = 24
M2_SPEED = 9

left_encoder = 0
right_encoder = 0

left_encoder_offset = 0
right_encoder_offset = 0

left_motor = Motor(IN1, IN2, M1_SPEED)
right_motor = Motor(IN3, IN4, M2_SPEED)
        
def set_motor_direction(motors, direction):
    for motor in motors:
        motor.setDirection(direction)
        
def set_motor_speeds(motors, speed):
    for motor in motors:
        motor.setSpeed(speed)


def parse_line(line):
    split_line = line.split()
    if split_line[0] == "left:":
        print(f"left: {left}")
    elif split_line[0] == "right:":
        print(f"right: {right}")
        
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
line = ''

while ser.is_open:    
    try:
        line = ser.readline().decode('utf-8')
        
        if(line == ''):
            continue
        else:
            try:
                parse_line(line)
            except:
                print("failed to parse line")


    except:
        print("failed to read line")
        exit(1)
        