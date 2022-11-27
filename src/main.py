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


def set_left_offset(offset):
    global left_encoder_offset
    if left_encoder_offset == 0:
        left_encoder_offset = offset

def set_right_offset(offset):
    global right_encoder_offset
    if right_encoder_offset == 0:
        right_encoder_offset = offset

        
def parse_left_or_right_encoder(data_split):
    global left_encoder_offset
    global right_encoder_offset
    global left_encoder
    global right_encoder

    if data_split[0] == "left:":
        set_left_offset(data_split[1])
        left_encoder = int(data_split[1]) - int(left_encoder_offset)
    elif data_split[0] == "right:":
        set_right_offset(data_split[1])
        right_encoder = int(data_split[1]) - int(right_encoder_offset)
        
def set_motor_direction(motors, direction):
    for motor in motors:
        motor.setDirection(direction)
        
def set_motor_speeds(motors, speed):
    for motor in motors:
        motor.setSpeed(speed)



        
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
line = ''

while ser.is_open:    
    try:
        line = ser.readline().decode('utf-8')
        
        if(line != ""):
            continue
        else:
            print(f"line: {line}")

    except:
        print("failed to read line")
        exit(1)
        