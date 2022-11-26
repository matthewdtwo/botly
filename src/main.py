from motor import Motor
from direction import Direction as Dir

import serial
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# PIN delcarations
IN1 = 22
IN2 = 27
M1_SPEED = 10
IN3 = 23
IN4 = 24
M2_SPEED = 9

left_encoder = 0;
right_encoder = 0;

left_motor = Motor(IN1, IN2, M1_SPEED)
right_motor = Motor(IN3, IN4, M2_SPEED)

def parse_serial_data(data):
    data_string = data[2:][:-5] # strip of b and \r\n
    return data_string.split()
    


with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.prot = "/dev/ttyACM0"
    ser.open()

    while ser.is_open:
        data = str(ser.readline())
        data_split = parse_serial_data(data)
        
        if data_split[0] == "left:":
            left = int(data_split[1])
        elif data_split[0] == "right:":
            right = int(data_split[1])
        
        print(f"left: {left}, right: {right}")

    
            
