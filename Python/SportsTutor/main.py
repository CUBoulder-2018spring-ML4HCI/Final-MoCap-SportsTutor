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
        # self.returning_button.clicked.connect(self.returningUserClicked)
        # self.new_button.clicked.connect(self.newUserClicked)
        # self.actionNew_Recording.triggered.connect(self.newRecordingClicked)
        self.continue_button.clicked.connect(self.nextPage)
        self.BackButton.clicked.connect(self.prevPage)
        self.BackButton_2.clicked.connect(self.prevPage)
        self.BackButton_3.clicked.connect(self.prevPage)

    def nextPage(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
    def prevPage(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)
    def newRecordingClicked(self):
        return 1
    def returningUserClicked(self):
        self.stackedWidget.setCurrentIndex(2)
    def newUserClicked(self):
        self.stackedWidget.setCurrentIndex(1)
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())