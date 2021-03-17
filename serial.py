# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QFileDialog, QApplication, QWidget, QMessageBox, QPushButton, QToolTip, QSizePolicy
from PyQt5.QtGui import QIcon, QFont, QTextCursor, QFontDatabase
from PyQt5.QtCore import QCoreApplication, Qt

class Example(QMainWindow):
    buttonStyle = "QPushButton {border: 2px solid #8f8f91; border-radius: 6px; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde); min-width: 80px; min-height: 40px; font-size: 20px; font-family: \"Sans-serif\"; cursor: pointer;}"
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.textEdit.setStyleSheet("QTextEdit {color:blue; font-size:20px;}")
        self.textEdit.selectAll()
        self.textEdit.setFontPointSize(18)
        self.textEdit.setMaximumHeight(40)
        self.textEdit.textChanged.connect(self.keyChanged)
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.openFile)

        exit_btn = QPushButton('Exit', self)
        exit_btn.clicked.connect(QCoreApplication.instance().quit)
        #exit_btn.setFont(QFont('SansSerif', 14))
        exit_btn.resize(200, 60)
        exit_btn.move(290, 205)

        self.copy_btn = copy_btn = QPushButton('Load key', self)
        copy_btn.clicked.connect(self.serialCopy)
        copy_btn.setToolTip('Rename and copy key')
        #copy_btn.setFont(QFont('SansSerif', 14))
        copy_btn.resize(200, 60)
        copy_btn.move(10, 205)

        clr_btn = QPushButton('Delete key', self)
        clr_btn.clicked.connect(self.clearText)
        #clr_btn.setFont(QFont('SansSerif', 34))
        clr_btn.resize(200, 60)
        clr_btn.move(290, 75)

        open_btn = QPushButton('Open file', self)
        open_btn.clicked.connect(self.openFile)
        #open_btn.setFont(QFont('SansSerif', 14))
        open_btn.resize(200, 60)
        open_btn.move(10, 75)

        #self.setGeometry(600, 380, 500, 300)
        #policy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        #self.setSizePolicy(policy)
        self.setFixedSize(500, 300)
        self.setWindowTitle('Load key')
        self.setWindowIcon(QIcon(r'/path_to_icon/qicon.png'))
        self.center()
        self.show()
        self.openFile()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Exit', "Do you want to exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, directory='/media/')#, os.getenv('HOME'))
        if filename[0]:
            with open(filename[0], 'r') as file:
                my_text = file.read()
            self.textEdit.setText(my_text)
            self.textEdit.moveCursor(QTextCursor.End)
            self.textEdit.setFocus()

    def serialCopy(self):
        try:
            with open(r"/usr/local/my_user/config/serial.pin", 'w') as f:
                f.write(self.textEdit.toPlainText())
        except FileNotFoundError:
            msg_box2 = QMessageBox(self)
            msg_box2.setWindowTitle("Error occured during copying")
            msg_box2.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} " + self.buttonStyle)
            msg_box2.setText("Error occured!")
            msg_box2.setStandardButtons(QMessageBox.Ok)
            msg_box2.setDefaultButton(QMessageBox.Ok)
            msg_box2.exec_()
        else:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Copy key")
            msg_box.setStyleSheet("QLabel{min-width:300 px; font-size: 16px;} " + self.buttonStyle)
            msg_box.setText("Success!")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.setDefaultButton(QMessageBox.Ok)
            msg_box.exec_()

    def clearText(self):
        self.textEdit.clear()
        self.textEdit.setFocus()

    def center(self):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def keyChanged(self):
        if not self.textEdit.toPlainText():
            self.copy_btn.setEnabled(False)
        else:
            self.copy_btn.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Example.buttonStyle)
    ex = Example()
    sys.exit(app.exec_())
