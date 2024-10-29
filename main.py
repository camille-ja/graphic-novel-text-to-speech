import keyboard
from capture import Capturing
from reader import Reading

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
            Capturing.getCords(runningCapture) #runs capture program to get cords of screen
            runningCapture = False
        if keyboard.is_pressed("x") and not runningCapture and not runningReader: #takes ss of and reads screen with alr chosen cords
            runningReader = True
            Capturing.screenshot(runningReader)
            Reading.read(runningReader)
            runningReader = False
    print("done")
    


if __name__ == "__main__":
    main()
    