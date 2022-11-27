import serial

right = 0;
left = 0;

try:
    ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
except Exception as e:
    print(f"Failed to open serial port: {e}")
    exit(1)

try:
    while ser.is_open:
        line = ser.readline().decode('utf-8').strip()
        if(line == ""):
            print("nothing recieved")
        else:
            print(f"line is: {line}")
    
except Exception as e:
    print(f"failure occurred: {e}")
    exit(1)