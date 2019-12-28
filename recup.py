import json
import time
import serial

info = {}

try:
	with open('/home/pi/aqn-ceri/i2c/result','r') as f:
		txt = f.read().split(',')
		info['co2'] = txt[0]
		info['cov'] = txt[1].split('\n')[0]
except ValueError:
	print("Error open file !")
	raise

try:
	with open('/home/pi/aqn-ceri/dht/result','r') as f:
		txt = f.read().split(',')
		info['temp'] = txt[0]
		info['humid'] = txt[1].split('\n')[0]
except ValueError:
	print("error open file ! ")
	raise

try:
	with open('/home/pi/aqn-ceri/result','w') as f:
		f.write(json.dumps(info))
except ValueError:
	print('Error open file !')
	raise

port = "/dev/ttyACM0"

s1 = serial.Serial(port,115200)
s1.flushInput()

s1.write(json.dumps(info))


time.sleep(5)

