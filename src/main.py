from motor import Motor
from direction import Direction as Dir

import signal
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

start_time = int(time.time())

console_print_delay = 1

def reset_arduino():
    gpio.setup(ARDUINO_RESET, gpio.OUT)
    gpio.output(ARDUINO_RESET, gpio.LOW)
    time.sleep(1)
    gpio.output(ARDUINO_RESET, gpio.HIGH)

def cleanup(signum, frame):
    print("cleaning up")
    print("stopping motors")
    for motor in motors:
        motor.setSpeed(0)
        motor.setDirection(Dir.STOPPED)
    print("resetting arduino")
    reset_arduino()
    exit(1)

def open_serial_port():
    global ser
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

def read_line():
    try: 
        line = ser.readline().decode('utf-8')
        line = str(line).strip()
        return line
    except Exception as read_exception:
        print(f"read exception: {read_exception}")

def set_left_encoder_offset(value):
    global left_encoder_offset
    if left_encoder_offset == 0:
        left_encoder_offset = value
            
def set_right_encoder_offset(value):
    global right_encoder_offset
    if right_encoder_offset == 0:
        right_encoder_offset = value

def parse_encoder_values(line):
    global left_encoder
    global right_encoder

    try:
        [direction, value] = line.split()
        value = int(value)
        if direction == "left:":
            set_left_encoder_offset(value)
            left_encoder = value - left_encoder_offset
        if direction == "right:":
            set_right_encoder_offset(value)
            right_encoder = value - right_encoder_offset
    except Exception as e:
        print(f"failed to parse: {e}")
            
def print_encoder_values():
    global start_time
    current_time = int(time.time())
    elapsed_time = int(current_time - start_time)
    if(elapsed_time >= console_print_delay):
        print(f"left: {left_encoder}, right: {right_encoder}")      
        start_time = int(time.time())


def check_encoder_values():
    global left_encoder
    global right_encoder

    if(left_encoder >= 475):
        left_motor.setDirection(Dir.STOPPED)
        left_motor.setSpeed(0)
    if(right_encoder >= 475):
        right_motor.setDirection(Dir.STOPPED)
        right_motor.setSpeed(0)
        
        
signal.signal(signal.SIGINT, cleanup)        
reset_arduino()
time.sleep(10)
open_serial_port()

try:
    while ser.is_open:
        line = read_line()
        parse_encoder_values(line)
        print_encoder_values()

        check_encoder_values()

except Exception as e:
    print(f"recieved {e}")
    exit(1)