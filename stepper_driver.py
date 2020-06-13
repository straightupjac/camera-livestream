import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class StepperDriver(object):
	
	def __init__(self, IN1, IN2, IN3, IN4):
		self.IN1 = IN1 #Blue wire
		self.IN2 = IN2 #Pink
		self.IN3 = IN3 #Yellow
		self.IN4 = IN4 #Orange
		GPIO.setup(self.IN1, GPIO.OUT)
		GPIO.setup(self.IN2, GPIO.OUT)
		GPIO.setup(self.IN3, GPIO.OUT)
		GPIO.setup(self.IN4, GPIO.OUT)
		self.setPins([0,0,0,0])

	def resetPins(self):
		GPIO.output(self.IN1, 0)
		GPIO.output(self.IN2, 0)
		GPIO.output(self.IN3, 0)
		GPIO.output(self.IN4, 0)
		#GPIO.cleanup()

	def setPins(self, arr):
		GPIO.output(self.IN1, arr[0])
		GPIO.output(self.IN2, arr[1])
		GPIO.output(self.IN3, arr[2])
		GPIO.output(self.IN4, arr[3])

	def set(self, pin, val):
		pin_map = {1 : self.IN1, 2:self.IN2, 3:self.IN3, 4:self.IN4}
		GPIO.output(pin_map[pin], val)
		time.sleep(0.001)

	def left(self): #clockwise
		self.setPins([0,0,0,1])
		self.set(1,0) #1
		self.set(3,1) #2
		self.set(4,0) #3
		self.set(2,1) #4
		self.set(3,0) #5
		self.set(1,1) #6
		self.set(2,0) #7
		self.set(4,1) #8

	def right(self): #counter clockwise
		self.setPins([1,0,0,1])
		self.set(4,1) #8
		self.set(2,0) #7
		self.set(1,1) #6
		self.set(3,0) #5
		self.set(2,1) #4
		self.set(4,0) #3
		self.set(3,1) #2
		self.set(1,0) #1
