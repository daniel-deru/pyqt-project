from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
import mysql.connector as mc


class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 256)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dbname = QtWidgets.QLineEdit(Form)
        self.dbname.setObjectName("dbname")
        self.horizontalLayout.addWidget(self.dbname)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_db = QtWidgets.QPushButton(Form)
        self.create_db.setObjectName("create_db")


        self.create_db.clicked.connect(self.create_database)


        self.horizontalLayout_2.addWidget(self.create_db)
        self.db_connect = QtWidgets.QPushButton(Form)
        self.db_connect.setObjectName("db_connect")

        self.db_connect.clicked.connect(self.db_connection)

        self.horizontalLayout_2.addWidget(self.db_connect)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database name"))
        self.create_db.setText(_translate("Form", "create database"))
        self.db_connect.setText(_translate("Form", "database connection"))

    def create_database(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "daniel",
                passwd = "Jacobus#3"
            )
            cursor = mydb.cursor()
            dbname = self.dbname.text()
            
            cursor.execute(f"CREATE DATABASE {dbname}")
            self.label_2.setText(f"Database {dbname} created")
        except mc.Error as e:
            self.label_2.setText("Database creation failed")
            print(e)

    def db_connection(self):
        try: 
            mydb = mc.connect(
                host = "localhost",
                user = "daniel",
                passwd = "Jacobus#3",
                database = "pythondatabase"
            )

            self.label_2.setText("there is a connection")
        
        except mc.Error as e:
            self.label_2.setText("error in connection")
            print(e)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
