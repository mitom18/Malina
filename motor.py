import RPi.GPIO as gpio
from time import sleep

gpio.setmode (gpio.BOARD)

gpio.setup (11, gpio.OUT, initial = gpio.LOW) #enable
sleep (1)
gpio.output (11, gpio.HIGH)
sleep (2)
gpio.output (11, gpio.LOW)
gpio.cleanup()
