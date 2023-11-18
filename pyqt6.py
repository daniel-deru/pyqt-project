import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QHBoxLayout, QSpinBox, QLabel, QLineEdit
from PyQt5.QtGui import QIcon

class WindowExample(QWidget):
    def __init__(self):
        super(WindowExample, self).__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PyQt5 spinbox")

        self.create_spinbox()

    # I added this code 
    def create_spinbox(self):
        hbox = QHBoxLayout()

        label = QLabel("laptop price: ")

        self.lineEdit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.totalResult = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineEdit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.totalResult)
        


        self.setLayout(hbox)

    def spin_selected(self):
        if self.lineEdit.text() is not 0:
            price = int(self.lineEdit.text())
            totalPrice = self.spinbox.value() * price

            self.totalResult.setText(str(totalPrice))
        else: print("wrong volume")

def show_window():
    app = QApplication(sys.argv)
    window = WindowExample()
    window.show()
    sys.exit(app.exec_())
  
show_window()
