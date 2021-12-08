from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Tables(object):
    def setupUi(self, Dialog_Tables):
        Dialog_Tables.setObjectName("Dialog_Tables")
        Dialog_Tables.resize(300, 430)
        Dialog_Tables.setStyleSheet("background-color: rgb(89, 101, 214);")
        self.label_2 = QtWidgets.QLabel(Dialog_Tables)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 271, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(3)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog_Tables)
        self.pushButton.setGeometry(QtCore.QRect(100, 60, 100, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog_Tables)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 90, 100, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog_Tables)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 120, 100, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog_Tables)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 360, 75, 23))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_4.setCheckable(False)
        self.pushButton_4.setChecked(False)
        self.pushButton_4.setAutoRepeat(False)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(Dialog_Tables)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 191, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog_Tables)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Tables)

    def retranslateUi(self, Dialog_Tables):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Tables.setWindowTitle(_translate("Dialog_Tables", "Tables"))
        self.label_2.setText(_translate("Dialog_Tables", "                   Tables"))
        self.pushButton.setText(_translate("Dialog_Tables", "Заявки на продаж"))
        self.pushButton_4.setText(_translate("Dialog_Tables", "Вихід"))
        self.label_4.setText(_translate("Dialog_Tables", "Автор:Краснящих Андрій ФІТ (1-7)"))