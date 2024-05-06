# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main(object):
    def setupUi(self, mainfront):
        mainfront.setObjectName("mainfront")
        mainfront.resize(1280, 720)
        mainfront.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.jarvis = QtWidgets.QLabel(mainfront)
        self.jarvis.setGeometry(QtCore.QRect(960, -70, 331, 781))
        self.jarvis.setText("")
        self.jarvis.setPixmap(QtGui.QPixmap("H:/study/vad/UI/jav.jpg"))
        self.jarvis.setScaledContents(True)
        self.jarvis.setObjectName("jarvis")
        self.logo = QtWidgets.QLabel(mainfront)
        self.logo.setGeometry(QtCore.QRect(300, -10, 791, 131))
        self.logo.setStyleSheet("background-color: transparent;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("H:/study/vad/UI/pragya.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.code = QtWidgets.QLabel(mainfront)
        self.code.setGeometry(QtCore.QRect(10, 0, 291, 151))
        self.code.setText("")
        self.code.setPixmap(QtGui.QPixmap("H:/study/vad/UI/code.gif"))
        self.code.setScaledContents(True)
        self.code.setObjectName("code")
        self.exit = QtWidgets.QPushButton(mainfront)
        self.exit.setGeometry(QtCore.QRect(1140, 640, 130, 71))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.exit.setStyleSheet("border-image: url(H:/study/vad/UI/exits.png);")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.loading = QtWidgets.QLabel(mainfront)
        self.loading.setGeometry(QtCore.QRect(40, 170, 311, 291))
        self.loading.setText("")
        self.loading.setPixmap(QtGui.QPixmap("H:/study/vad/UI/loadd.gif"))
        self.loading.setScaledContents(True)
        self.loading.setObjectName("loading")
        self.frame = QtWidgets.QFrame(mainfront)
        self.frame.setGeometry(QtCore.QRect(10, 480, 1101, 231))
        self.frame.setStyleSheet("background-color: transparent;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.terminaloutput = QtWidgets.QPlainTextEdit(self.frame)
        self.terminaloutput.setGeometry(QtCore.QRect(0, 0, 1101, 200))
        self.terminaloutput.setStyleSheet("background-color: transparent; color: white; border: 1px solid white;")
        self.terminaloutput.setOverwriteMode(False)
        self.terminaloutput.setBackgroundVisible(False)
        self.terminaloutput.setCenterOnScroll(True)
        self.terminaloutput.setStyleSheet("color: white;")
        self.terminaloutput.setObjectName("terminaloutput")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 200, 1101, 31))
        self.lineEdit.setStyleSheet("background-color: transparent; color: white; border: 1px solid white;")
        self.lineEdit.setText("")
        self.lineEdit.setStyleSheet("background-color: transparent; color: white; border: ;")
        self.lineEdit.setObjectName("lineEdit")
        self.Enter = QtWidgets.QPushButton(self.frame)
        self.Enter.setGeometry(QtCore.QRect(1030, 200, 71, 31))
        self.Enter.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Enter.setAutoFillBackground(False)
        self.Enter.setStyleSheet("border-image: url(H:/study/vad/UI/ok.png);")
        self.Enter.setText("")
        self.Enter.setObjectName("Enter")
        self.load = QtWidgets.QLabel(mainfront)
        self.load.setGeometry(QtCore.QRect(40, 170, 311, 291))
        self.load.setText("")
        self.load.setPixmap(QtGui.QPixmap("H:/study/vad/UI/load.gif"))
        self.load.setScaledContents(True)
        self.load.setObjectName("load")
        self.listening = QtWidgets.QLabel(mainfront)
        self.listening.setGeometry(QtCore.QRect(40, 170, 311, 291))
        self.listening.setText("")
        self.listening.setPixmap(QtGui.QPixmap("H:/study/vad/UI/listening.gif"))
        self.listening.setScaledContents(True)
        self.listening.setObjectName("listening")
        self.venus = QtWidgets.QLabel(mainfront)
        self.venus.setGeometry(QtCore.QRect(40, 170, 311, 291))
        self.venus.setText("")
        self.venus.setPixmap(QtGui.QPixmap("H:/study/vad/UI/venus.gif"))
        self.venus.setScaledContents(True)
        self.venus.setObjectName("venus")
        self.sleep = QtWidgets.QLabel(mainfront)
        self.sleep.setGeometry(QtCore.QRect(40, 170, 311, 291))
        self.sleep.setText("")
        self.sleep.setPixmap(QtGui.QPixmap("H:/study/vad/UI/sleeping.gif"))
        self.sleep.setScaledContents(True)
        self.sleep.setObjectName("sleep")
        self.arc = QtWidgets.QLabel(mainfront)
        self.arc.setGeometry(QtCore.QRect(450, 90, 481, 381))
        self.arc.setText("")
        self.arc.setPixmap(QtGui.QPixmap("H:/study/vad/UI/circle.gif"))
        self.arc.setScaledContents(True)
        self.arc.setObjectName("arc")

        self.retranslateUi(mainfront)
        QtCore.QMetaObject.connectSlotsByName(mainfront)

    def retranslateUi(self, mainfront):
        _translate = QtCore.QCoreApplication.translate
        mainfront.setWindowTitle(_translate("mainfront", "mainfront"))
        self.terminaloutput.setPlainText(_translate("mainfront", "\n""\n"""))
        self.terminaloutput.setPlaceholderText(_translate("mainfront", "Terminal Goes Here"))
        self.lineEdit.setPlaceholderText(_translate("mainfront", "Enter Your Commond"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainfront = QtWidgets.QWidget()
    ui = Ui_main()
    ui.setupUi(mainfront)
    mainfront.show()
    sys.exit(app.exec_())