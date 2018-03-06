#import picamera
import time
import cv2
import numpy as np
#from matplotlib import pyplot as plt

"""
camera = picamera.PiCamera()

camera.start_preview()
time.sleep(10)
camera.stop_preview()


camera.close()
"""
img = cv2.imread('image.jpg')
img2 = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
hsv_img = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

lower_green = np.array([60,0,0])
upper_green = np.array([80,255,255])

mask = cv2.inRange(hsv_img, lower_green, upper_green)

kernel = np.ones((15,15),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
kernel = np.ones((3,3),np.uint8)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

res = cv2.bitwise_and(img2,img2, mask= closing)
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
    
dice = res[nejmY:nejvY, nejmX:nejvX]
print (nejvX, nejvY)
print (nejmX, nejmY)
cv2.imshow('blue', dice)
cv2.waitKey(0)
