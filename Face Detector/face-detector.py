import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
#cv2.namedWindow('Remote', cv2.WINDOW_AUTOSIZE)
while True:
    _, img = cap.read()
#face = cv2.imread('selena.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
#faces = face_cascade.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0), thickness = 2)
    

    cv2.imshow('img',img)
    key = cv2.waitKey(30) & 0Xff
    if key ==27:
        break

cap.release()


