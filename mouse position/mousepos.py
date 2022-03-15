## Tell mouse position after certain period of time
from pynput.mouse import Controller
import time
import pyautogui

mouse = Controller()
 # Read pointer position
 #return mouse.position
time.sleep(10)

count = 0
def take_screenshot():
    screenshot = pyautogui.screenshot()
    save_path = 'C:/Users/Shivam Sharma/Proctoring-Sys/mouse position/screenshots/'
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
