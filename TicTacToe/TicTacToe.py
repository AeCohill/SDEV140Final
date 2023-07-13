from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load UI File
        uic.loadUi('TicTacToe.ui',self)


        #counter to keep track of turns
        self.counter = 0

        
        #define widgets
        self.button1 = self.findChild(QPushButton, 'pushButton_1')
        self.button2 = self.findChild(QPushButton, 'pushButton_2')
        self.button3 = self.findChild(QPushButton, 'pushButton_3')
        self.button4 = self.findChild(QPushButton, 'pushButton_4')
        self.button5 = self.findChild(QPushButton, 'pushButton_5')
        self.button6 = self.findChild(QPushButton, 'pushButton_6')
        self.button7 = self.findChild(QPushButton, 'pushButton_7')
        self.button8 = self.findChild(QPushButton, 'pushButton_8')
        self.button9 = self.findChild(QPushButton, 'pushButton_9')
        self.button10 = self.findChild(QPushButton, 'pushButton_10')
        self.label = self.findChild(QLabel,'label')


        #Click The Button
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)

        #Show the app
        self.show()
        
    def clicker(self,b):
        #if to change turns
        if self.counter % 2 == 0:
            mark = 'X'
            self.label.setText("O's Turn")
        else:
            mark = 'O'
            self.label.setText("X's Turn")
        b.setText(mark)
        b.setEnabled(False)

        #change from X to O
        self.counter += 1
        
        #CHECK WIN!!

        if self.checkWin(mark):
            self.label.setText("WINNER!!")
    def checkWin(self,mark):
        #Horizontal test
        if self.button1.text() == self.button2.text() == self.button3.text()== mark:
            return True
        if self.button4.text() == self.button5.text() == self.button6.text()== mark:
            return True
        if self.button7.text() == self.button8.text() == self.button9.text()== mark:
            return True
        #Vertical Test
        
        if self.button1.text() == self.button4.text() == self.button7.text()== mark:
            return True
        if self.button2.text() == self.button5.text() == self.button8.text()== mark:
            return True
        if self.button3.text() == self.button6.text() == self.button9.text()== mark:
            return True
        #Diagonal Test
        
        if self.button1.text() == self.button5.text() == self.button9.text()== mark:
            return True
        if self.button3.text() == self.button5.text() == self.button7.text()== mark:
            return True

        return False

    def reset(self):
        buttonList = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9]

        for b in buttonList:
            b.setText("")
            b.setEnabled(True)
        
        self.label.setText("X Goes First")
        self.counter = 0


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
