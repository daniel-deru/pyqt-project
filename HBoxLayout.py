import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 1000, 800)
        self.setWindowTitle("HBoxLayout")

        hbox = QHBoxLayout()

        btn1 = QPushButton("button 1")
        btn2 = QPushButton("button 2")
        btn3 = QPushButton("button 3")
        btn4 = QPushButton("button 4")

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        self.setLayout(hbox)

def show_window():
    app = QApplication(sys.argv)
    window =Window()
    window.show()
    sys.exit(app.exec_())

show_window()