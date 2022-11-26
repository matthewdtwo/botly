from motor import Motor
from direction import Direction as Dir

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
    if left_encoder_offset == 0:
        left_encoder_offset = offset

def set_right_offset(offset):
    if right_encoder_offset == 0:
        right_encoder_offset = offset

        
def parse_left_or_right_encoder(data_split):
    if data_split[0] == "left:":
        set_left_offset(data_split[1])
        left_encoder = data_split[1] - left_encoder_offset
    elif data_split[0] == "right:":
        set_right_offset(data_split[1])
        right_encoder = data_split[1] - right_encoder_offset
        


with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.port = "/dev/ttyACM0"
    ser.open()

    while ser.is_open:
        data = str(ser.readline())
        data_split = parse_serial_data(data)

        parse_left_or_right_encoder(data_split)
        
        print(f"left: {left_encoder}, right: {right_encoder}")


        
    
            
