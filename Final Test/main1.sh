python login.py
echo "pls wait , face verification starting ..."
python face_auth.py
echo "pls wait , intializing the system ..."
python headpose_esti.py &
python quiz.py  
killall python