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
        
motors = [left_motor, right_motor]

def read_line():
    try: 
        line = ser.readline().decode('utf-8')
        line = str(line).strip()
        return line
    except Exception as read_exception:
        print(f"read exception: {read_exception}")
        

def reset_arduino():
    gpio.setup(ARDUINO_RESET, gpio.OUT)
    gpio.output(ARDUINO_RESET, gpio.LOW)
    time.sleep(1)
    gpio.output(ARDUINO_RESET, gpio.HIGH)
    time.sleep(5)

# main program variables

try :
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
except Exception as e:
    print(f"Failed opening the serial port: {e}")
    reset_arduino()
    try:
        ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
    except:
        print("failed twice. exiting")
        exit(1)
    
    
