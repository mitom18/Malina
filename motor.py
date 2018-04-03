import RPi.GPIO as gpio
from time import sleep

gpio.setmode (gpio.BOARD)

gpio.setup (11, gpio.OUT, initial = gpio.LOW)
sleep (1)
gpio.output (11, gpio.HIGH)
sleep (5)
gpio.output (11, gpio.LOW)
gpio.cleanup()
