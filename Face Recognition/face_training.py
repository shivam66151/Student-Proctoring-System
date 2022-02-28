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
    
