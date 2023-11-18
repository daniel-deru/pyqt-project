from PyQt5.QtGui import qAlpha
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QSlider, QLabel
import sys
from PyQt5 import uic

class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("slider.ui", self)

        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.slider.valueChanged.connect(self.changed_slider)


        self.label = self.findChild(QLabel, "label")

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))



def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()