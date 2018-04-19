import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5 import *


import backend

qtCreatorFile = "main.ui" # Enter file here.

pipe = open("/tmp/un_pipe", "r")

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

running = False

# def send():
#     while True: # Thread will run infinitely in the background
#         if running:
#             print("send")


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.continue_button.clicked.connect(self.nextPage)
        self.continue_button_2.clicked.connect(self.nextPage)
        self.BackButton.clicked.connect(self.prevPage)
        self.BackButton_2.clicked.connect(self.prevPage)
        self.BackButton_3.clicked.connect(self.prevPage)
        self.BackButton_7.clicked.connect(self.prevPage)
        self.coachButton.clicked.connect(self.coachPage)
        self.userButton.clicked.connect(self.userPage)
        super(type(self.recordButton), self.recordButton).setAutoRepeat(True)
        # hold down button
        super(type(self.recordButton), self.recordButton).setAutoRepeatInterval(10) 
        # speed of the hold down function
        self.recordButton.pressed.connect(self.kill)
        self.recordButton.released.connect(self.me)

    def kill(self):
        backend.get_training_data()
    def me(self):
        backend.stop()
    def nextPage(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
    def prevPage(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)
    def coachPage(self):
        self.stackedWidget.setCurrentIndex(3)
    def userPage(self):
        self.stackedWidget.setCurrentIndex(4)
    def returningUserClicked(self):
        self.stackedWidget.setCurrentIndex(2)
    def newUserClicked(self):
        self.stackedWidget.setCurrentIndex(1)
 
if __name__ == "__main__":
    # Create and start the new thread
    
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setFixedSize(1031, 720)
    window.show()
    sys.exit(app.exec_())


