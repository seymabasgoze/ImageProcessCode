import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
while True:
    ret,goruntu=kamera.read()
    gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    median=cv2.medianBlur(gri,15)
    daireler=cv2.HoughCircles(median,cv2.HOUGH_GRADIENT,1,median.shape[0]/3,param1=200,param2=10,minRadius=10,maxRadius=70)

    if daireler is not None:
        daireler=np.uint16(np.around(daireler))
        for i in daireler[0,:]:
            cv2.circle(median,(i[0],i[1]),i[2],(75,0,130),2)
    cv2.imshow("kamera",median)

    if cv2.waitKey(25)&0xFF==ord('q'):
        break
