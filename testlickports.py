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
    if not GPIO.input(leftlickport):
        print('<----LEFT')
    elif not GPIO.input(rightlickport):
        print('RIGHT---->')
    elif not GPIO.input(leftlickport) and GPIO.input(rightlickport):
        print('<-BOTH->')
    else:
        print('-')
    time.sleep(0.01)
