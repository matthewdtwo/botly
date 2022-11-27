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

ARDUINO_RESET = 21

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
    left_encoder = left_encoder_offset - value    

def set_right_encoder(value):
    global right_encoder
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

def try_parse_line(line):
    if line != "":
        try:
            parse_line_to_encoders(line)
            print(f"left: {left_encoder}, left_encoder_offset {left_encoder_offset}, right: {right_encoder}, right_encoder_offset {right_encoder_offset}")
            print(f"line: {line}")
        except Exception as e:
            print(f"failed: {e}")

def read_line():
    line = ser.readline().decode('utf-8')
    line = str(line).strip()
    return line

def reset_arduino():
    gpio.setup(ARDUINO_RESET, gpio.OUT)
    gpio.output(ARDUINO_RESET, gpio.LOW)
    time.sleep(1)
    gpio.output(ARDUINO_RESET, gpio.HIGH)
    time.sleep(5)

# main program variables

reset_arduino()

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

motors = [left_motor, right_motor]

left_encoder_target = -475
right_encoder_target = -475

set_motor_direction(motors, Dir.STOPPED)
# main program loop   
while ser.is_open:
    try_parse_line(read_line())
