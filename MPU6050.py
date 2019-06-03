import smbus			#import SMBus module of I2C
from time import sleep          #import


class mpu6050(object):
	def __init__(self):
		self.PWR_MGMT_1   = 0x6B
		self.SMPLRT_DIV   = 0x19
		self.CONFIG       = 0x1A
		self.GYRO_CONFIG  = 0x1B
		self.INT_ENABLE   = 0x38
		self.ACCEL_XOUT_H = 0x3B
		self.ACCEL_YOUT_H = 0x3D
		self.ACCEL_ZOUT_H = 0x3F
		self.GYRO_XOUT_H  = 0x43
		self.GYRO_YOUT_H  = 0x45
		self.GYRO_ZOUT_H  = 0x47
		self.Device_Address = 0x68
		self.bus = smbus.SMBus(1)
		
	def MPU_Init(self):
		#write to sample rate register
		self.bus.write_byte_data(self.Device_Address, self.SMPLRT_DIV, 7)
		#Write to power management register
		self.bus.write_byte_data(self.Device_Address, self.PWR_MGMT_1, 1)
		#Write to Configuration register
		self.bus.write_byte_data(self.Device_Address, self.CONFIG, 0)
		#Write to Gyro configuration register
		self.bus.write_byte_data(self.Device_Address, self.GYRO_CONFIG, 24)
		#Write to interrupt enable register
		self.bus.write_byte_data(self.Device_Address, self.INT_ENABLE, 1)
	
	def read_raw_data(self,addr):
		#Accelero and Gyro value are 16-bit
		high = self.bus.read_byte_data(self.Device_Address, addr)
		low = self.bus.read_byte_data(self.Device_Address, addr+1)
		
		#concatenate higher and lower value
		value = ((high << 8) | low)
			
		#to get signed value from mpu6050
		if(value > 32768):
			value = value - 65536
		return value
	
	def getAccelX(self):
		return self.read_raw_data(self.ACCEL_XOUT_H)
	
	def getAccelY(self):
		return self.read_raw_data(self.ACCEL_YOUT_H)
	
	def getAccelZ(self):
		return self.read_raw_data(self.ACCEL_ZOUT_H)	
	def getGyroX(self):
		return self.read_raw_data(self.GYRO_XOUT_H)
	
	def getGyroY(self):
		return self.read_raw_data(self.GYRO_YOUT_H)
	
	def getGyroZ(self):
		return self.read_raw_data(self.GYRO_ZOUT_H)
		
		
				
