import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    ret,thresh = cv2.threshold(mask,127,255,0)
    M = cv2.moments(thresh)

    dM01 = int(M["m01"])
    dM10 = int(M["m10"])
    dArea = int(M["m00"])
    
    if dArea > 10000:

        posX = dM10 / dArea
        posY = dM01 / dArea

        R = math.sqrt((dArea / 255) / 3.14)
        realR = 4
        f = -10
        fpx = 750
        d = (realR*fpx) / R + f
        print("Distance: ")
        print(d)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
