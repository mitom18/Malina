import picamera
import time
import cv2

camera = picamera.PiCamera()

camera.start_preview()
time.sleep(10)
camera.stop_preview()


camera.close()
