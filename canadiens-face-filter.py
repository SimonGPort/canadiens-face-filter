import cv2


wCam, hCam=640,480

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    succes,img=cap.read()

    cv2.imshow("Img",img)
    cv2.waitKey(1)
