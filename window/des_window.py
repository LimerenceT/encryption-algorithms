#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Main window to show."""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QLineEdit, QPushButton, QGridLayout, QLabel, QMessageBox)
from algorithm.des import des


class Gcd(QWidget):

    def __init__(self):
        super(Gcd, self).__init__()
        self._input_num1 = QLineEdit()
        self._input_num2 = QLineEdit()
        self.result = QLineEdit()
        self.init_ui()

    def init_ui(self):
        """init the window and show it"""
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)
        ok_button1 = QPushButton('加密')
        ok_button2 = QPushButton('解密')

        grid.addWidget(QLabel('明文：'), 2, 1)
        grid.addWidget(self._input_num1, 2, 2)
        grid.addWidget(QLabel('8位密钥：'), 2, 3)
        grid.addWidget(self._input_num2, 2, 4)
        grid.addWidget(ok_button1, 2, 5)
        grid.addWidget(ok_button2, 2, 6)
        grid.addWidget(self.result, 2, 7)

        ok_button1.clicked.connect(self.button1_clicked)
        ok_button2.clicked.connect(self.button2_clicked)

        self.resize(800, 100)
        self.center()
        self.setWindowTitle('DES(Only English letters and numbers are supported)')
        self.show()

    def center(self):
        """make window located center."""
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button1_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(des, 'encrypt')
            self.result.setText(result)
        except ValueError:
            self.show_dialog()

    def button2_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(des, '')
            self.result.setText(result)

        except ValueError:
            self.show_dialog()

    def get_result(self, gcd_func, en_or_de):
        _num1 = self._input_num1.text()
        _num2 = self._input_num2.text()
        if len(_num2) == 8:
            result = gcd_func(_num1, _num2, en_or_de)
            return result
        else:
            raise ValueError

    def show_dialog(self):
        """show error to user"""
        QMessageBox.warning(self, "error", "请输入8位密钥", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Gcd()
    sys.exit(app.exec_())
