# Run a program through cmd to prevent frame delay
# sekai version
import os
import time
import pyautogui 

def run_sekai():
    time.sleep(0.5)
    os.system("start cmd /k cd C:\\Users\\villo\\OneDrive\\Desktop\\ASCII Art Program") #C:\\User\Name\\Location\\Document\Folder
    time.sleep(1)
    pyautogui.write("python SEKAI_VER_Bad_Apple!!.py", interval=0.1) # run better without after frames
    pyautogui.press("enter") # executing
    time.sleep(0.5)
    pyautogui.hotkey("f11")  # Fullscreen

if __name__ == "__main__":
    run_sekai()
