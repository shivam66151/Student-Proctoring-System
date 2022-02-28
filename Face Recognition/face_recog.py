import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

datapath = 'C:/Users/sharm/OneDrive/Desktop/Student Proctoring System/Face Recognition/capturedfaces/'

onlyfiles = [f for f in listdir(datapath) if isfile(join(datapath, f))]

Datatraining, labels = [], []

for i, files in enumerate(onlyfiles):
	faces_path = datapath + onlyfiles[i]
	face_img = cv2.imread(faces_path, cv2.IMREAD_GRAYSCALE)
	Datatraining.append(np.asarray(face_img, dtype = np.uint8))
	labels.append(i)

labels = np.asarray(labels, dtype = np.int32)


model_recog = cv2.face.LBPHFaceRecognizer_create()

model_recog.train(np.asarray(Datatraining), np.asarray(labels))

print("Training Completed Sir!!!")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def face_detection(img, size = 0.5):
	graycol = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(graycol, 1.3, 5)

	if faces is():
		return img, []

	for(x,y,w,h) in faces:
		cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
		roi = img[y: y+h, x:x+w]
		roi = cv2.resize(roi, (200, 200))


	return img,roi


cap = cv2.VideoCapture(0)
while True:

	ret, frame = cap.read()

	image, face = face_detection(frame)

	try:
		face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
		result = model_recog.predict(face)

		if result[1] < 500:
			confidence = int(100 *(1 -(result[1])/300))
			display_string = str(confidence)+'% Confidence it is user'
			cv2.putText(image,display_string,(100,120), cv2.FONT_HERSHEY_COMPLEX,1,(250, 120, 255),2)

		if confidence > 75:
			cv2.putText(image, "Access Granted", (250 , 450), cv2.FONT_HERSHEY_COMPLEX,1,(0,255, 0),2)
			cv2.imshow('Face Crop', image)
		else:
			cv2.putText(image, "Access Denied", (250 , 450), cv2.FONT_HERSHEY_COMPLEX,1,(0,0, 255),2)
			cv2.imshow('Face Crop', image)

	except:
		cv2.putText(image, "Face Not Found", (250 , 450), cv2.FONT_HERSHEY_COMPLEX,1,(255,0, 0),2)
		cv2.imshow('Face Crop', image)
		pass

	if cv2.waitKey(1) == 13:
		break

cap.release()
cv2.destroyAllWindows()



    
