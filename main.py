import sys
import random
from PyQt5 import uic
import sqlite3
import math
import csv
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
            self.label_2.setText('?????????? ?????????????? ?????????? ???????????????????????????????????? ?????? ?????????? ?? ??????????????')
        else:
            self.mainw = TheMainWindow()
            stylesheet_m = """            TheMainWindow {                background-image: url("themain.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
            self.mainw.setStyleSheet(stylesheet_m)
            self.mainw.show()
            self.close()

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
        self.label_4.setFont(QFont("Academy", 17))
        res = {}
        with open('news.csv', encoding="utf8") as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            for el in reader:
                el = el[0].split(',')
                res[el[0]] = el[1]
            data = sorted(res.keys(), key = self.sortt, reverse = True)
        items = []
        for i in range(len(data)):
            items.append((data[i], res[data[i]]))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['????????', '??????????????????????'])
        for value, item in enumerate(items):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for el, row in enumerate(item):
                self.tableWidget.setItem(value, el, QTableWidgetItem(str(row)))
        self.tableWidget.horizontalHeader().resizeSection(1, 1500)
        self.tableWidget.horizontalHeader().resizeSection(0, 150)
        self.label_5.setStyleSheet("font: 30pt \"Academy\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 0);")
        self.pushButton_2.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.tableWidget.setStyleSheet("font: 17pt \"Academy\";\n"
                                        "color: rgb(100, 100, 150);\n"
                                        "background-color: rgba(250, 250, 255, 100);")
        self.pushButton_3.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_19.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_21.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_22.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")



        self.pushButton_3.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgba(100, 100, 150, 170);")
        self.pushButton_4.setStyleSheet("font: 12pt \"Times New Roman\";\n"
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
        self.pushButton_5.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")

        self.pushButton_3.clicked.connect(self.problems)
        self.pushButton_4.clicked.connect(self.problems)
        self.pushButton_5.clicked.connect(self.problems)
        self.pushButton_6.clicked.connect(self.problems)
        self.pushButton_7.clicked.connect(self.problems)
        self.pushButton_8.clicked.connect(self.problems)
        self.pushButton_9.clicked.connect(self.problems)
        self.pushButton_10.clicked.connect(self.problems)
        self.pushButton_11.clicked.connect(self.problems)

        self.pushButton.clicked.connect(self.search)
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
        self.pushButton_19.clicked.connect(self.tasks)
        self.pushButton_2.clicked.connect(self.problem)
        self.label_3.setFont(QFont("Academy", 17))
        self.lineEdit.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        w = self

    def sortt(self, el):
        el = el.split('.')
        try:
            year = int(el[2])
        except Exception:
            year = int(el[2].replace('0', ''))
        try:
            month = int(el[1])
        except Exception:
            month = int(el[1].replace('0', ''))
        try:
            day = int(el[0])
        except Exception:
            day = int(el[0].replace('0', ''))
        return (year, month, day)


    def problems(self):
        global text
        text = self.sender().text()
        self.problemsss = ProblemssWindow()
        self.problemsss.show()


    def tasks(self):
        self.task = TWindow()
        stylesheet_s3 = """            TWindow {                background-image: url("regist.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.task.setStyleSheet(stylesheet_s3)
        self.task.show()

    def problem(self):
        self.prob = PWindow()
        stylesheet_s2 = """            PWindow {                background-image: url("snow5.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.prob.setStyleSheet(stylesheet_s2)
        self.prob.show()


    def search(self):
        self.searching = SWindow()
        stylesheet_s1 = """            SWindow {                background-image: url("snow5.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.searching.setStyleSheet(stylesheet_s1)
        self.searching.show()


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
            if el == '??????':
                self.textEdit_2.setText('?????????????? ?????? ??????, ???? ???? ???????????? ?????? ????????????????, ?????????? ???? ???????????? ????????????')
            else:
                self.textEdit_2.setText(el)
        res1 = ''
        for el in id:
            res1 = res1 + str(el)
        self.lineEdit.setText(f'?????????? ????????????: {res1}')


    def add_solve(self):
        self.add_solving = SolveWindow()
        self.add_solving.show()

class ProblemssWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = 0
        uic.loadUi('problemsss.ui', self)
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        self.r = []
        try:
            result = self.cur.execute(f"""SELECT * from problems where type = '{text}'""").fetchall()
            for el in result:
                self.r.append(el)
        except Exception:
            self.label_6.setText('???????????? ???? ??????????????')
        if not self.r:
            self.label_6.setText('???????????? ???? ??????????????')
        self.pushButton_3.setStyleSheet("font: 17pt \"Academy\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgba(255, 255, 255, 170);")
        self.pushButton.setStyleSheet("font: 17pt \"Academy\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgba(255, 255, 255, 170);")
        self.pushButton_2.setStyleSheet("font: 17pt \"Academy\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgba(255, 255, 255, 170);")
        self.lineEdit_3.setStyleSheet("font: 17pt \"Academy\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgba(255, 255, 255, 170);")
        self.lineEdit_2.setStyleSheet("font: 17pt \"Academy\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgba(255, 255, 255, 170);")
        self.lineEdit.setStyleSheet("font: 17pt \"Academy\";\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "background-color: rgba(255, 255, 255, 170);")
        self.textEdit_2.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.textEdit.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.label_6.setFont(QFont("Academy", 20))
        self.label.setFont(QFont("Academy", 20))
        self.label_3.setFont(QFont("Academy", 20))
        self.label_4.setFont(QFont("Academy", 20))
        self.label.setText(f'???????????? ???? ???????? "{text}"')
        self.label_2.setFont(QFont("Academy", 20))
        self.label.setEnabled(False)
        self.textEdit.setEnabled(False)
        self.lineEdit.setEnabled(False)
        self.textEdit_2.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        if self.r:
            self.new()
            self.pushButton_3.clicked.connect(self.solve)
            self.pushButton_2.clicked.connect(self.right)
            self.pushButton.clicked.connect(self.left)

    def new(self):
        self.textEdit_2.setText('')
        self.lineEdit_3.setText(str(self.r[self.flag][0]))
        self.lineEdit_2.setText(str(self.r[self.flag][2]))
        self.lineEdit.setText(str(self.r[self.flag][3]))
        c = self.r[self.flag][1]
        self.textEdit.setText(c)


    def solve(self):
        if self.r[self.flag][5] == '??????':
            self.textEdit_2.setText('?????????????? ?????? ??????, ???? ???? ???????????? ???????????????? ?????? ???? ?????????????? ????????????, ???????????? ?????????? ???????????? ????????????')
        else:
            self.textEdit_2.setText(self.r[self.flag][5])


    def right(self):
        if self.flag + 1 <= len(self.r) and self.flag + 1 >= 0:
            self.flag = self.flag + 1
            self.new()

    def left(self):
        if self.flag - 1 <= len(self.r) and self.flag - 1 >= 0:
            self.flag = self.flag - 1
            self.new()





class TWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tasks.ui', self)
        self.textEdit.setStyleSheet("font: 17pt \"Academy\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgba(255, 255, 255, 170);")
        self.textEdit_2.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")
        self.textEdit_3.setStyleSheet("font: 17pt \"Academy\";\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgba(255, 255, 255, 170);")

        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        res = self.cur.execute(f"""SELECT task from problems""").fetchall()
        res1 = []
        for el in res:
            res1.append(el[0])
        res2 = []
        for i in range(len(res1)):
            res2.append(int(i))
        t = random.choice(res2)
        self.textEdit.setText(res1[t])
        res1.pop(res1.index(res1[t]))
        res2.pop(int(t))
        res2 = []
        for i in range(len(res1)):
            res2.append(int(i))
        m = random.choice(res2)
        self.textEdit_2.setText(res1[m])
        res1.pop(res1.index(res1[m]))
        res2.pop(int(m))
        res2 = []
        for i in range(len(res1)):
            res2.append(int(i))
        y = random.choice(res2)
        self.textEdit_3.setText(res1[y])
        res2.pop(int(y))



class PWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_new_solve.ui', self)
        self.label.setFont(QFont("Academy", 30))
        self.label_3.setFont(QFont("Academy", 17))
        self.label_4.setFont(QFont("Academy", 17))
        self.label_5.setFont(QFont("Academy", 17))
        self.label_6.setFont(QFont("Academy", 24))
        self.label_7.setFont(QFont("Academy", 24))
        self.textEdit.setFont(QFont("Academy", 17))
        self.textEdit_2.setFont(QFont("Academy", 17))
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgba(100, 100, 150, 170);")
        self.lineEdit_3.setFont(QFont("Academy", 17))
        self.lineEdit_2.setFont(QFont("Academy", 17))
        self.lineEdit_4.setFont(QFont("Academy", 17))
        self.pushButton.clicked.connect(self.add)


    def add(self):
        points = self.lineEdit_2.text()
        type1 = self.lineEdit_3.text()
        type2 = self.lineEdit_3.text()
        task = self.textEdit.toPlainText()
        solve = self.textEdit_2.toPlainText()
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        self.cur.execute(f"""INSERT INTO problems(task, points, type, type2, solve) VALUES('{str(task)}', '{str(points)}', '{str(type1)}', '{str(type2)}', '{str(solve)}')""")
        self.con.commit()
        self.label_9.setText('???????????? ??????????????????')



class SWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('search.ui', self)
        self.label.setFont(QFont("Academy", 30))
        self.label_2.setFont(QFont("Academy", 17))
        self.label_3.setFont(QFont("Academy", 17))
        self.label_4.setFont(QFont("Academy", 17))
        self.label_5.setFont(QFont("Academy", 17))
        self.label_6.setFont(QFont("Academy", 24))
        self.label_7.setFont(QFont("Academy", 24))
        self.label_8.setFont(QFont("Academy", 13))
        self.textEdit.setFont(QFont("Academy", 17))
        self.textEdit_2.setFont(QFont("Academy", 17))
        self.lineEdit_5.setFont(QFont("Academy", 17))
        self.pushButton_3.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.lineEdit_3.setFont(QFont("Academy", 17))
        self.lineEdit_2.setFont(QFont("Academy", 17))
        self.lineEdit_4.setFont(QFont("Academy", 17))
        self.lineEdit.setFont(QFont("Academy", 17))
        self.label_9.setFont(QFont("Academy", 17))
        self.pushButton_3.clicked.connect(self.find)
        self.pushButton.clicked.connect(self.add)




    def find(self):
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        try:
            res = self.cur.execute(f"""SELECT * FROM problems WHERE id = {int(self.lineEdit_5.text())}""").fetchall()[0]
        except Exception:
            pass
        item = []
        for el in res:
            item.append(el)
        self.lineEdit.setText(str(item[0]))
        self.lineEdit_2.setText(str(item[2]))
        self.lineEdit_3.setText(str(item[3]))
        self.lineEdit_4.setText(str(item[4]))
        self.textEdit.setText(str(item[1]))
        self.textEdit_2.setText(str(item[5]))


    def add(self):
        res = self.textEdit_2.toPlainText()
        id = self.lineEdit.text()
        self.cur.execute(f"""UPDATE problems SET solve = '{res}' WHERE id = {int(id)}""")
        self.label_9.setText('?????????????????? ??????????????????')
        self.con.commit()
        self.con.close()



class SolveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_solve.ui', self)
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        self.label.setFont(QFont("Academy", 17))
        self.textEdit.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color: rgba(100, 100, 150, 170);")
        self.pushButton.clicked.connect(self.make)

    def make(self):
        res = self.textEdit.toPlainText()
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        id = self.lineEdit.text()
        self.cur.execute(f"""UPDATE problems SET solve = '{res}' WHERE id = {int(id)}""")
        self.con.commit()
        self.con.close()
        TheMainWindow.solve(w)
        self.close()

class GoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('go.ui', self)
        self.label_5.setFont(QFont("Times New Roman", 16))
        self.label_2.setFont(QFont("Times New Roman", 16))
        self.label.setFont(QFont("Times New Roman", 16))
        self.lineEdit.setFont(QFont("Academy", 17))
        self.lineEdit_2.setEchoMode(2)
        self.lineEdit_2.setFont(QFont("Academy", 17))
        self.label_4.setFont(QFont("Times New Roman", 30))
        self.con = sqlite3.connect('profiles.db')
        self.cur = self.con.cursor()
        self.pushButton.setStyleSheet("font: 20pt \"Times New Roman\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgba(100, 100, 150, 170);")
        self.pushButton.clicked.connect(self.go)

    def go(self):
        global profile
        name = self.lineEdit.text()
        password1 = self.lineEdit_2.text()
        result = list(self.cur.execute("""SELECT * FROM profiles""").fetchall()[0])
        if name in result:
            password_main = self.cur.execute(f"""SELECT password FROM profiles WHERE name = '{name}'""").fetchall()[0][0]
            if password1 == password_main:
                points = self.cur.execute(f"""SELECT points FROM profiles WHERE name = '{name}'""").fetchall()[0][0]
                profile = [name, points]
                self.close()
        else:
            self.label_5.setText('?????????? ???????????????????????? ?????? ???? ??????????????????????????????')


class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('info.ui', self)
        self.textEdit.setFont(QFont("Times New Roman", 16))


class RegWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('registration.ui', self)
        self.con = sqlite3.connect('profiles.db')
        self.cur = self.con.cursor()
        self.lineEdit.setFont(QFont("Academy", 17))
        self.lineEdit_2.setFont(QFont("Academy", 17))
        self.lineEdit_2.setEchoMode(2)
        self.lineEdit_3.setEchoMode(2)
        self.lineEdit_3.setFont(QFont("Academy", 17))
        self.label_5.setFont(QFont("Times New Roman", 16))
        self.pushButton.setStyleSheet("font: 20pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.label.setFont(QFont("Times New Roman", 14))
        self.label_2.setFont(QFont("Times New Roman", 14))
        self.label_3.setFont(QFont("Times New Roman", 14))
        self.label_4.setFont(QFont("Times New Roman", 35))
        self.pushButton.clicked.connect(self.go)


    def go(self):
        global profile
        name = self.lineEdit.text()
        password1 = self.lineEdit_2.text()
        password2 = self.lineEdit_3.text()
        if password1 != password2:
            self.label_5.setText('?????????????? ???????????? ????????????')
        else:
            alpha = False
            digit = False
            for el in password2:
                if el.isdigit():
                    digit = True
                if el.isalpha():
                    alpha = True
            if alpha and digit:
                if name == '':
                    self.label_5.setText('?????????????????? ???????????? ????????')
                else:
                    result = list(self.cur.execute("""SELECT * FROM profiles""").fetchall()[0])
                    if name not in result:
                        profile = [name, 0]
                        self.cur.execute(f"""
                                            INSERT INTO profiles(points, name, password) VALUES({0}, '{name}', '{password1}')""")
                        self.con.commit()
                        self.close()
                        result = self.cur.execute("""SELECT name FROM profiles""").fetchall()
                        print(result)


                    else:
                        self.label_5.setText('???????????????????????? ?? ???????????? ?????????????????? ?????? ??????????????????????????????')
            else:
                self.label_5.setText('?? ???????????? ???????????? ???????? ?? ??????????, ?? ??????????')






class LitWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('literature.ui', self)
        global a
        self.con = sqlite3.connect('literature.db')
        self.cur = self.con.cursor()
        self.tableWidget.setStyleSheet("font: 17pt \"Academy\";\n"
                                        "color: rgb(100, 100, 150);\n"
                                        "background-color: rgba(250, 250, 255, 100);")
        self.label.setFont(QFont("Times New Roman", 20))
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(100, 100, 150, 170);")
        self.new()
        self.pushButton.clicked.connect(self.run)
        a = self

    def run(self):
        stylesheet_lit = """            ExtraWindow {                background-image: url("lit2.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
        self.win = ExtraWindow()
        self.win.setStyleSheet(stylesheet_lit)
        self.win.show()

    def new(self):
        result = self.cur.execute("""SELECT name, link, author, subject from books""").fetchall()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['????????????????', '????????????', '??????????', '??????????????'])
        for value, item in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for el, row in enumerate(item):
                self.tableWidget.setItem(value, el, QTableWidgetItem(str(row)))
        self.tableWidget.horizontalHeader().resizeSection(1, 300)
        self.tableWidget.horizontalHeader().resizeSection(0, 300)



class ExtraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('add_book.ui', self)
        self.con = sqlite3.connect('literature.db')
        self.cur = self.con.cursor()
        self.name.setFont(QFont("Times New Roman", 14))
        self.link.setFont(QFont("Times New Roman", 14))
        self.sub.setFont(QFont("Times New Roman", 14))
        self.author.setFont(QFont("Times New Roman", 14))
        self.pushButton.setStyleSheet("font: 12pt \"Times New Roman\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgba(0, 0, 100, 200);")
        self.pushButton.clicked.connect(self.run)


    def run(self):
        self.error.setText('')
        name = self.lineEdit.text()
        link = self.lineEdit_2.text()
        sub = self.lineEdit_3.text()
        author = self.lineEdit_4.text()
        try:
            if name.isdigit() or link.isdigit() or sub.isdigit() or author.isdigit():
                raise ValueError
            if name == '' or link == '' or sub == '' or author == '':
                raise NameError
        except ValueError:
            self.error.setText('?????????????? ?????????????????? ??????????')
            return
        except NameError:
            self.error.setText('?????????? ????????????, ?????????????????? ???? ??????????????????')
            return
        self.cur.execute("""
INSERT INTO books(name, link, author, subject) VALUES(?, ?, ?, ?)""", (name, link,
                                                                        author, sub))
        self.con.commit()
        self.con.close()
        LitWindow.new(a)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()

    stylesheet_main = """            MainWindow {                background-image: url("mainwindow1.png");                 background-repeat: no-repeat;                 background-position: center;            }        """
    ex.setStyleSheet(stylesheet_main)
    ex.show()
    sys.exit(app.exec_())

