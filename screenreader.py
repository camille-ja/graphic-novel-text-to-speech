#https://pyautogui.readthedocs.io/en/latest/quickstart.html
import pyautogui
from PyQt5.QtWidgets import QWidget, QApplication, QRubberBand
from PyQt5.QtGui import QCursor, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QRect
import time

#creates a big window that's transparent so it looks like user is drawing on their screen
class Capture(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main = main_window
        self.main.hide()

        self.setMouseTracking(True)
        desk_size = QApplication.desktop() #grabs cords of screen
        self.setGeometry(0, 0, desk_size.width(), desk_size.height() ) #sets size of area to desktop
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint) #makes the window frameless
        self.setWindowOpacity(0.15) #window is basically transparent

        self.rubber_band = QRubberBand(QRubberBand.Rectangle, self) #shows dimensions of new bounding area
        self.origin = QPoint()

        QApplication.setOverrideCursor(Qt.CrossCursor)
        screen = QApplication.primaryScreen()
        rect = QApplication.desktop().rect()

        time.sleep(0.35) #If you're capturing multiple ss it won't get the capture frame in the ss
        self.imgmap = screen.grabWindow(
            QApplication.desktop().winId(), #takes ss of entire window
            rect.x(), rect.y(), rect.width(), rect.height()
        )

    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.LeftButton:
            #When mouse is clicked the first time, you should be in the top left corner
            self.origin = event.pos() #Gets the top left corner from the first click
            self.rubber_band.setGeometry(QRect(self.origin, event.pos()).normalized()) #Creates a rectangle using top left corner & changing variable
            self.rubber_band.show()

    

    def mouseMoveEvent(self, event:QMouseEvent | None) -> None:
        if not self.origin.isNull():
            self.rubber_band.setGeometry(QRect(self.origin,event.pos()).normalized()) #Expands the rectangle once top left corner is defined
    
    #takes ss when mouse is released
    def mouseReleaseEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.LeftButton:
            self.rubber_band.hide() #hides the created screen

            rect = self.rubber_band.geometry() #stores the created rectangle
            print(self.rubber_band.shape())
            self.imgmap = self.imgmap.copy(rect) 
            QApplication.restoreOverrideCursor() #stops looking at the cursor/ screen

            #set image clipboard (allows you to temporarliy store the image)
            clipboard = QApplication.clipboard()
            clipboard.setPixmap(self.imgmap)

            self.main.label.setPixmap(self.imgmap)
            self.main.show()

            self.close()




def get_image():
    pyautogui.confirm('Move to top left and press enter')
    print(pyautogui.size())
    position = pyautogui.position()
    min_x = position.x
    min_y = position.y
    print(min_x,min_y)
    pyautogui.confirm('Move to bottom right and press enter')
    position = pyautogui.position()
    max_x = position.x
    max_y = position.y
    print(max_x, max_y)
    pyautogui.alert('The cordinates of your screen: ' + str(min_x) + ", " + str(min_y) + ", " + str(max_x) + ", " + str(max_y))
    pyautogui.sleep(5)
    return pyautogui.screenshot( 'my_image.png', region=(min_x,min_y,max_x,max_y))



