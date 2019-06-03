from MPU6050 import mpu6050
from PID import PID
from Motor import Motor
import math
import time
import RPi.GPIO as GPIO





def distance(a, b):
	return math.sqrt((a*a) + (b*b))

def get_y_rotation(x,y,z):
	radians = math.atan2(x, distance(y,z))
	return -math.degrees(radians)	

def get_x_rotation(x,y,z):
	radians = math.atan2(y, distance(x,z))
	return math.degrees(radians)	
	
	

#currAngle = 0.0
mpu = mpu6050()
mpu.MPU_Init()
targetAngle = -0.50
p = PID(100.0, 0.0, 0)
p.setPoint(-0.5)
motor = Motor(27, 22 , 4, 17)
accelXoffset = 0.0
accelYoffset = 0.0
accelZoffset = 0.0
gyroXoffset = 0.0
gyroYoffset = 0.0
gyroZoffset = 0.0
angle_pitch = 0.0
angle_roll = 0.0
angle_pitch_output = 0.0


#Calculating Offsets
for i in range(0,1000):
	accelXoffset += mpu.getAccelX()
	accelYoffset += mpu.getAccelY()
	accelZoffset += mpu.getAccelZ()
	gyroXoffset += mpu.getGyroX()
	gyroYoffset += mpu.getGyroY()
	gyroZoffset += mpu.getGyroZ()
	time.sleep(0.003)

accelXoffset /= 1000
accelYoffset /= 1000
accelZoffset /= 1000
gyroXoffset /= 1000
gyroYoffset /= 1000
gyroZoffset /= 1000
			

	
while True:
	time.sleep(0.004)
	
	accelX = mpu.getAccelX()
	accelY = mpu.getAccelY()
	accelZ = mpu.getAccelZ()
	
	gyroX = mpu.getGyroX()
	gyroY = mpu.getGyroY()
	gyroZ = mpu.getGyroZ()
	
		
	accelX -= accelXoffset
	accelY -= accelYoffset
	accelZ -= accelZoffset
	gyroX -= gyroXoffset
	gyroY -= gyroYoffset
	gyroZ -= gyroZoffset
	
	angle_pitch += gyroX*0.0000611
	angle_roll += gyroY*0.0000611
	 
	
	accelAngle = get_x_rotation(accelX, accelY, accelZ)
	angle_pitch = angle_pitch*0.9960 + accelAngle*0.004
	
	
	print('Angle of Inclination: {}'.format(angle_pitch))
	#motorspeed = int(p.update(currAngle, 0.004))
	#print('Motor:{}'.format(motorspeed))
	
	#if motorspeed > 0:
	#	motor.forward(motorspeed)
	#elif motorspeed < 0:
	#	motor.backward(abs(motorspeed))
	#else:
	#	motor.stop()		
		
	

	
