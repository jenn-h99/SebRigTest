import time
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#DEFINE PINS
limitpin = 16

#INITIALIZE PINS
GPIO.setup(limitpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#SCRIPT
loopstat = 1
while loopstat > 0:
    if GPIO.input(limitpin):
        print('open')
    else:
        print('TRIGGERED')