#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 10:15
# @Author  : hkiny
# @File    : loginwin.py
# @Software: win10 Tensorflow1.13.1 python3.10.0

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LoginWin(QWidget):
    # 自定义返回信号  信号传参
    back_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录界面")
        self.setFixedSize(700, 500)
        self.setWindowIcon(QIcon("img/rubs.png"))  # ------没显示图标

        # 调用ui设置函数
        self.init_ui()
        self.init_connection()

    # 初始ui
    def init_ui(self):
        self.loginBtn = QPushButton("返回", self)  # 按钮
        self.loginBtn.move(50, 50)

    # 初始化数据
    def init_data(self):
        pass

    # 初始化连接  调用该函数
    def init_connection(self):
        # 登录跳转函数，返回主界面
        self.loginBtn.clicked.connect(self.doLogin)

    def doLogin(self):
        # pass
        # 触发发送自定义返回信号给主界面
        print("00")
        self.back_signal.emit("小月")

# # 1.创建应用
# app = QApplication(sys.argv)
# # 2.创建窗口
# LoginView = LoginWin()
# # 3.窗口显示 show
# LoginView.show()
# # 4.程序运行
# sys.exit(app.exec())
