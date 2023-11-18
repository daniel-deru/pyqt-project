import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
# from PyQt5.QtChart import QtCharts

# print(QtCharts)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 1000, 700)
        self.setWindowTitle("chart")

def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()