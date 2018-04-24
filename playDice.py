import picamera
import time
import cv2
import numpy as np
#from matplotlib import pyplot as plt
import RPi.GPIO as gpio
from time import sleep

gpio.setmode (gpio.BOARD)
print ("zacatek motoru")
gpio.setup (11, gpio.OUT, initial = gpio.LOW)
sleep (1)
gpio.output (11, gpio.HIGH)
sleep (2)
gpio.output (11, gpio.LOW)
gpio.cleanup()
print ("konec motoru")

sleep (2)

camera = picamera.PiCamera()

camera.capture('image.jpg')

camera.close()
"""
img = cv2.imread('image.jpg')
img2 = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

lower_green = np.array([50,0,0])
upper_green = np.array([90,255,255])

mask = cv2.inRange(hsv_img, lower_green, upper_green)

kernel = np.ones((15,15),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

res = img2#cv2.bitwise_and(img2,img2, mask= closing)
cerne = []
for y in range (len (closing)):
  for x in range (len (closing [y])):
    if (closing [y][x] != 0):
      cerne.append ([x,y])
nejvX = 0
nejvY = 0
nejmX = len (closing [0])
nejmY = len (closing)
for i in cerne:
  if (i [0] > nejvX):
    nejvX = i [0]
  if (i [1] > nejvY):
    nejvY = i [1]
  if (i [0] < nejmX):
    nejmX = i [0]
  if (i [1] < nejmY):
    nejmY = i [1]
    """

img = cv2.imread('image.jpg',cv2.CV_8UC1)
dice = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#ret,thresh1 = cv2.threshold(dice,110,255,cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(dice,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

#kernel = np.ones((10,10),np.uint8)
#opening = cv2.morphologyEx(thresh2, cv2.MORPH_OPEN, kernel)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(thresh2, cv2.MORPH_CLOSE, kernel)

pocetPuntiku = 0
ukoly = []
for y in range (len (closing)):
  for x in range (len (closing [y])):
    if (closing [y][x] == 0):
      closing [y][x] = 128
      pocetPuntiku += 1
      ukoly.append ([x,y])
      while (len (ukoly) > 0):
        a = ukoly.pop (0)
        if (closing [a [1] + 1][a [0]] == 0):
          closing [a [1] + 1][a [0]] = 128
          ukoly.append ([a [0], a[1] + 1])
        if (closing [a [1] - 1][a [0]] == 0):
          closing [a [1] - 1][a [0]] = 128
          ukoly.append ([a [0], a[1] - 1])
        if (closing [a [1]][a [0] + 1] == 0):
          closing [a [1]][a [0] + 1] = 128
          ukoly.append ([a [0] + 1, a[1]])
        if (closing [a [1]][a [0] - 1] == 0):
          closing [a [1]][a [0] - 1] = 128
          ukoly.append ([a [0] - 1, a[1]])
      """
      pocetPuntiku += 1
      zmena = 1
      closing [y][x] = 128
      while (zmena):
        zmena = 0
        for yy in range (1, len (closing) - 1):
          for xx in range (1, len (closing [yy]) - 1):
            if (closing [yy][xx] == 128 ):
              if (closing [yy - 1][xx] == 0):
                closing [yy - 1][xx] = 128
                zmena = 1
              if (closing [yy + 1][xx] == 0):
                closing [yy + 1][xx] = 128
                zmena = 1
              if (closing [yy][xx - 1] == 0):
                closing [yy][xx - 1] = 128
                zmena = 1
              if (closing [yy][xx + 1] == 0):
                closing [yy][xx + 1] = 128
                zmena = 1"""
print (pocetPuntiku)

cv2.imshow('blue', closing)
cv2.waitKey(0)
