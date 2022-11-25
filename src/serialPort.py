import serial

right = 0;
left = 0;

with serial.Serial() as ser:
    ser.baudrate = 115200
    ser.port = '/dev/ttyACM0'
    ser.open()

    while ser.is_open:
        data = str(ser.readline())
        data_string = data[2:][:-5] # strip off the b and \r\n

        data_split = data_string.split()

        if data_split[0] == "left:":
            left = int(data_split[1])
        elif data_split[0] == "right:":
            right = int(data_split[1])

        print(f"left: {left}, right: {right}")


