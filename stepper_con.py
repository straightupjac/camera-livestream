import RPi.GPIO as GPIO
import time
import json
import sys
from stepper_driver import StepperDriver
from python_websocket import *
from Queue import Empty
GPIO.setwarnings(False)

#Stepper 1 gpio pins
IN1 = 26 #Blue
IN2 = 19 #Pink
IN3 = 13 #yellow
IN4 = 6 #Orange
left_right_stepper = StepperDriver(IN1, IN2, IN3, IN4)

#Stepper 2 gpio pins
IN1 = 22  #Blue
IN2 = 27 #Pink
IN3 = 17 #yellow
IN4 = 4 #Orange
up_down_stepper = StepperDriver(IN1, IN2, IN3, IN4)

cont = True

turning_left = False
turning_right = False
turning_up = False
turning_down = False

socketQ = getSocket(sys.argv[1])
print ("Ready for commands")
try:
	while cont:
		try:
			cmd = json.loads(socketQ.get(True, 0.01))
			if cmd['val']=='panLeftDown':
				turning_left = True
				turning_right = False
			if cmd['val']=='panRightDown':
				turning_left = False
				turning_right = True
			if cmd['val']=='tiltFrontDown':
				turning_up = True
				turning_down = False
			if cmd['val']=='tiltBackDown':
				turning_up = False
				turning_down = True
			if cmd['val']=='panLeftUp':
				turning_left = False
			if cmd['val']=='panRightUp':
				turning_right = False
			if cmd['val']=='tiltFrontUp':
				turning_up = False
			if cmd['val']=='tiltBackUp':
				turning_down = False
			if cmd['val']=='stop':
				turning_left = False; 
				turning_right = False; 
				turning_down = False; 
				turning_up = False; 
		except Empty:
			pass
		if turning_left:
			left_right_stepper.left()
		if turning_right:
			left_right_stepper.right()
		if turning_up:
			up_down_stepper.right()
		if turning_down:
			up_down_stepper.left()

		if not (turning_left or turning_up or turning_down or turning_right):
			left_right_stepper.setPins([0,0,0,0])
			up_down_stepper.setPins([0,0,0,0])

except:
	cont = False
	print cont
	left_right_stepper.resetPins()
	up_down_stepper.resetPins()

finally:
	GPIO.cleanup()

