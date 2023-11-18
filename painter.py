from PyQt5.QtGui import QPainter,QPen, QBrush
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QCalendarWidget, QLabel
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 800, 500)
        self.setWindowTitle("PyQt5 drawing")
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.green, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        painter.drawRect(100, 15, 600, 200)



def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()