import RPi.GPIO as GPIO
import time

class Motor(object):
	
	def __init__(self, ForwardA, BackwardA, ForwardB, BackwardB, mhz = 100):
		self.mhz = mhz
		self.ForwardA = ForwardA
		self.BackwardA = BackwardA
		self.ForwardB = ForwardB
		self.BackwardB = BackwardB
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(self.ForwardB, GPIO.OUT)
		GPIO.setup(self.BackwardB, GPIO.OUT)
		GPIO.setup(self.ForwardA, GPIO.OUT)
		GPIO.setup(self.BackwardA, GPIO.OUT)
		self.m1 = GPIO.PWM(self.ForwardA, self.mhz)
		self.m2 = GPIO.PWM(self.BackwardA, self.mhz)
		self.m3 = GPIO.PWM(self.ForwardB, self.mhz)
		self.m4 = GPIO.PWM(self.BackwardB, self.mhz)

	def backward(self, speed):
		if(speed > 100):
			speed = 100
		self.m2.start(speed)
		GPIO.output(self.BackwardA, True)
		self.m4.start(speed)
		GPIO.output(self.BackwardB, True)
						
	def forward(self, speed):
		if(speed > 100):
			speed = 100
		self.m1.start(speed)
		GPIO.output(self.ForwardA, True)
		self.m3.start(speed)
		GPIO.output(self.ForwardB, True)
		
	def stop(self):
		self.m1.stop()		
		self.m2.stop()		
		self.m3.stop()		
		self.m4.stop()
				
	def finish(self):
		GPIO.cleanup()
			
						
		
