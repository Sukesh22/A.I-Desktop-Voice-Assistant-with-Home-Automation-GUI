import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from Login import Ui_Frame

class mainFile(QFrame):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Setting up GUI")
        self.firstUI = Ui_Frame()
        self.firstUI.setupUi(self)
        
        self.firstUI.movie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\Jarvis_Gui (2).gif")
        self.firstUI.maingif.setMovie(self.firstUI.movie)
        self.firstUI.movie.start()
        
        self.firstUI.exit.clicked.connect(self.close)
        self.firstUI.start.clicked.connect(self.connectToLoginWindow)
        
    def connectToLoginWindow(self):
        from loginWindowMAIN import loginWindow
        self.showLoginWindow = loginWindow()
        ui.close()
        self.showLoginWindow.show()
        
    def connectToSecondWindow(self):
        from Jarvis import jarvisMainClass
        self.showSecondWindow = jarvisMainClass()
        ui.close()
        self.showSecondWindow.show()
             
        
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())  