import picamera
import time
import cv2
import numpy as np
#from matplotlib import pyplot as plt


camera = picamera.PiCamera()

camera.capture('image.jpg')

camera.close()

"""img = cv2.imread('image.jpg')
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
for y in range (len (closing)):
  for x in range (len (closing [y])):
    if (closing [y][x] == 0):
      pocetPuntiku += 1
      zmena = 1
      closing [y][x] = 128
      while (zmena):
        zmena = 0
        for yy in range (len (closing)):
          for xx in range (len (closing [yy])):
            if (closing [yy][xx] == 128):
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
                zmena = 1
print (pocetPuntiku)

cv2.imshow('blue', closing)
cv2.waitKey(0)
