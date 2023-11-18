from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(733, 685)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.item = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.item.setFont(font)
        self.item.setObjectName("item")
        self.verticalLayout_3.addWidget(self.item)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.extra = QtWidgets.QLabel(Dialog)
        self.extra.setObjectName("extra")
        self.horizontalLayout_3.addWidget(self.extra)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setObjectName("checkBox")

        # I added this code
        self.checkBox.stateChanged.connect(self.checked_item)


        self.verticalLayout_6.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setObjectName("checkBox_2")

         # I added this code
        self.checkBox_2.stateChanged.connect(self.checked_item)


        self.verticalLayout_6.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setObjectName("checkBox_3")

         # I added this code
        self.checkBox_3.stateChanged.connect(self.checked_item)


        self.verticalLayout_6.addWidget(self.checkBox_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setText("")
        self.result.setObjectName("result")
        self.verticalLayout_3.addWidget(self.result)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PyQt5 QCheckbox"))
        self.item.setText(_translate("Dialog", "regular tuna price: 20"))
        self.extra.setText(_translate("Dialog", "select extra"))
        self.checkBox.setText(_translate("Dialog", "sausage: 3"))
        self.checkBox_2.setText(_translate("Dialog", "pizza: 3"))
        self.checkBox_3.setText(_translate("Dialog", "salad: 4"))


    # I added this code
    def checked_item(self):
        price = 20
        
        if self.checkBox.isChecked():
            price += 3
        
        if self.checkBox_2.isChecked():
            price += 4
        
        if self.checkBox_3.isChecked():
            price += 5
  

        self.result.setText(f"Total price is: {price}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
