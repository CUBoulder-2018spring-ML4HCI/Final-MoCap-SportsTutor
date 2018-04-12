import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5 import *

qtCreatorFile = "main.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_button.clicked.connect(self.startClicked)
        self.continue_button.clicked.connect(self.continueClicked)
        self.restart_button.clicked.connect(self.returnClicked)
        
    def startClicked(self):
        self.stackedWidget.setCurrentIndex(1)
    def continueClicked(self):
        self.stackedWidget.setCurrentIndex(2)
    def returnClicked(self):
        self.stackedWidget.setCurrentIndex(0)
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())