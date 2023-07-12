from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        #load UI File
        uic.loadUi('TicTacToe.ui',self)

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
        self.button10.clicked.connect(lambda: self.clicker(self.button10))

        #Show the app
        self.show()
        
    def clicker(self,b):
        b.setText("X")
        b.setEnabled(False)

        


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
