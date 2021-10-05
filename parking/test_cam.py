
import cv2
import imutils
import numpy as np
import pytesseract

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
while True:
    ret, img = cap.read()
    cv2.imshow("dasd", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break