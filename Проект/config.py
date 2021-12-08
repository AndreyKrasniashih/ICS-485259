from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_0(object):
    def setupUi(self, Dialog_0):
        Dialog_0.setObjectName("Dialog_0")
        Dialog_0.resize(301, 100)
        Dialog_0.setStyleSheet("background-color: rgb(89, 101, 214);")
        self.label = QtWidgets.QLabel(Dialog_0)
        self.label.setGeometry(QtCore.QRect(10, 20, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(3)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog_0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_0)

