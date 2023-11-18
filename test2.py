from PyQt5.QtWidgets import QApplication, QWidget
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 900, 600)


def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()

