'''
Just a file for playing with different OpenCV methods and attributes
'''

import cv2
import numpy as np

cv2.namedWindow("frame")
vc = cv2.VideoCapture(0)


while (1):
    _, frame = vc.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([255,255,130])
    upper_orange = np.array([0, 128, 255])
    lower_orange = np.array([204, 229, 255])
    lower_ = np.array([255,255,0])
    upper_ = np.array([0,255,255])

    # Threshold the HSV image to get only blue colors
    blueMask = cv2.inRange(hsv, lower_blue, upper_blue)
    orangeMask = cv2.inRange(hsv, lower_orange, upper_orange)
    mask = cv2.inRange(hsv, lower_, upper_)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= blueMask)


    cv2.imshow('mask',blueMask)
    cv2.imshow('res',res)
    cv2.imshow("frame", frame)

    b, g, r = cv2.split(frame)
    cv2.imshow('red', r)
    cv2.imshow('blue', b)
    cv2.imshow('green', g)
    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

vc.release()
cv2.destroyAllWindows()
