import cv2
import numpy as np
global sayac
kamera = cv2.VideoCapture(0)
dusuk = np.array([0, 170, 50])
yuksek = np.array([6, 255, 255])
dusuk2=np.array([175,170,50])
yuksek2=np.array([180,255,255])
while True:
    ret, frame = kamera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, dusuk, yuksek)
    mask2=cv2.inRange(hsv,dusuk2,yuksek2)
    median = cv2.medianBlur(mask, 15)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #histogram esitleme
    clahe = cv2.createCLAHE(clipLimit=20.0, tileGridSize=(8, 8))
    cl1 = clahe.apply(median)

    _, thresh = cv2.threshold(cl1, 85, 255, 0)
    _, thresh2 = cv2.threshold(median, 85, 255, 0)
    M = cv2.moments(thresh)
    C = cv2.moments(thresh2)

    if M["m00"] != 0 and C["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cZ = int(C["m10"] / C["m00"])
        cW = int(C["m01"] / C["m00"])

    else:
        cX, cY, cZ, cW = 0, 0, 0, 0
        daire = cv2.HoughCircles(median, cv2.HOUGH_GRADIENT, 1, median.shape[0] / 2, param1=200, param2=10, minRadius=50, maxRadius=150)

    if daire is not None:
        daire = np.uint16(np.around(daire))

        for i in daire[0, :]:
            cv2.circle(median, (i[0], i[1]), i[2], (255, 0, 255), 2)
            median = cv2.circle(median, (i[0], i[1]), i[2], (255, 255, 0), 2)

            cv2.circle(median, (cX, cY), 5, (150, 250, 250), -1)
            cv2.putText(median, "kamera merkezi", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 250, 250), 2)

            cv2.circle(median, (cZ, cW), 5, (150, 250, 250), -1)
            cv2.putText(median, "cisim merkezi", (cZ - 25, cW - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 250, 250), 2)

    def alanSay(cevre):
        global mask
        mask=cv2.inRange(cevre,dusuk,yuksek)
        suAlan=cv2.countNonZero(mask)
        sayac=0+suAlan
        return sayac

    def ekran_merkezine_daire_ciz(merkezx, merkezy, cap):  # satir80
         cv2.circle(median, (merkezx, merkezy), cap, (255, 255, 255), 3)
    ekran_merkezine_daire_ciz(320, 240, 100)

    if 220 < cZ < 420 and 140 < cW < 340:
        ekran_merkezine_daire_ciz(320, 240, 100)
        #cv2.putText(median, "ALGILANDI", (cZ - 25, cW - 25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (150, 250, 250), 2)
        cv2.putText(median, 'ALGILANDI', (170, 420), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (100, 250, 250), 2,
                            cv2.LINE_AA)
        cv2.putText(median, 'author: A T U G E M  U A V', (20, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (255, 250, 250), 2, cv2.LINE_AA)
        cv2.imshow("ana", median)