# Proctoring System

An AI Based Proctoring System Project to create an automated proctoring system where the user can be monitored automatically through the webcam and microphone.

## Prerequisites
For Foresight 
```bash
pip install opencv-python
pip install dlib
pip install tensorflow
pip install scikit
pip install imutils
pip install mediapipe
```
For Audio
```bash
pip install speech-recognition
pip install pyaudio
pip install wave
pip install threading
```
## Foresight
It has six foresight based functionalities right now:
1. Track eyeballs and report if candidate is looking left, right or up.
2. Find if the candidate opens his mouth by recording the distance between lips at starting.
3. Track the position of mouse cursor and take screenshot when cursor goes out of certain frames.
4. Find and report any instances of mobile phones.
5. Head pose estimation to find where the person is looking.
6. Face Authentication to make sure real user is using the system

## Contributing

If you have any other ideas or do any step of to do consider making a pull request . Please update the README as well in the pull request.

## License
[MIT](https://choosealicense.com/licenses/mit/)
