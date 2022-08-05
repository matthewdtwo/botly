from direction import Direction
import RPi.GPIO as gpio

class Motor:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        print(f"in1: {in1} in2: {in2}")
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        
    def setDirection(self, direction):
        print(f"direction: {direction} in1: {self.in1}, in2: {self.in2}")
        if direction == Direction.FORWARD:
            print("forward")
            gpio.output(self.in1, gpio.LOW)
            gpio.output(self.in2, gpio.HIGH)
        if direction == Direction.STOPPED:
            print("stopped")
            gpio.output(self.in1, gpio.LOW)
            gpio.output(self.in2, gpio.LOW)
    