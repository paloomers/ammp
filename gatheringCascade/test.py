import cv2
import sys
import numpy as np
import cv2


#this is the cascade we just made. Call what you want
airpod = cv2.CascadeClassifier('cascadecopy.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # add this
    # image, reject levels level weights.
    airpods = airpod.detectMultiScale(gray, 1.3, 5)
    
    # add this
    for (x,y,w,h) in airpods:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()