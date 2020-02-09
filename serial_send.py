


import serial, time
arduino = serial.Serial('/dev/ttyUSB1', 115200, timeout=.1)
time.sleep(1) #give the connection a second to settle

while True:
        nextInput = False

	data = input("Enter an angle: ")

	while data > 360:
        	data = data - 360

	angle = str(data)
	angle = angle + "\n"

	print(angle)

	arduino.write(angle)

	print('Reading')

	while nextInput == False:
	        accept = arduino.readline()
                print(repr(accept.rstrip('\n')))
                accept = (accept.rstrip('\n'))
		if accept == '1\r':
			print accept.rstrip('\n')
                        nextInput = True

