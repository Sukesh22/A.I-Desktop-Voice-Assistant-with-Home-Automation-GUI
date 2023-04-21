import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from loginWindow import Ui_GroupBox

class loginWindow(QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        print("Setting up GUI")
        self.loginUI = Ui_GroupBox()
        self.loginUI.setupUi(self)
        
        self.loginUI.illegalentry.hide()
        self.loginUI.password.setEchoMode(QLineEdit.Password)
        self.loginUI.login.clicked.connect(self.validateLogin)
        
      
        self.loginUI.retry.clicked.connect(self.retryButton)
        self.loginUI.exit.clicked.connect(self.close)
     
    def retryButton(self):
        self.loginUI.username.clear()
        self.loginUI.password.clear()
        
       
    def validateLogin(self):
        username = self.loginUI.username.text()
        passw = self.loginUI.password.text()    
        if username == "Sukesh" and passw == "jarvis":
            print("Login Success") 
        else:
            print("Login Fail")
                  
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)  
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_())  