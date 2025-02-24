import keyboard
from capture import Capturing
from reader import Reading
from panel_detection import Slice 
import os
import shutil

def main():
    print("run")
    loop = True
    runningCapture = False
    runningReader = False
    haveCords = False
    count  = 0

    while loop:
        count+=1
        if keyboard.is_pressed("w") and not runningCapture and not runningReader: #exits loop at keypress w
            loop = False
        if keyboard.is_pressed("y") and not runningCapture and not runningReader:
            runningCapture = True
            Capturing.getCords(runningCapture) #runs capture program to get cords of screen (press this first)
            haveCords = True
            runningCapture = False
        if keyboard.is_pressed("x") and not runningCapture and not runningReader and haveCords: #takes ss of and reads screen with alr chosen cords 
            runningReader = True
            Capturing.screenshot(runningReader)
            Slice.split_panels()
            Reading.read(runningReader)
            runningReader = False
    print("done")

if __name__ == "__main__":
    main()