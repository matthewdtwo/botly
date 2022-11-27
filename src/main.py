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
    global right_encoder_offset
    if right_encoder_offset == 0:
        right_encoder_offset = offset
        
def set_left_offset(offset):
    global left_encoder_offset
    if left_encoder_offset == 0:
        left_encoder_offset = offset

def set_left_encoder(value):
    global left_encoder
    print(f"left: {value}")
    left_encoder = left_encoder_offset - value    
def set_right_encoder(value):
    global right_encoder
    print(f"right: {value}")
    right_encoder = right_encoder_offset - value    

def parse_line_to_encoders(line):
    split_line = line.split()
    direction = split_line[0]
    value = int(split_line[1])

    if direction == "right:":
        if right_encoder_offset == 0:
            set_right_offset(value)
        set_right_encoder(value)
    if direction == "left:":
        if left_encoder_offset == 0:
            set_left_offset(value)
        set_left_encoder(value)
        
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

while ser.is_open:    
    try:
        line = ser.readline().decode('utf-8')
        
        if(line == ''):
            continue
        else:
            try:
                parse_line_to_encoders(line)
    
            except Exception as e:
                print(f"failed to parse line: {e}")

        print(f"left: {left_encoder}, right: {right_encoder}")

    except:
        print("failed to read line")
        exit(1)
        