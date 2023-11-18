import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QComboBox, QLabel
from PyQt5 import uic


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 1000, 700)
        self.setWindowTitle("QGridLayout")
        uic.loadUi("combobox.ui", self)

        self.combo = self.findChild(QComboBox,"comboBox")
        self.combo.currentTextChanged.connect(self.text_changed)

        self.label = self.findChild(QLabel, "label")

    def text_changed(self):
        item = self.combo.currentText()
        self.label.setText(f"you selected: {item}")
    

def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()