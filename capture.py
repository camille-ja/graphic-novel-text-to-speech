import sys
from PyQt5.QtWidgets import(
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QFrame,
    QPushButton,
    QFileDialog,
    QWidget
)

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication, QRubberBand
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QRect
import time
import pyscreenshot as imgGrab

xCord = [] 
yCord = []
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
            print("cords:", rect.x(), rect.y(), rect.width())
            xCord.insert(0, rect.x())
            xCord.insert(1, rect.width() + rect.x())
            yCord.insert(0, rect.y())
            yCord.insert(1, rect.height() + rect.y())
            self.close()



#Main class for screen region selector
class ScreenRegionSelector(QMainWindow):
    
    def __init__(self,):
        super().__init__(None)

        self.m_width = 400
        self.m_height = 500

        self.setMinimumSize(self.m_width, self.m_height)

        frame = QFrame()
        frame.setContentsMargins(0, 0, 0, 0)
        lay = QVBoxLayout(frame)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(5, 5, 5, 5)

        self.label = QLabel()
        self.btn_capture = QPushButton("Capture")
        self.btn_capture.clicked.connect(self.capture)
        
        self.btn_save = QPushButton("Save")
        self.btn_save.clicked.connect(self.save)
        self.btn_save.setVisible(False)

        lay.addWidget(self.label)
        lay.addWidget(self.btn_capture)
        lay.addWidget(self.btn_save)

        self.setCentralWidget(frame)

    def capture(self):
        self.capturer = Capture(self) #grabs the mouse movement from capture class
        self.capturer.show()
        self.btn_save.setVisible(True)


    def save(self):
        print("Saved")
        self.close()
        #file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "temp", "Image files (*.jpg *.bmp)")
        #if file_name:
        #    self.capturer.imgmap.save(file_name)



class Capturing():
    def getCords(run):
        app = QApplication(sys.argv)
        selector = ScreenRegionSelector()
        selector.show()
        app.exit(app.exec_())    
        print("->x",xCord)
        print("->y",yCord)
    def screenshot(run):
        im = imgGrab.grab(bbox=(xCord[0], yCord[0], xCord[1], yCord[1]))
        im.save('temp.jpg')
        print("something")
