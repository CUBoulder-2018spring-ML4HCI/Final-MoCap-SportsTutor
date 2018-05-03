import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5 import *


import backend

qtCreatorFile = "main.ui" # Enter file here.

# pipe = open("/tmp/un_pipe", "r")

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
        self.continue_button_3.clicked.connect(self.nextPage)
        self.BackButton.clicked.connect(self.prevPage)
        self.BackButton_2.clicked.connect(self.prevPage)
        self.BackButton_3.clicked.connect(self.prevPage)
        self.BackButton_7.clicked.connect(self.prevPage)
        self.BackButton_8.clicked.connect(self.prevPage)
        self.coachButton.clicked.connect(self.coachPage)
        self.userButton.clicked.connect(self.userPage)
        # super(type(self.recordButton), self.recordButton).setAutoRepeat(True)
        # # hold down button
        # super(type(self.recordButton), self.recordButton).setAutoRepeatInterval(10)
        # speed of the hold down function

        # super(type(self.runUser), self.runUser).setAutoRepeat(True)
        # # hold down button
        # super(type(self.runUser), self.runUser).setAutoRepeatInterval(10)



        self.recordButton.pressed.connect(self.record)
        #self.recordButton.released.connect(self.stop_train)
        self.stopRecording.pressed.connect(self.stop_train)
        self.runUser.pressed.connect(self.run_user)
        self.stopUser.pressed.connect(self.stop_user)
        # self.runUser.released.connect(self.stop)

    #USER
    def run_user(self):
        reset_color(self.bodyShoulder)
        reset_color(self.bodyElbow)
        reset_color(self.bodyWrist)

        reset_color_circle(self.circleShoulder)
        reset_color_circle(self.circleElbow)
        reset_color_circle_wrist(self.circleWrist)


        backend.get_test_data()
    def stop_user(self):
        backend.stop_test()
        body_part = str(backend.get_largest_distance())
        if "SHOULDER" in body_part:# set this to when we want to change body shoulder
            change_color(self.bodyShoulder)
            change_color_circle(self.circleShoulder)
        if "ELBOW" in body_part:
            change_color(self.bodyElbow)
            change_color_circle(self.circleElbow)
        if "WRIST" in body_part:
            change_color(self.bodyWrist)
            change_color_circle_wrist(self.circleWrist)
        feedback_string = "Change your " + body_part
        change_text(self.feedbackText, feedback_string)


    #COACH
    def record(self):
        backend.get_train_data()
    def stop_train(self):
        backend.stop_train()
    def stop_test(self):
        backend.stop_test()
    def nextPage(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()+1)
    def prevPage(self):
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()-1)
    def coachPage(self):
        self.stackedWidget.setCurrentIndex(4)
    def userPage(self):
        self.stackedWidget.setCurrentIndex(5)
    def returningUserClicked(self):
        self.stackedWidget.setCurrentIndex(2)
    def newUserClicked(self):
        self.stackedWidget.setCurrentIndex(1)

def change_color(obj):
    obj.setStyleSheet("""
           font: 20pt "DIN 2014";
           color: orange;
           """
    )

def change_color_circle(obj):
    obj.setStyleSheet("""
           background: orange;
           border-radius: 15px;
           """
    )

def change_color_circle_wrist(obj):
    obj.setStyleSheet("""
           background: orange;
           border-radius: 13px;
           """
    )

def reset_color(obj):
    obj.setStyleSheet("""
           font: 20pt "DIN 2014";
           color: black;
           """
    )

def reset_color_circle(obj):
    obj.setStyleSheet("""
           background: white;
           border-radius: 15px;
           """
    )
def reset_color_circle_wrist(obj):
    obj.setStyleSheet("""
           background: white;
           border-radius: 13px;
           """
    )

def change_text(obj, text):
    obj.setText(text)

if __name__ == "__main__":
    # Create and start the new thread

    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.setFixedSize(1031, 720)
    window.show()
    sys.exit(app.exec_())
