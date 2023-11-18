from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog
import mysql.connector as mc

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 314)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.email_input = QtWidgets.QLineEdit(Form)
        self.email_input.setObjectName("email_input")
        self.horizontalLayout.addWidget(self.email_input)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.name_input = QtWidgets.QLineEdit(Form)
        self.name_input.setObjectName("name_input")
        self.horizontalLayout_2.addWidget(self.name_input)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.login)

        self.verticalLayout.addWidget(self.pushButton)
        self.result = QtWidgets.QLabel(Form)
        self.result.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "email"))
        self.label_2.setText(_translate("Form", "name"))
        self.pushButton.setText(_translate("Form", "login"))

    def login(self):
        try:
            email_input = self.email_input.text()
            name_input = self.name_input.text()

            mydb = mc.connect(
                host = "localhost",
                user = "daniel",
                passwd = "Jacobus#3",
                database = "pythondatabase"
            )

            mycursor = mydb.cursor()
            query = f"SELECT email, name from users where email like '{email_input}' and name like '{name_input}'"
            mycursor.execute(query)

            result = mycursor.fetchone()

            if result is None:
                self.result.setText(f"incorrect email and name combination")
            else: 
                self.result.setText("you are loggged in")
                myDialog = QDialog()
                myDialog.setModal(True)
                myDialog.exec_()

        except mc.Error as e:
            print(e)
            self.result.setText(f"login failed query: {query}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
