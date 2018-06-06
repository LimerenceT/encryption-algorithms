#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Main window to show."""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QLineEdit, QPushButton, QGridLayout, QLabel, QMessageBox)
from algorithm.gcd import gcd, gcd_stein


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
        ok_button1 = QPushButton('GCD结果')
        ok_button2 = QPushButton('stein结果')

        grid.addWidget(QLabel('数字1：'), 1, 1)
        grid.addWidget(self._input_num1, 1, 2)
        grid.addWidget(QLabel('数字2：'), 1, 3)
        grid.addWidget(self._input_num2, 1, 4)
        grid.addWidget(ok_button1, 1, 5)
        grid.addWidget(ok_button2, 1, 6)
        grid.addWidget(self.result, 1, 7)

        ok_button1.clicked.connect(self.button1_clicked)
        ok_button2.clicked.connect(self.button2_clicked)

        self.resize(500, 100)
        self.center()
        self.setWindowTitle('GCD')
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
            result = self.get_result(gcd)
            self.result.setText(result)
        except ValueError:
            self.show_dialog()

    def button2_clicked(self):
        """handle this button clinked"""
        try:
            result = self.get_result(gcd_stein)
            self.result.setText(result)
        except ValueError:
            self.show_dialog()

    def get_result(self, gcd_func):
        _num1 = int(self._input_num1.text())
        _num2 = int(self._input_num2.text())
        result = gcd_func(_num1, _num2)
        return str(result)

    def show_dialog(self):
        """show error to user"""
        QMessageBox.warning(self, "error", "请输入整数字", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Gcd()
    sys.exit(app.exec_())
