import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtCore import QTime, QTimer

class WindowExample(QDialog):
    def __init__(self):
        super(WindowExample, self).__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 QLCDNumber")

        timer = QTimer()
        timer.timeout.connect(self.lcd_number)
        timer.start(1000)

        self.lcd_number()

    def lcd_number(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet("background-color: black;"
                          "color: #40ff00;")

        vbox.addWidget(lcd)
        time = QTime.currentTime()
        text = time.toString("hh:mm")

        lcd.display(text)
        self.setLayout(vbox)
    

def show_window():
    app = QApplication(sys.argv)
    window = WindowExample()
    window.show()
    sys.exit(app.exec_())
  
show_window()
