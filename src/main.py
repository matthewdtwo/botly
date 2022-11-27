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

def set_right_offset(offset):
    print("right offset")

def set_left_offset(offset):
    print("left offset")

def parse_line_to_encoders(line):
    split_line = line.split()
    direction = split_line[0]
    value = int(split_line[1])

    if direction == "right:":
        if right_encoder_offset == 0:
            set_right_offset(value)
    if direction == "left:":
        if left_encoder_offset == 0:
            set_left_offset(value)
        
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

while ser.is_open:    
    try:
        line = ser.readline().decode('utf-8')
        
        if(line == ''):
            continue
        else:
            try:
                parse_line_to_encoders(line)
    
            except:
                print("failed to parse line.")

        print(f"left: {left_encoder}, right: {right_encoder}")
        
    except:
        print("failed to read line")
        exit(1)
        