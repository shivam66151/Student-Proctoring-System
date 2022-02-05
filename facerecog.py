import cv2 as cv
import os
import numpy as np

# face detection

img = cv.imread('lady.jpg')
cv.imshow('Group of 5 people',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People',gray)

#cascadeClassifier

haar_cascade = cv.CascadeClassifier('haar_face.xml')

cv.destroyAllWindows()
cv.waitKey(60)