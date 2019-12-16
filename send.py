import serial

port = "/dev/ttyACM0"

s1 = serial.Serial(port,115200)
s1.flushInput()

with open('result','r') as f:
	result = f.read()
	s1.write(result)
