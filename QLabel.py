from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(846, 384)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name = QtWidgets.QLabel(Form)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.input = QtWidgets.QLineEdit(Form)
        self.input.setBaseSize(QtCore.QSize(10, 5))
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text = QtWidgets.QLabel(Form)
        self.text.setObjectName("text")
        self.text.setFont(QFont("sanserif", 15))
        self.text.setStyleSheet("background-color: yellow")
        self.horizontalLayout_2.addWidget(self.text)
        self.change_button = QtWidgets.QPushButton(Form)
        self.change_button.setMinimumSize(QtCore.QSize(8, 4))
        self.change_button.setObjectName("change_button")
        self.horizontalLayout_2.addWidget(self.change_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.change_button.clicked.connect(self.btn_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Qlabel & QlineEdit"))
        self.name.setText(_translate("Form", "name"))
        self.text.setText(_translate("Form", "enter name"))
        self.change_button.setText(_translate("Form", "change"))

    def btn_clicked(self):
        name = self.input.text()
        self.text.setText(name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
