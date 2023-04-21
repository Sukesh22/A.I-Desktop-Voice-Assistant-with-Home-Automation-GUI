import sys
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from JARVISmainfile import Ui_Frame

class jarvisMainClass(QFrame):
    def __init__(self):
        super(jarvisMainClass, self).__init__()
        self.jarvisUI = Ui_Frame()
        self.jarvisUI.setupUi(self)
        
        self.jarvisUI.codingMovie = QtGui.QMovie("C:\\Users\\91914\\Project\\GUI files\\B.G_Template_1.gif")
        self.jarvisUI.codelabel.setMovie(self.jarvisUI.codingMovie)
        self.jarvisUI.codingMovie.start()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    ui = jarvisMainClass()
    ui.show()
    sys.exit(app.exec_())  