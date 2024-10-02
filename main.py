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
from screenreader import Capture
from PyQt5.QtCore import Qt

#main class for screen region selector
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
        self.capturer = Capture(self)
        self.capturer.show()
        self.btn_save.setVisible(True)

    def save(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Image files (*.png *.jpg *.bmp)")
        if file_name:
            self.capturer.imgmap.save(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
    Qframe {
            background-color: rgb(0,0,0);
        }
    QPushButton {
        border-radius: 5px;
        background-color: rgb(60,90,255)  
        padding: 10px;
        color: white;
        font-weight: bold;
        font-family: Arial;
        font-size: 12px;  
    }

    QPushButton::hover{
        background-color: rgb(60,20,255)              
    }""")

    selector = ScreenRegionSelector()
    selector.show()
    app.exit(app.exec_())
    
    