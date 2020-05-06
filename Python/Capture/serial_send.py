
import serial, time

arduino = serial.Serial('COM3', 115200, timeout=.1)
time.sleep(1) #give the connection a second to settle

while True:
	nextInput = False
	data = int(input("Enter an angle: "))

	while data > 360:
		data = data - 360

	angle = str(data)
	angle = angle + "\n"

	print(angle)

	arduino.write(angle.encode())

	print('Reading')

	while nextInput == False:
		accept = arduino.readline()
		print(repr(accept.rstrip('\n'.encode())))
		accept = (accept.rstrip('\n'.encode()))
		if accept == '1\r'.encode():
			nextInput = True

