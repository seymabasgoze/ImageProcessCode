import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
dusuk=np.array([1, 10, 10])
yuksek=np.array([6, 255, 255])

while True:

    ret,goruntu=kamera.read()
    hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,dusuk,yuksek)
    asilResim=cv2.bitwise_and(goruntu,goruntu,mask=mask)
    blur=cv2.GaussianBlur(asilResim,(15,15),0)
    median=cv2.medianBlur(asilResim,15)

    cv2.imshow("görüntü",goruntu)
    cv2.imshow("renk algılama",asilResim)
    cv2.imshow("median",median)
    cv2.imshow("maske",mask)
    cv2.imshow("blur",blur)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
