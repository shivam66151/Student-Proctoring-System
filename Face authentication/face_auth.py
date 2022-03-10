import face_recognition
import cv2
import numpy as np
import sys
import pandas as pd
import re
import time

try:
    cap = cv2.VideoCapture(0)
except:
    print("Your camera is not working , pls fix it to attempt the test ..")
    print("After fixing pls restart the test")
    time.sleep(5*60)

#learn how to recognize using face_Recog sample picture
shivam_image = face_recognition.load_image_file("shivam.jpg") 
shivam_face_encoding = face_recognition.face_encodings(shivam_image)[0]

ayush_image = face_recognition.load_image_file("ayush.jpg")
ayush_face_encoding = face_recognition.face_encodings(ayush_image)[0]

shreya_image = face_recognition.load_image_file("shreya.jpg")
shreya_face_encoding = face_recognition.face_encodings(shreya_image)[0]

# Create arrays of known face encoding and their names
known_face_encodings = [
     shivam_face_encoding,
     ayush_face_encoding,
     shreya_face_encoding
]

known_face_names = [
    "Shivam Sharma",
    "Ayush Kunbi",
    "Shreya Sharma",
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

## implement the authentic function to read from the file the username of the person whose autorization is required
def authentic():
    df = pd.read_csv('Record.csv')
    temp_l = list(df['UName'])
    return temp_l[len(temp_l)-1]

def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string)

#---------------------------------------------------------------------------------------------------------------

username = authentic()
print(username)
## count of sucess and count of the rest of the cases
count = 1
rest_count = 1

while True:
    # Grab a single frame of video
    ret, frame = cap.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
