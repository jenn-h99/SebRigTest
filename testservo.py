import time
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#DEFINE PINS
servopin = 13

#INITIALIZE PINS
GPIO.setup(servopin, GPIO.OUT)
servopwm = GPIO.PWM(servopin, 50) #sets the PWM duty cycle 50Hz is for 20ms for the SG90
# 1ms or 20ms is 0 degrees, 1.5ms of 20ms is 90 degress, 2ms of 20ms is 180 degrees.
servopwm.start(0)

#SCRIPT
loopstat = 1

while loopstat > 0:
    enterangle = input('Enter position (0-180 degrees)')
    pwmcalc = (enterangle * 0.027) + 5
    servopwm.ChangeDutyCycle(pwmcalc)

