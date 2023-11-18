import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import QTime, QTimer
from random import randint


class WindowExample(QDialog):
    def __init__(self):
        super(WindowExample, self).__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 rando, number")

        self.create_msgbox()

    def create_msgbox(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        btn1 = QPushButton("warning")
        btn2 = QPushButton("information")
        btn3 = QPushButton("about")
        btn4 = QPushButton("yes/no")

        btn1.clicked.connect(self.warning_msg)
        btn2.clicked.connect(self.info_msg)
        btn3.clicked.connect(self.about_msg)
        btn4.clicked.connect(self.yes_no)

        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)

        self.label = QLabel("text")
        self.label.setFont(QFont("sanserif", 15))

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def warning_msg(self):
        QMessageBox.warning(self, "Warning", "this is a warning")
        
    def info_msg(self):
        QMessageBox.information(self, "Information", "this is information") 
        
    def about_msg(self):
        QMessageBox.about(self, "About", "this is about")
        
    def yes_no(self):
        message = QMessageBox.question(self, "Choice Message", "Do you like python?", QMessageBox.Yes | QMessageBox.No)
        
        if message == QMessageBox.Yes: self.label.setText("Yes I like Python.")
        else: self.label.setText("No I don't like Python.")
    

def show_window():
    app = QApplication(sys.argv)
    window = WindowExample()
    window.show()
    sys.exit(app.exec_())
  
show_window()
