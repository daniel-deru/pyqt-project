from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(999, 864)
        self.button1 = QtWidgets.QPushButton(Form)
        self.button1.setGeometry(QtCore.QRect(380, 70, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Montserrat Subrayada")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.btn_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button1.setText(_translate("Form", "button 1"))

    def btn_clicked(self):
        print("button clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
