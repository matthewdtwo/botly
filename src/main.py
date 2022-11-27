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


def parse_serial_data(data):
    data_string = data[2:][:-5] # strip of b and \r\n
    return data_string.split()

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
        

def set_motor_speeds(motors, speed):
    for motor in motors:
        motor.setSpeed(speed)

with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.port = "/dev/ttyACM0"
    try:
        ser.open()
    except:
        print("failed to open serial port")

    print("Serial port is open")

    while ser.is_open:
        data = str(ser.readline())
        data_split = parse_serial_data(data)

        parse_left_or_right_encoder(data_split)

        print(f"left: {left_encoder}, right: {right_encoder}")

        if left_encoder <= 475 and right_encoder <= 475:
            set_motor_speeds([left_motor, right_motor], 100)
            print("forward")    
        else:
            set_motor_speeds([left_motor, right_motor], 0)
            print("stopped")

        
        
    if not ser.is_open:
        print("")
        exit(1)


        
    
            
