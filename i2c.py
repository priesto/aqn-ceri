import smbus
import time

bus = smbus.SMBus(1)

data = bus.read_i2c_block_data(0x5a, 0)

prediction = data[0] * 256 + data[1]
time.sleep(10)
result = ''
while 1:
	# 450 - 2000
	data = bus.read_i2c_block_data(0x5a, 0)
	data[2] = data[2] & 1
	if data[2] == 0:
		prediction = data[0] * 256 + data[1]
		cov = data[7] * 256 + data[8]
		if prediction >= 150 and prediction < 2000:
			try:
				with open('/home/pi/Desktop/co2','w') as f:
					result = str(prediction)+','+str(cov)
					f.write(result)
			except ValueError:
				console.log("Error open file !")
				raise
		else:
			pass
	time.sleep(10)
