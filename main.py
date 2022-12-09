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


w = None
class TheMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global w
        uic.loadUi('themain.ui', self)
        self.pushButton_3.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_4.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_5.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_6.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_7.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_8.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_9.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_10.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_11.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_12.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_13.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_14.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_15.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_16.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_17.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_18.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.label_2.setFont(QFont("Academy", 17))
        self.label.setStyleSheet("font: 17pt \"Academy\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 0);")
        self.textEdit.setEnabled(False)
        self.textEdit_2.setEnabled(False)
        self.textEdit.setStyleSheet("font: 17pt \"Academy\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgba(255, 255, 255, 170);")

        self.textEdit_2.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.daytask()
        self.pushButton_21.clicked.connect(self.solve)
        self.pushButton_22.clicked.connect(self.add_solve)
        self.label_3.setFont(QFont("Academy", 17))
        self.lineEdit.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        w = self


    def daytask(self):
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        res = self.cur.execute(f"""SELECT task FROM problems""").fetchall()
        m = []
        for el in res:
            m.append(''.join(el))
        self.textEdit.setText(random.choice(m))


    def solve(self):
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        res = self.cur.execute(f"""SELECT solve FROM problems where task = '{self.textEdit.toPlainText()}'""").fetchall()[0]
        id = self.cur.execute(f"""SELECT id FROM problems where task = '{self.textEdit.toPlainText()}'""").fetchall()[0]
        for el in res:
            if el == 'нет':
                self.textEdit_2.setText('Решения еще нет, но вы можете его добавить, нажав на кнопку справа')
            else:
                self.textEdit_2.setText(el)
        res1 = ''
        for el in id:
            res1 = res1 + str(el)
        self.lineEdit.setText(f'Номер задачи: {res1}')


    def add_solve(self):
        self.add_solving = SolveWindow()
        self.add_solving.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()

    stylesheet_main = """            MainWindow {                background-image: url("mainwindow1.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec_())

