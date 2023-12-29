# This Python file uses the following encoding: utf-8
import os
import string
from pathlib import Path
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QRegularExpression, QModelIndex
from PyQt6.QtGui import QRegularExpressionValidator, QStandardItemModel, QStandardItem
from view.graphwindow import GraphWindow
from presenter.presenter import Presenter

SYMBOL = ['(', ')', 'e', 'x', '*', '/']
OPERATOR = ['+', '-', '*', '/', '^', 'd']
NUMBER = list(string.digits) + ['.', 'e']


class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(Path(__file__).resolve().parent / 'about.ui', self)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(Path(__file__).resolve().parent / 'mainwindow.ui', self)
        self.setWindowTitle('SmartCalculator')
        self.graph = GraphWindow()
        self.about = AboutWindow()
        self.history = QStandardItemModel()
        self.history_list.setModel(self.history)
        if os.path.isfile('history.txt'):
            self.load_history()

        validator = QRegularExpressionValidator(self)
        validator.setRegularExpression(QRegularExpression(r'[-+]?[0-9]*\.?[0-9]*'))
        self.enter_x.setValidator(validator)

        self.bracket_ = 0
        self.button_ = []
        self.dot_ = False
        self.exp_ = False
        self.digit_ = False

        self.push_button()

    def push_button(self):
        self.buttonGroupDigit.buttonClicked.connect(self.digit_click)
        self.buttonGroupPlusMinus.buttonClicked.connect(self.plusminus_click)
        self.buttonGroupArithmetic.buttonClicked.connect(self.arithmetic_click)
        self.buttonGroupFunction.buttonClicked.connect(self.function_click)
        self.pushButton_bracket_open.clicked.connect(self.bracket_open_click)
        self.pushButton_bracket_close.clicked.connect(self.bracket_close_click)
        self.pushButton_backspace.clicked.connect(self.backspace_click)
        self.pushButton_dot.clicked.connect(self.dot_click)
        self.pushButton_e.clicked.connect(self.e_click)
        self.pushButton_x.clicked.connect(self.x_click)
        self.pushButton_AC.clicked.connect(self.ac_click)
        self.pushButton_equal.clicked.connect(self.equal_click)
        self.pushButton_graph.clicked.connect(self.graph_click)
        self.pushButton_clear.clicked.connect(self.clear_history)
        self.actionAbout.triggered.connect(self.open_about)
        self.history_list.clicked[QModelIndex].connect(self.get_history_list)

    def open_about(self):
        self.about.show()

    def digit_click(self, btn):
        res = self.enter_exp.text()
        if not len(res) or (res[-1] not in [')', 'x']):
            if len(res) and res[-1] == '0' and not self.dot_:
                res = res[:-1]
                if len(res) and res[-1] in list(string.digits):
                    res = res + "0"
                else:
                    self.button_.pop()
            self.enter_exp.setText(res + btn.text())
            self.button_.append(len(btn.text()))
            self.digit_ = True

    def dot_click(self):
        res = self.enter_exp.text()
        if not self.dot_ and not self.exp_:
            if self.digit_:
                self.enter_exp.setText(res + self.sender().text())
                self.button_.append(len(self.sender().text()))
                self.dot_ = True
            elif not len(res) or res[-1] not in [')', 'x']:
                self.enter_exp.setText(res + "0" + self.sender().text())
                self.button_.append(len(self.sender().text()))
                self.button_.append(len(self.sender().text()))
                self.dot_ = self.digit_ = True

    def plusminus_click(self, btn):
        res = self.enter_exp.text()
        if len(res) and res[-1] in ['+', '-']:
            res = res[:-self.button_.pop()]
        if not len(res) or res[-1] in list(string.digits) + SYMBOL:
            self.enter_exp.setText(res + btn.text())
            self.button_.append(len(btn.text()))
            if len(res) and res[-1] != 'e':
                self.settings(False)

    def arithmetic_click(self, btn):
        res = self.enter_exp.text()
        if len(res):
            if len(res) > 1 and res[-1] in OPERATOR and res[-2] not in ['(', 'e']:
                res = res[:-self.button_.pop()]
            if res[-1] in list(string.digits) + [')', 'x']:
                self.enter_exp.setText(res + btn.text())
                self.button_.append(len(btn.text()))
                self.settings(False)

    def function_click(self, btn):
        res = self.enter_exp.text()
        if not len(res) or (not self.digit_ and res[-1] not in [')', 'x', 'd']):
            self.enter_exp.setText(res + btn.text() + "(")
            self.button_.append(len(btn.text()) + 1)
            self.bracket_ += 1

    def bracket_open_click(self):
        res = self.enter_exp.text()
        if not len(res) or (not self.digit_ and res[-1] not in [')', 'x']):
            self.enter_exp.setText(res + self.sender().text())
            self.button_.append(len(self.sender().text()))
            self.bracket_ += 1

    def bracket_close_click(self):
        res = self.enter_exp.text()
        if self.bracket_ and res[-1] in list(string.digits) + [')', 'x']:
            self.enter_exp.setText(res + self.sender().text())
            self.button_.append(len(self.sender().text()))
            self.bracket_ -= 1
            self.settings(False)

    def e_click(self):
        res = self.enter_exp.text()
        if not self.exp_ and len(res) and res[-1] in list(string.digits):
            self.enter_exp.setText(res + self.sender().text())
            self.button_.append(len(self.sender().text()))
            self.settings(True)

    def x_click(self):
        res = self.enter_exp.text()
        if not len(res) or (not self.digit_ and res[-1] not in ['x', ')']):
            self.enter_exp.setText(res + self.sender().text())
            self.button_.append(len(self.sender().text()))

    def ac_click(self):
        self.enter_exp.setText("")
        self.res_output.setText("")
        self.enter_x.setText("")
        self.button_.clear()
        self.bracket_ = 0
        self.settings(False)

    def backspace_click(self):
        if len(self.button_):
            res = self.enter_exp.text()
            if res[-1] == ')':
                self.bracket_ += 1
            elif res[-1] == '(':
                self.bracket_ -= 1
            res = res[:-self.button_.pop()]
            self.enter_exp.setText(res)
            self.settings(False)
            if len(res) and res[-1] in NUMBER:
                self.digit_ = True
                while len(res) and res[-1] in NUMBER:
                    if res[-1] == '.':
                        self.dot_ = True
                    elif res[-1] == 'e':
                        self.exp_ = self.dot_ = True
                    res = res[:-1]

    def equal_click(self):
        res = self.enter_exp.text()
        self.res_output.setText("")
        if len(res):
            if self.bracket_ or res[-1] not in list(string.digits) + ['x', ')']:
                self.res_output.setText("Error")
            else:
                x_value = self.enter_x.text()
                if x_value:
                    x_value = float(x_value)
                else:
                    x_value = 0
                self.res_output.setText(str(Presenter.calculate(res, x_value)))
                self.history.appendRow(QStandardItem(res))
                self.save_history()

    def load_history(self):
        with open('history.txt', 'rt', encoding='utf-8') as file:
            for item in file.readlines():
                self.history.appendRow(QStandardItem(item.strip()))

    def save_history(self):
        with open('history.txt', 'at', encoding='utf-8') as file:
            file.write(self.enter_exp.text() + '\n')

    def get_history_list(self, index):
        self.enter_exp.setText(self.history.itemFromIndex(index).text())

    def clear_history(self):
        self.history.clear()
        with open('history.txt', 'wt', encoding='utf-8') as _:
            pass

    def graph_click(self):
        self.graph.set_formula(self.enter_exp.text())
        self.graph.show()

    def settings(self, setting):
        self.dot_ = setting
        self.exp_ = setting
        self.digit_ = setting
