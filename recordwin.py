import numpy as np
import cv2
from PIL import ImageGrab
import win32api
import winGuiAuto
import win32gui
import win32con

cap = cv2.VideoCapture(0)

# Capture the window frame by frame
image_list = []
for _ in range(70):
    ret, frame = cap.read()
    cv2.imshow('SCORE',frame)
    cv2.waitKey(1)
    hwnd = winGuiAuto.findTopWindow("SCORE")
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
    win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    rect = win32gui.GetWindowPlacement(hwnd)[-1]
    image = ImageGrab.grab(rect)
    image_list.append(image)

height,width,channel = np.array(image).shape
cap.release()
cv2.destroyAllWindows()


out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, (width,height))
 
for images in image_list:
    out.write(cv2.cvtColor(np.array(images),cv2.COLOR_BGR2RGB))
out.release()

# Save into .gif
#import imageio
#image_gif = []
#for images in image_list:
#    print(np.array(images))
#    image_gif.append(np.array(images))
#imageio.mimsave('movie.gif', image_gif,duration=0.2)