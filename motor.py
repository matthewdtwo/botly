from direction import Direction
import RPi.GPIO as gpio

class Motor:
    def __init__(self, in1, in2):
        print(f"in1: {in1}, in2: {in2}")