from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import mysql.connector as mc

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(937, 594)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.email_input = QtWidgets.QLineEdit(Form)
        self.email_input.setObjectName("email_input")
        self.horizontalLayout.addWidget(self.email_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.horizontalLayout_2.addWidget(self.password_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.insert_data)

        self.verticalLayout.addWidget(self.pushButton)
        self.result = QtWidgets.QLabel(Form)
        self.result.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.result.setObjectName("result")
        self.verticalLayout.addWidget(self.result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "email"))
        self.label_2.setText(_translate("Form", "password"))
        self.pushButton.setText(_translate("Form", "insert data"))
        self.result.setText(_translate("Form", "TextLabel"))

    def insert_data(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "daniel",
                passwd = "Jacobus#3",
                database = "pythondatabase"
            )

            mycursor = mydb.cursor()

            email = self.email_input.text()
            password = self.password_input.text()

            query = "INSERT INTO users (email, name) VALUES (%s, %s)"
            value = (email, password)

            mycursor.execute(query, value)

            mydb.commit()
            self.result.setText("data inserted")

        except mc.Error as e:
            print(e)
            self.result.setText("Error inserting data")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
