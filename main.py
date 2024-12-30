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
    count  = 0

    while loop:
        count+=1
        if keyboard.is_pressed("w") and not runningCapture and not runningReader: #exits loop at keypress w
            loop = False
        if keyboard.is_pressed("y") and not runningCapture and not runningReader:
            runningCapture = True
            Capturing.getCords(runningCapture) #runs capture program to get cords of screen (press this first)
            runningCapture = False
        if keyboard.is_pressed("x") and not runningCapture and not runningReader: #takes ss of and reads screen with alr chosen cords 
            runningReader = True
            Capturing.screenshot(runningReader)
            Slice.split_panels()
            Reading.read(runningReader)
            runningReader = False
    print("done")
    if os.path.exists('C:/Users/cjam2/graphic novel text to speech/panels/panels'):
        shutil.rmtree('C:/Users/cjam2/graphic novel text to speech/panels/panels')
    


if __name__ == "__main__":
    main()
    