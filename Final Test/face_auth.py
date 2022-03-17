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


    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

             # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(remove(name))

            font = cv2.FONT_HERSHEY_DUPLEX
            if len(face_names) > 1:
              cv2.putText(frame, "More than 1 Faces Detected", (20 , 440), font, 1.0, (255, 255, 255), 1)
            elif len(face_names) == 1 and face_names[0] == "Unknown":
              cv2.putText(frame, "Unknown", (20,440), font, 1.0, (255, 255, 255), 1)
              rest_count = rest_count + 1
            elif len(face_names) == 1 and face_names[0] == username:
              cv2.putText(frame, "Success", (20 , 440), font, 1.0, (255, 255, 255), 1)
              count = count + 1

            if (count/rest_count) > 5 :
             print("Sucessfull Verification")
             sys.exit()
    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

     # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   

# Release handle to the webcam
cap.release()
cv2.destroyAllWindows() 

            

