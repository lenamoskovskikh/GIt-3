import sys
import random
from PyQt5 import uic
import sqlite3
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGraphicsColorizeEffect
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot, QPropertyAnimation, Qt
from PyQt5 import QtCore, QtWidgets



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('window1.ui', self)
        global profile
        profile = []
        self.setFixedSize(1920, 1100)
        self.pushButton.setStyleSheet("font: 48pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 100, 200);")
        self.pushButton_2.setStyleSheet("font: 12pt \"Times New Roman\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(100, 100, 150, 170);")
        self.pushButton_3.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_4.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_5.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.label_2.setFont(QFont("Academy", 17))
        self.label.setFont(QFont("Times New Roman", 40))
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.info)
        self.pushButton_3.clicked.connect(self.literature)
        self.pushButton_4.clicked.connect(self.regist)
        self.pushButton_5.clicked.connect(self.go_in)


    def go_in(self):
        self.go = GoWindow()
        stylesheet_go = """            GoWindow {                background-image: url("regist.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.go.setStyleSheet(stylesheet_go)
        self.go.show()



    def info(self):
        self.info = InfoWindow()
        stylesheet = """            InfoWindow {                background-image: url("info.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.info.setStyleSheet(stylesheet)
        self.info.show()


    def start(self):
        if not profile:
            self.label_2.setText('перед началом стоит зарегистрироваться или войти в систему')
        else:
            self.mainw = TheMainWindow()
            stylesheet_m = """            TheMainWindow {                background-image: url("themain.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
            self.mainw.setStyleSheet(stylesheet_m)
            self.mainw.show()

    def literature(self):
        self.literatures = LitWindow()
        stylesheet_lit1 = """            LitWindow {                background-image: url("liter1.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.literatures.setStyleSheet(stylesheet_lit1)
        self.literatures.show()


    def regist(self):
        self.registration = RegWindow()
        stylesheet_reg = """            RegWindow {                background-image: url("regist.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.registration.setStyleSheet(stylesheet_reg)
        self.registration.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()

    stylesheet_main = """            MainWindow {                background-image: url("mainwindow1.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec_())

