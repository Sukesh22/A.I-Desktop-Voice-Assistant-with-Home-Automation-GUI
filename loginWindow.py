# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName("GroupBox")
        GroupBox.setEnabled(True)
        GroupBox.resize(1080, 720)
        GroupBox.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.heading = QtWidgets.QLabel(GroupBox)
        self.heading.setGeometry(QtCore.QRect(10, 0, 1051, 161))
        self.heading.setText("")
        self.heading.setPixmap(QtGui.QPixmap("C:\\Users\\91914\\Project\\GUI files\\heading.jpg"))
        self.heading.setScaledContents(True)
        self.heading.setObjectName("heading")
        self.frame = QtWidgets.QFrame(GroupBox)
        self.frame.setGeometry(QtCore.QRect(80, 210, 911, 491))
        self.frame.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius:30px;\n"
"border-width:5px,5px,5px,5px;\n"
"border-style:solid;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.retry = QtWidgets.QPushButton(self.frame)
        self.retry.setGeometry(QtCore.QRect(50, 380, 211, 91))
        self.retry.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retry.setStyleSheet("border-image: url(C:/Users/91914/Project/GUI files/retry.png);")
        self.retry.setText("")
        self.retry.setObjectName("retry")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(630, 380, 211, 91))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("border-image: url(C:/Users/91914/Project/GUI files/exit.png);")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(160, 30, 551, 111))
        self.username.setStyleSheet("font: 75 italic 30pt \"Stark\";\n"
"padding-left: 180px;")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(160, 150, 551, 111))
        self.password.setStyleSheet("font: 75 italic 30pt \"Stark\";\n"
"padding-left:180px;")
        self.password.setText("")
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.frame)
        self.login.setGeometry(QtCore.QRect(330, 280, 201, 81))
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setStyleSheet("border-image: url(C:/Users/91914/Project/GUI files/retry.png);\n"
"border-image: url(C:/Users/91914/Project/GUI files/login-empty.png);")
        self.login.setText("")
        self.login.setObjectName("login")
        self.illegalentry = QtWidgets.QLabel(self.frame)
        self.illegalentry.setGeometry(QtCore.QRect(20, 20, 841, 351))
        self.illegalentry.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.illegalentry.setText("")
        self.illegalentry.setPixmap(QtGui.QPixmap("C:\\Users\\91914\\Project\\GUI files\\illegalentry.gif"))
        self.illegalentry.setScaledContents(True)
        self.illegalentry.setObjectName("illegalentry")

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        _translate = QtCore.QCoreApplication.translate
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox"))
        self.username.setPlaceholderText(_translate("GroupBox", "USERNAME"))
        self.password.setPlaceholderText(_translate("GroupBox", "PASSWORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GroupBox = QtWidgets.QGroupBox()
    ui = Ui_GroupBox()
    ui.setupUi(GroupBox)
    GroupBox.show()
    sys.exit(app.exec_())