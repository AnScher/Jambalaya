# -*- coding: utf-8 -*-

import subprocess
import sys
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication, Qt, QTimer
from PyQt5.QtWidgets import QMessageBox, QLabel, QFrame, QPushButton, QApplication
from PyQt5.QtGui import QIcon, QFont, QTextCursor, QFontDatabase
from datetime import datetime
from itertools import chain
from configparser import ConfigParser


class Ui_MainWindow(object):
    buttonStyle = "QPushButton {border: 2px solid #8f8f91; border-radius: 6px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde); min-width: 80px; min-height: 40px; font-size: 18px; font-family: \"Calibri\"}"
    info_btnStyle = "QPushButton {border: 2px solid #8f8f91; border-radius: 6px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde); min-width: 80px; min-height: 40px; font-size: 28px; font-family: \"Calibri\";color:red}"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 630)
        MainWindow.setMaximumSize(QtCore.QSize(880, 630))
        MainWindow.setMinimumSize(QtCore.QSize(880,630))
        #MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setWindowIcon(QIcon(r'/usr/local/service/Python/pppoe/pppoe.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(420, 85, 451, 311))
        self.textEdit.setStyleSheet("QTextEdit {color:purple; font-size:15px; font-family: \"Calibri\"}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.textEdit.setAlignment(Qt.AlignRight)
        self.info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.info_btn.setStyleSheet(self.info_btnStyle)
        self.info_btn.setGeometry(QtCore.QRect(375, 520, 170, 51))
        self.info_btn.clicked.connect(self.help)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        #self.info_btn.setFont(font)
        #self.info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.info_btn.setToolTipDuration(-1)
        #self.info_btn.setAutoFillBackground(True)
        self.info_btn.setObjectName("info_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(740, 550, 131, 51))
        self.exit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.exit_btn.setStyleSheet(self.buttonStyle)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setGeometry(QtCore.QRect(30, 20, 361, 441))
        self.groupbox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupbox.setObjectName("groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.interface_name = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.interface_name.setFont(font)
        self.interface_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.interface_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.interface_name.setLineWidth(1)
        self.interface_name.setTextFormat(QtCore.Qt.AutoText)
        self.interface_name.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.interface_name.setObjectName("interface_name")
        self.verticalLayout.addWidget(self.interface_name)
        self.lineEdit = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.login = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.login.setFont(font)
        self.login.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.password = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.dns1 = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dns1.setFont(font)
        self.dns1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.dns1.setObjectName("dns1")
        self.verticalLayout.addWidget(self.dns1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.dns2 = QtWidgets.QLabel(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.dns2.setFont(font)
        self.dns2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.dns2.setObjectName("dns2")
        self.verticalLayout.addWidget(self.dns2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setFrame(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.save_btn = QtWidgets.QPushButton(self.groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.save_btn.setBaseSize(QtCore.QSize(0, 0))
        self.save_btn.setStyleSheet(self.buttonStyle)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.save_btn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.save_btn.setIconSize(QtCore.QSize(16, 16))
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.save_btn.setStyleSheet(self.buttonStyle)
        self.save_btn.clicked.connect(self.change_settings)
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(731, 27, 140, 31))
        self.time.setObjectName("time")
        self.time.setStyleSheet('color: black')
        self.time.setFrameShape(QFrame.Panel)
        self.time.setFrameShadow(QFrame.Raised)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.groupbox1 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox1.setGeometry(QtCore.QRect(420, 390, 451, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupbox1.setFont(font)
        self.groupbox1.setObjectName("groupbox1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupbox1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.interface_test_btn = QtWidgets.QPushButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.interface_test_btn.setFont(font)
        self.interface_test_btn.setObjectName("interface_test_btn")
        self.interface_test_btn.clicked.connect(self.checkInterface)
        self.interface_test_btn.setStyleSheet(self.buttonStyle)
        self.horizontalLayout.addWidget(self.interface_test_btn)
        self.connect_btn = QtWidgets.QPushButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.connect_btn.setFont(font)
        self.connect_btn.setObjectName("connect_btn")
        self.horizontalLayout.addWidget(self.connect_btn)
        self.connect_btn.clicked.connect(self.connectPPPoE)
        self.connect_btn.setStyleSheet(self.buttonStyle)
        self.drop_btn = QtWidgets.QPushButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.drop_btn.setFont(font)
        self.drop_btn.setObjectName("drop_btn")
        self.horizontalLayout.addWidget(self.drop_btn)
        self.drop_btn.clicked.connect(self.pppoeTurnOff)
        self.drop_btn.setStyleSheet(self.buttonStyle)
        self.ping_btn = QtWidgets.QPushButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.ping_btn.setFont(font)
        self.ping_btn.setObjectName("ping_btn")
        self.horizontalLayout.addWidget(self.ping_btn)
        self.ping_btn.clicked.connect(self.checkPing)
        self.ping_btn.setStyleSheet(self.buttonStyle)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setStyleSheet(self.buttonStyle)
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.setGeometry(QtCore.QRect(30, 550, 141, 51))
        self.clear_btn.clicked.connect(self.clearSettings)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PPPoE Settings"))
        self.info_btn.setText(_translate("MainWindow", "Инструкция"))
        self.exit_btn.setText(_translate("MainWindow", "Выход"))
        self.groupbox.setTitle(_translate("MainWindow", "Настройки сетевого интерфейса"))
        self.interface_name.setText(_translate("MainWindow", "Название сетевого интерфейса:"))
        self.login.setText(_translate("MainWindow", "Имя пользователя:"))
        self.password.setText(_translate("MainWindow", "Пароль:"))
        self.dns1.setText(_translate("MainWindow", "DNS-сервер 1:"))
        self.lineEdit_4.setInputMask(_translate("MainWindow", "009.009.009.009"))
        self.lineEdit_4.setText(_translate("MainWindow", "8.8.8.8"))
        self.dns2.setText(_translate("MainWindow", "DNS-сервер 2:"))
        self.lineEdit_5.setInputMask(_translate("MainWindow", "009.009.009.009"))
        self.lineEdit_5.setText(_translate("MainWindow", "8.8.4.4"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить"))
        self.interface_test_btn.setText(_translate("MainWindow", "Определить \n"
"интерфейс"))
        self.connect_btn.setText(_translate("MainWindow", "Подключить\n"
"интернет"))
        self.drop_btn.setText(_translate("MainWindow", "Отключить\n"
"интернет"))
        self.ping_btn.setText(_translate("MainWindow", "Проверить \n"
"Ping"))
        self.clear_btn.setText(_translate("MainWindow", "Сброс настроек"))
        self.center()
    """def savesettings(self):
        settings_path = '/etc/ppp/pppoe.conf'
        pap = '/etc/ppp/pap-secrets'
        chap = '/etc/ppp/chap-secrets'
        if os.path.exists(settings_path) and os.path.isfile(settings_path):
            with open(settings_path, 'r') as file:
                spisok = file.readlines()
                spisok[26] = 'ETH=' + str(self.lineEdit.text()) + '\n'
                spisok[33] = 'USER=' + str(self.lineEdit_2.text()) + '\n'
                spisok[50] = 'DNS1=' + str(self.lineEdit_4.text()) + '\n'
                spisok[51] = 'DNS2=' + str(self.lineEdit_5.text()) + '\n'
            with open(settings_path, 'w') as file:
                file.writelines(spisok)
        else:
            self.textEdit.setText('Ошибка! Не найден файл pppoe.conf в директории /etc/ppp/')
        if os.path.exists(pap) and os.path.isfile(pap):
            with open(pap, 'a') as file:
                file.write(str(self.lineEdit_2.text()) + '        *        ' + str(self.lineEdit_3.text()) + '\n')
        else:
            self.textEdit.setText('Ошибка! Не найден файл pap-secrets в директории /etc/ppp/')
        if os.path.exists(chap) and os.path.isfile(chap):
            with open(chap, 'a') as file:
                file.write(str(self.lineEdit_2.text()) + '        *        ' + str(self.lineEdit_3.text()) + '\n')
        else:
            self.textEdit.setText('Ошибка! Не найден файл chap-secrets в директории /etc/ppp/')
    """

    def change_settings(self, settings_path, **key_value_pairs):
        settings_path = '/etc/ppp/pppoe.conf'
        pap = '/etc/ppp/pap-secrets'
        chap = '/etc/ppp/chap-secrets'
        resolv = '/etc/resolv.conf'
        autostart = '/home/my_user/.config/openbox/autostart'
        command = '/usr/sbin/pppoe-start'
        if os.path.exists(settings_path) and os.path.isfile(settings_path):
            with open(settings_path) as file:
                lines = file.readlines()
            key_value_pairs = {'ETH': str(self.lineEdit.text()),
                               'USER': str(self.lineEdit_2.text()),
                               'DNS1': str(self.lineEdit_4.text()),
                               'DNS2': str(self.lineEdit_5.text())}
            keys = frozenset(key for key in key_value_pairs.keys())
            out_lines = []
            seen_keys = set()
            for line in lines:
                out_line = line
                if '=' in line:
                    key, value = line.split('=', 1)
                    if key in keys:
                        seen_keys.add(key)
                        out_line = '%s=%s\n' % (key, key_value_pairs[key])
                out_lines.append(out_line)
            for key in (keys - seen_keys):
                out_lines.append('%s=%s\n' % (key, key_value_pairs[key]))
            with open(settings_path, 'w') as file:
                file.writelines(out_lines)
            with open(autostart, 'a') as file:
                file.write(command)


        else:
            self.textEdit.setText('Ошибка! Не найден файл pppoe.conf в директории /etc/ppp/')
        if os.path.exists(pap) and os.path.isfile(pap):
            with open(pap, 'a') as file:
                file.write(str(self.lineEdit_2.text()) + '        *        ' + str(self.lineEdit_3.text()) + '\n')
        else:
            self.textEdit.setText('Ошибка! Не найден файл pap-secrets в директории /etc/ppp/')
        if os.path.exists(chap) and os.path.isfile(chap):
            with open(chap, 'a') as file:
                file.write(str(self.lineEdit_2.text()) + '        *        ' + str(self.lineEdit_3.text()) + '\n')
        else:
            self.textEdit.setText('Ошибка! Не найден файл chap-secrets в директории /etc/ppp/')
        if os.path.exists(resolv) and os.path.isfile(resolv):
            with open(resolv, 'w') as file:
                file.write(str(self.lineEdit_4.text()) + '\n' + str(self.lineEdit_5.text()))
        else:
            self.textEdit.setText('Ошибка! Не найден файл resolv.conf в директории /etc/')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Вы действительно хотите выйти?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def checkPing(self):
        with subprocess.Popen(["ping", "-c 3 ", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as result:
            out = result.stdout.read()
            err = result.stderr.read()
            self.textEdit.setText((out if out else err).decode('utf-8'))

    def connectPPPoE(self):
        with subprocess.Popen("/usr/sbin/pppoe-start; rc-update add pppoe default", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as result:
            out = result.stdout.read()
            err = result.stderr.read()
            self.textEdit.setText((out if out else err).decode('utf-8'))

    def pppoeTurnOff(self):
        with subprocess.Popen("/usr/sbin/pppoe-stop; rc-update del pppoe", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as result:
            out = result.stdout.read()
            err = result.stderr.read()
            self.textEdit.setText((out if out else err).decode('utf-8'))

    def checkInterface(self):
        with subprocess.Popen("cat /proc/net/dev | awk -F : '{if (NR>2) print $1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as result:
            out = result.stdout.read()
            err = result.stderr.read()
            self.textEdit.setText((out if out else err).decode('utf-8'))

    def help(self):
        with open(r"/usr/local/service/Python/pppoe/hosts.txt", encoding="utf-8") as text:
            self.textEdit.setText(text.read())

    def showTime(self):
        cur_time = datetime.strftime(datetime.now(), "%d.%m.%y  %H:%M:%S")
        self.time.setText(cur_time)

    def clearSettings(self):
        subprocess.Popen(["cp", "/etc/ppp/pppoe.conf-bak", "/etc/ppp/pppoe.conf"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.Popen(["cp", "/etc/resolv.conf-bak", "/etc/resolv.conf"])
        subprocess.Popen(["cp", "/etc/ppp/pap-secrets-bak", "/etc/ppp/pap-secrets"])
        subprocess.Popen(["cp", "/etc/ppp/chap-secrets-bak", "/etc/ppp/chap-secrets"])
        subprocess.Popen(["cp", "/home/my_user/.config/openbox/autostart.bak", "/home/my_user/.config/openbox/autostart"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.Popen(["sed", "-i", "s'/\/usr\/sbin\/pppoe-start'/''/", "/home/my_user/.config/openbox/autostart"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        
    def center(self):
        frameGm = MainWindow.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        MainWindow.move(frameGm.topLeft())



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

