python login.py
echo "pls wait , face verification starting ..."
python face_auth.py
echo "pls wait , intializing the system ..."
python headpose_esti.py &
python gaze_tracking.py &
python person and phone.py &
python oral_Detector.py &
python mousepos.py &
python recorder.py &
python quiz.py  
killall python