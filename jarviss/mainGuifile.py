# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainGuifile(object):
    def setupUi(self, mainGuifile):
        mainGuifile.setObjectName("mainGuifile")
        mainGuifile.resize(800, 500)
        mainGuifile.setStyleSheet("background-color: rgb(0, 0, 0)")
        self.hariom = QtWidgets.QLabel(mainGuifile)
        self.hariom.setGeometry(QtCore.QRect(50, 0, 671, 101))
        self.hariom.setStyleSheet("background-color:transparent;")
        self.hariom.setText("")
        self.hariom.setPixmap(QtGui.QPixmap("H:/study/vad/UI/name.gif"))
        self.hariom.setScaledContents(True)
        self.hariom.setObjectName("hariom")
        self.frame = QtWidgets.QLabel(mainGuifile)
        self.frame.setGeometry(QtCore.QRect(130, 100, 531, 291))
        self.frame.setText("")
        self.frame.setPixmap(QtGui.QPixmap("H:/study/vad/UI/frame10.jpg"))
        self.frame.setScaledContents(True)
        self.frame.setObjectName("frame")
        self.loading = QtWidgets.QLabel(mainGuifile)
        self.loading.setGeometry(QtCore.QRect(160, 130, 471, 231))
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("H:/study/vad/UI/loading.gif"))
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")
        self.startlabel = QtWidgets.QLabel(mainGuifile)
        self.startlabel.setGeometry(QtCore.QRect(10, 392, 181, 101))
        self.startlabel.setText("")
        self.startlabel.setPixmap(QtGui.QPixmap("H:/study/vad/UI/start.gif.gif"))
        self.startlabel.setScaledContents(True)
        self.startlabel.setObjectName("startlabel")
        self.loginlabel = QtWidgets.QLabel(mainGuifile)
        self.loginlabel.setGeometry(QtCore.QRect(290, 400, 181, 101))
        self.loginlabel.setText("")
        self.loginlabel.setPixmap(QtGui.QPixmap("H:/study/vad/UI/login.png"))
        self.loginlabel.setScaledContents(True)
        self.loginlabel.setObjectName("loginlabel")
        self.quitelaber = QtWidgets.QLabel(mainGuifile)
        self.quitelaber.setGeometry(QtCore.QRect(610, 400, 181, 101))
        self.quitelaber.setText("")
        self.quitelaber.setPixmap(QtGui.QPixmap("H:/study/vad/UI/exit.png"))
        self.quitelaber.setScaledContents(True)
        self.quitelaber.setObjectName("quitelaber")
        self.startbutton = QtWidgets.QPushButton(mainGuifile)
        self.startbutton.setGeometry(QtCore.QRect(14, 402, 181, 81))
        self.startbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startbutton.setStyleSheet("background-color:transparent;")
        self.startbutton.setText("")
        self.startbutton.setObjectName("startbutton")
        self.loginbutton = QtWidgets.QPushButton(mainGuifile)
        self.loginbutton.setGeometry(QtCore.QRect(290, 410, 181, 81))
        self.loginbutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginbutton.setStyleSheet("background-color:transparent;")
        self.loginbutton.setText("")
        self.loginbutton.setObjectName("loginbutton")
        self.quitebutton = QtWidgets.QPushButton(mainGuifile)
        self.quitebutton.setGeometry(QtCore.QRect(610, 400, 181, 81))
        self.quitebutton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quitebutton.setStyleSheet("background-color:transparent;")
        self.quitebutton.setText("")
        self.quitebutton.setObjectName("quitebutton")

        self.retranslateUi(mainGuifile)
        QtCore.QMetaObject.connectSlotsByName(mainGuifile)

    def retranslateUi(self, mainGuifile):
        _translate = QtCore.QCoreApplication.translate
        mainGuifile.setWindowTitle(_translate("mainGuifile", "mainGuifile"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainGuifile = QtWidgets.QWidget()
    ui = Ui_mainGuifile()
    ui.setupUi(mainGuifile)
    mainGuifile.show()
    sys.exit(app.exec_())
