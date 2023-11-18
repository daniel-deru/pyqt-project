import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLCDNumber
from PyQt5.QtCore import QTime, QTimer
from random import randint


class WindowExample(QDialog):
    def __init__(self):
        super(WindowExample, self).__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 rando, number")

        vbox = QVBoxLayout()

        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet("background-color: yellow;")
        vbox.addWidget(self.lcd)

        button = QPushButton("create random number")
        button.setStyleSheet("background-color: green")
        button.setFont(QFont("sanserif", 15))
        button.clicked.connect(self.random_gen)
        vbox.addWidget(button)

        self.setLayout(vbox)

    def random_gen(self):
        random = randint(1, 300)
        self.lcd.display(random)
        
    

def show_window():
    app = QApplication(sys.argv)
    window = WindowExample()
    window.show()
    sys.exit(app.exec_())
  
show_window()
