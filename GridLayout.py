import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 400, 1000, 700)
        self.setWindowTitle("QGridLayout")

        grid = QGridLayout()

        btn1 = QPushButton("button 1")
        btn2 = QPushButton("button 2")
        btn3 = QPushButton("button 3")
        btn4 = QPushButton("button 4")
        btn5 = QPushButton("button 5")
        btn6 = QPushButton("button 6")
        btn7 = QPushButton("button 7")
        btn8 = QPushButton("button 8")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 1, 0)
        grid.addWidget(btn5, 1, 1)
        grid.addWidget(btn6, 1, 2)
        grid.addWidget(btn7, 2, 0)
        grid.addWidget(btn8, 2, 2)

        self.setLayout(grid)

def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()