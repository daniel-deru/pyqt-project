import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
    
        self.setGeometry(400, 400, 900, 600)
        self.setWindowTitle("PyQt5 tutorial 2")
        self.setWindowIcon(QIcon("react.jpg"))
        
        self.buttons()
        
    def buttons(self):
        btn1 = QPushButton("button 1", self)
        btn1.setGeometry(200, 200, 150, 50)
        btn1.setStyleSheet("background-color: green")

        btn2 = QPushButton("button 2", self)
        btn2.setGeometry(400, 400, 150, 100)
        btn2.setIcon(QIcon("react.jpg"))
       
    
def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()