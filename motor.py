from direction import Direction
import RPi.GPIO as gpio

class Motor:
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        gpio.output(self.in1, gpio.LOW)
        gpio.output(self.in2, gpio.LOW)


    def setDirection(self, direction):
        if(direction == Direction.FORWARD):
            print("Forward")
        if(direction == Direction.BACKWARD):
            print("Backward")
        if(direction == Direction.STOPPED):
            print("Stopped")