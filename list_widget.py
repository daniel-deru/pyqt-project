from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class Ui_Form(QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 809)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setStyleSheet("QListWidget {\n"
"    color: red;\n"
"    \n"
"    font: 75 14pt \"MS Shell Dlg 2\";\n"
"    background-color: black;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        # I added this line of code below
        self.listWidget.clicked.connect(self.item_clicked)

        self.verticalLayout.addWidget(self.listWidget)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: green;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Python"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Java"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "C++"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "C#"))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "JavaScript"))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "Kotlin"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def item_clicked(self):
        item = self.listWidget.currentItem()
        self.label.setText(f"you have selected: {str(item.text())}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
