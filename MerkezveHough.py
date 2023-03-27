import cv2
import numpy as np

import argparse

cap=cv2.VideoCapture(0)
dusuk=np.array([1, 10, 10])
yuksek=np.array([6, 255, 255])

while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, dusuk, yuksek)
    median = cv2.medianBlur(mask, 15)
    _,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    _,contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    M=cv2.moments(thresh)
   #print(M)
    x=int(M["m10"]/M["m00"])
    y=int(M["m01"]/M["m00"])

    daire = cv2.HoughCircles(median, cv2.HOUGH_GRADIENT, 1, median.shape[0] / 2, param1=200, param2=10, minRadius=50, maxRadius=70)
    if daire is not None:
        daire = np.uint16(np.around(daire))

        for i in daire[0, :]:
            cv2.circle(median, (i[0], i[1]), i[2], (150, 250, 250), 2)
            median=cv2.circle(median, (i[0], i[1]), i[2], (150, 250, 250), 2)

        cv2.drawContours(median,contours,-1,(0,0,255),5)
        cv2.circle(median,(x,y),5,(150,10,10),-1)
        cv2.imshow("merkez",median)
        cv2.imshow("frame",median)
        if cv2.waitKey(5) & 0XFF == ord('q'):
            break

cap.release()
cv2.waitKey()