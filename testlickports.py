import time
import RPi.GPIO as GPIO

# setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# DEFINE PINS
leftlickport = 10
rightlickport = 9


# INITIALIZE PINS
GPIO.setup(leftlickport, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightlickport, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# SCRIPT
loopstat = 1
while loopstat > 0:
    leftl = 0
    rightl = 0
    if GPIO.input(leftlickport):
        leftl = 1
    if GPIO.input(rightlickport):
        right = 1
    print('left: ',leftl,'    right: ',rightl)
    time.sleep(0.01)
