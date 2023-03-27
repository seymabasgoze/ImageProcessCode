import cv2
import numpy as np
# convert image to grayscale image
kamera = cv2.VideoCapture(0)
dusuk=np.array([1, 10, 10])
yuksek=np.array([6, 255, 255])
while True:
    ret,frame = kamera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, dusuk, yuksek)
    median = cv2.medianBlur(mask, 15)
    # convert the grayscale image to binary image
    ret,thresh = cv2.threshold(median,127,255,0)

    # calculate moments of binary image
    M = cv2.moments(thresh)

    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    daire = cv2.HoughCircles(median, cv2.HOUGH_GRADIENT, 1, median.shape[0] / 2, param1=200, param2=10, minRadius=50, maxRadius=70)
    if daire is not None:
        daire = np.uint16(np.around(daire))

        for i in daire[0, :]:
            cv2.circle(median, (i[0], i[1]), i[2], (150, 250, 250), 2)
            median = cv2.circle(median, (i[0], i[1]), i[2], (150, 250, 250), 2)
    # put text and highlight the center
    cv2.circle(median, (cX, cY), 5, (150, 250, 250), -1)
    cv2.putText(median, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 250, 250), 2)

    cv2.imshow("Image", median)

    if cv2.waitKey(3) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()