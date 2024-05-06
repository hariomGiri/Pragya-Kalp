import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from login import Ui_Dialog 

class login(QWidget):
    def __init__(self):
        super(login, self).__init__()
        self.loginUi = Ui_Dialog()
        self.loginUi.setupUi(self)
        self.loginUi.chitingmovie = QtGui.QMovie(u"H:\\study\\vad\\UI\\cheatin.gif")
        self.loginUi.chiting.setMovie(self.loginUi.chitingmovie)
        self.loginUi.retrybutton.clicked.connect(self.retryButton)      
        
        self.loginUi.loginbutton.clicked.connect(self.ValidateLogin)
        self.loginUi.chiting.hide()
        
    def ValidateLogin(self):
        username = self.loginUi.username.text()
        password = self.loginUi.password.text()
        if username == "admin" and password == "admin":
            print("login successful")
        else:
            self.startMovie()
            
            
    def retryButton(self):
        self.loginUi.username.clear()
        self.loginUi.password.clear()
        self.stopMovie()
    def startMovie(self):
        self.loginUi.chiting.show()
        self.loginUi.chitingmovie.start()
    def stopMovie(self):
        self.loginUi.chitingmovie.stop()
        self.loginUi.chiting.hide()          
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = login()
    ui.show()
    sys.exit(app.exec_())
    
    
    
    