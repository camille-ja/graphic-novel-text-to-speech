from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600,400,500,500) #xpos (where x starts on user's screen), ypos (where y starts on user's screen), width, height
        self.setWindowTitle("Home page")
        self.initUI()
    
    def initUI(self):
        self.label = QtWidgets.QLabel(self) #location of label
        self.label.setText("my first label B)")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me!")
        self.b1.clicked.connect(self.clicked) 
    
    def clicked(self):
        self.label.setText("you pressed the button!")
        self.update()

    def update(self): 
        self.label.adjustSize()



def window(): #finds applicaton
    app = QApplication(sys.argv) #starts application
    win = MyWindow()
    

    

    win.show()
    sys.exit(app.exec_())

window()