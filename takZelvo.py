import RPi.GPIO as GPIO
from time import *

GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (18,GPIO.OUT)
print ("LED on")
GPIO.output (18,GPIO.HIGH)
sleep (1)
print ("LED off")
GPIO.output (18,GPIO.LOW)
