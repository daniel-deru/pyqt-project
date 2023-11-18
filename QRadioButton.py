import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout, QRadioButton


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
    
        self.setGeometry(400, 400, 900, 600)
        self.setWindowTitle("PyQt5 tutorial 2")

        self.creat_radio_button()

        vbox = QVBoxLayout()

        vbox.addWidget(self.groupbox)

        self.label = QLabel("Text")
        self.label.setFont(QFont("sanserif", 15))
        vbox.addWidget(self.label)


        self.setLayout(vbox)
    
    def creat_radio_button(self):
        self.groupbox = QGroupBox("what is your favorite sport?")
        self.groupbox.setFont(QFont("sanserif", 15))

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("football")
        self.rad1.setChecked(True)
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("karate")
        self.rad2.setChecked(False)
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("tennis")
        self.rad3.setChecked(False)
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.groupbox.setLayout(hbox)
    
    def on_selected(self):
        radio_button = self.sender()
        print(radio_button)

        if radio_button.isSignalConnected:
            self.label.setText(f"you have selected: {radio_button.text()}")
        
   
    
def show_window():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

show_window()