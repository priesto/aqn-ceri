import json
import time
import serial
import os

info = {}

try:
	with open('/home/pi/aqn-ceri/dht/result','r') as f:
		txt = f.read().split(',')
		info['co2'] = txt[0]
		info['cov'] = txt[1].split('\n')[0]
except ValueError:
	print("Error open file !")
	raise

try:
	with open('/home/pi/aqn-ceri/i2c/result','r') as f:
		txt = f.read().split(',')
		info['temp'] = txt[0]
		info['humid'] = txt[1].split('\n')[0]
except ValueError:
	print("error open file ! ")
	raise

try:
	with open('/home/pi/aqn-ceri/result.json','w') as f:
		f.write(json.dumps(info))
except ValueError:
	print('Error open file !')
	raise



if not os.path.isfile('/home/pi/aqn-ceri/result.hist.json'):
	with open('/home/pi/aqn-ceri/result.hist.json', 'w+') as f:
		data = []
		data.append(info)
		f.write(json.dumps(data))

else:
	with open('/home/pi/aqn-ceri/result.hist.json', 'r') as f:
		data = json.load(f)
		data.append(info)

	with open('/home/pi/aqn-ceri/result.hist.json', 'w') as f:
		f.write(json.dumps(data))


port = "/dev/ttyACM0"

s1 = serial.Serial(port,115200)
s1.flushInput()

s1.write(json.dumps(info))


time.sleep(5)
