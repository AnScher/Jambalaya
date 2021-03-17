# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QFont, QTextCursor, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QWidget, QMessageBox, QPushButton, QToolTip, \
    QSizePolicy, QScrollArea
import subprocess
from datetime import date, time, datetime, timedelta
import sys
import os


class Ui_MainWindow(object):
    buttonStyle = "QPushButton {border: 2px solid #8f8f91; border-radius: 6px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde); min-width: 80px; min-height: 40px; font-size: 18px; font-family: \"Calibri\";}"

    STARTING_POINT = datetime(2017, 11, 7)
    EXPIRATION_PERIOD = timedelta(180)

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("Info")
        MainWindow.resize(860, 680)
        MainWindow.setMaximumSize(860, 680)
        MainWindow.setMinimumSize(860, 680)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 820, 560))
        self.label.setStyleSheet("background: white; border: 2px solid #8f8f91; color: blue")
        self.scrollArea = QScrollArea(MainWindow)
        self.scrollArea.setGeometry(QRect(10, 10, 840, 560))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.label)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(30, 590, 250, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 590, 161, 81))
        self.pushButton.setStyleSheet(self.buttonStyle)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(QCoreApplication.instance().quit)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText("""<html>Some body</html>""")

        self.checkBox.setText(_translate("MainWindow", "Не показывать больше"))
        self.checkBox.stateChanged.connect(self.keyChanged)
        self.pushButton.setText(_translate("MainWindow", "Выход"))
        self.pushButton.setEnabled(False)
        self.center()

    def keyChanged(self):
        if self.checkBox.isChecked() == True:
            self.pushButton.setEnabled(True)
            subprocess.Popen("sed -i s/'\/usr\/bin\/python3 .*'/''/ /home/my_user/.config/openbox/autostart",
                             shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            self.pushButton.setEnabled(False)

    def center(self):
        frameGm = MainWindow.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        MainWindow.move(frameGm.topLeft())

    def checkTime(self):
        if datetime.now() - self.STARTING_POINT > self.EXPIRATION_PERIOD:
            msg_box = QMessageBox(self.MainWindow)
            msg_box.setWindowTitle("Warning")
            msg_box.setStyleSheet("QLabel{font-size: 24px; color: #F30C0C; font-weight: bold} " + self.buttonStyle)
            msg_box.setText("Some warning message")
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.checkTime()
    sys.exit(app.exec_())
