import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
dusuk=np.array([1, 10, 10])
yuksek=np.array([6, 255, 255])

while True:

    ret,goruntu=kamera.read()
    hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    median=cv2.medianBlur(mask,15)

    daire=cv2.HoughCircles(median,cv2.HOUGH_GRADIENT,1,median.shape[0]/2,param1=200,param2=10,minRadius=15,maxRadius=70)

    if daire is not None:
        daire=np.uint16(np.around(daire))

        for i in daire[0,:]:
            cv2.circle(median,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.imshow("resim",median)

    if cv2.waitKey(25)&0xFF==ord('q'):
        break