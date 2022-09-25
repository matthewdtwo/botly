from direction import Direction
import RPi.GPIO as gpio

class Motor:
    def __init__(self, in1, in2, speed_pin):
        self.in1 = in1
        self.in2 = in2
        self.speed_pin = speed_pin
        print(f"in1: {in1} in2: {in2}, speed_pin: {speed_pin}")
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        gpio.setup(self.speed_pin, gpio.OUT)

        self.setDirection(Direction.STOPPED)

        gpio.output(self.speed_pin, gpio.HIGH)

        self.speed_pwm = gpio.PWM(self.speed_pin, 1000)

        self.speed_pwm.ChangeDutyCycle(100)
        
    def setDirection(self, direction):
        # print(f"direction: {direction} in1: {self.in1}, in2: {self.in2}")
        if direction == Direction.FORWARD:
            print("forward")
            gpio.output(self.in1, gpio.LOW)
            gpio.output(self.in2, gpio.HIGH)
        if direction == Direction.STOPPED:
            print("stopped")
            gpio.output(self.in1, gpio.LOW)
            gpio.output(self.in2, gpio.LOW)
        if direction == Direction.BACKWARD:
            print("forward")
            gpio.output(self.in1, gpio.HIGH)
            gpio.output(self.in2, gpio.LOW)

    def setSpeed(self, speed):
        self.speed_pwm.ChangeDutyCycle(speed)