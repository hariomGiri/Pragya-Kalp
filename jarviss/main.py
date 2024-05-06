import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from mainGuifile import Ui_mainGuifile
from jarvisMainfile import jarvisMain
from loginn import login

class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main File")
        self.ui = Ui_mainGuifile()  # Instantiate the Ui_mainGuifile class
        self.ui.setupUi(self)  # Now you can call the setupUi method
        self.ui.movie = QtGui.QMovie("H:/study/vad/UI/loading.gif")
        self.ui.loading.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.quitebutton.clicked.connect(self.close)
        self.ui.loginbutton.clicked.connect(self.connectLoginPage)
        
        
        
   

        
    def connectLoginPage(self):
        from loginn import login
        self.showloginPage = login()
        self.showloginPage.show()
        ui.close()
        from jarvisMainfile import jarvisMain
        self.jarvisMainInstance = jarvisMain()
        self.jarvisMainInstance.showJarvis()
    
        
def connectSecondWindow(self):
    from jarvisMainfile import jarvisMain
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())
        
        