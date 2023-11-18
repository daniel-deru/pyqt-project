import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("pyqt5 tutorial 3")

        self.create_buttons()

    def create_buttons(self):
        btn1 = QPushButton("button 1", self)
        btn1.clicked.connect(self.btn_clicked)
    
    def btn_clicked(self):
        print("button 1 clicked")



def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()