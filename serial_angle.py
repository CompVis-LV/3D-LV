

def serialAngle(data):
    import serial, time

    arduino = serial.Serial('COM3', 115200, timeout=.1)
    time.sleep(1) #give the connection a second to settle

    data = int(data)

    time.sleep(1) #give the connection a second to settle

    while data > 360:
        data = data - 360

    angle = str(data)
    angle = angle + "\n"

    print(angle)

    arduino.write(angle.encode())

    print('Reading')

    timeout = time.time() + 10   # 10 seconds from now

    nextInput = False

    while nextInput == False:
        accept = arduino.readline()
        print(repr(accept.rstrip('\n'.encode())))
        accept = (accept.rstrip('\n'.encode()))
        if accept == '1\r'.encode():
            return True
        if  time.time() > timeout:
            return False


