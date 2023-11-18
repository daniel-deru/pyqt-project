import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class WindowExample(QWidget):
    def __init__(self):
        super(WindowExample, self).__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("window title")
        self.setWindowIcon(QIcon("react.jpg"))
        self.setFixedHeight(500)
        self.setFixedWidth(700)
        self.setWindowOpacity(0.8)
        self.setStyleSheet("background-color: blue;")
        self.show()

def show_window():
    app = QApplication(sys.argv)
    window = WindowExample()
    sys.exit(app.exec_())
  
show_window()

