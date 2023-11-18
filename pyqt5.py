import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("PyQt5 lesson 5")

        vbox = QVBoxLayout()

        btn1 = QPushButton("button 1")
        btn2 = QPushButton("button 2")
        btn3 = QPushButton("button 3")
        btn4 = QPushButton("button 4")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)




def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()
