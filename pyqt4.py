from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from PyQt5 import uic
import sys

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("pyqtlesson4.ui", self)

        button = self.findChild(QPushButton, "button1")
        button.clicked.connect(self.btn_clicked)


    def btn_clicked(self):
        print("button clicked")


def show_window():
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())

show_window()