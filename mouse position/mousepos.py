## Tell mouse position after certain period of time
from pynput.mouse import Controller
import time
# from screenshot import click_screenshot
# from PIL import ImageGrab
import pyautogui
#def position():
mouse = Controller()
 # Read pointer position
 #return mouse.position
time.sleep(10)
# snapshot = ImageGrab.grab()
count = 0
def take_screenshot():
    screenshot = pyautogui.screenshot()
    # if take_screenshot() is not None:
    #     count += 1
    save_path = 'C:/Users/sharm/OneDrive/Desktop/Student Proctoring System/mouse position/'
    screenshot.save(save_path + "_screenshot.png")


while True:
    print(mouse.position)
    x,y = mouse.position
    if x < 566:
        print("you are going outside the screen")
        print("Clicking screenshot")
        take_screenshot()
    if x > 1348:
        print("you are going outside the screen")
        print("Clicking screenshot")
        take_screenshot()
    if y < 220:
        print("you are going outside the screen")
        print("Clicking screenshot")
        take_screenshot()
    if y > 888:
        print("you are going outside the screen")
        print("Clicking screenshot")
        take_screenshot()
    time.sleep(1)
# save_path = "C:/Users/sharm/OneDrive/Desktop/Student Proctoring System/mouse position/screenshots"+ str(count) + '.jpg'
# snapshot.save(save_path)