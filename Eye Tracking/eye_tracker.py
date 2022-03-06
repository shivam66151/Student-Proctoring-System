import cv2
import numpy as np
#from eye_modules import faceDetector
import eye_modules as mod
cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	#grayscale
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# calling the face detector function
	image, face = mod.faceDetector(frame, gray_frame)

	# calling landmark detector 
	image, pointList = mod.faceLandmarkDetector(frame, gray_frame, face, False)


	cv2.imshow('Frames' , image)

	key = cv2.waitKey(1)

	if key == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()


