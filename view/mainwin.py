#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 9:24
# @Author  : hkiny
# @File    : mainwin.py
# @Software: win10 Tensorflow1.13.1 python3.10.0
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from view.loginwin import LoginWin
# from 库名（另一个文件名） import 类名
"""
图片右键复制粘贴到工程目录里

"""


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        #
        self.userlayout = QHBoxLayout()
        self.setWindowTitle("主界面")
        self.setFixedSize(1000, 700)
        self.setWindowIcon(QIcon("img/rubs.png"))  # ------没显示图标
        # 创建登陆界面
        self.loginWin=LoginWin()
        # 调用ui设置函数
        self.init_ui()
        self.init_connection()

    # 初始化ui
    def init_ui(self):
        self.totalBoxLayout = QHBoxLayout()  # 整体水平布局
        # 设置左边区域 setStyleSheet（“background:green”）
        self.leftView = QWidget(self)  # 创建总布局的左边界面
        # self.leftView.setStyleSheet()  # 左边界面背景色设置为绿色（里面是qss）
        # 左边内容：
        # 垂直布局  label要设置siae  setMinimumSize(60,60)
        self.leftlayout = QVBoxLayout()
        # 用户信息界面
        self.userInfo = QWidget(self)
        # 用户信息水平布局
        self.imgLabel = QLabel(self)  # 头像
        self.imgLabel.setPixmap(QPixmap("./img/rubs.png").scaled(60, 60))
        self.imgLabel.setMinimumSize(60, 60)
        self.loginBtn = QPushButton("登录", self)  # 按钮
        self.usrname = QLabel("你好xxx", self)  # 登陆成功欢迎用户
        self.usrname.setMaximumWidth(150)
        self.usrname.hide()
        # 将控件加入用户水平布局
        self.userlayout.addWidget(self.imgLabel)
        self.userlayout.addWidget(self.loginBtn)
        self.userlayout.addWidget(self.usrname)
        # 用户水平布局布置到用户信息界面里
        self.userInfo.setLayout(self.userlayout)
        # -------------创建左上角用户信息结束

        # --------------创建左下角菜单start
        self.userManagerBtn = QPushButton("用户信息管理")
        self.recoverBtn = QPushButton("变废为宝模式")
        # 将用户水平布局加入整体水平布局的左边布局
        self.leftlayout.addWidget(self.userInfo)
        self.leftlayout.addWidget(self.userManagerBtn)
        self.leftlayout.addWidget(self.recoverBtn)
        # 将左边布局添加到左边界面
        self.leftView.setLayout(self.leftlayout)

        # 设置右边区域
        self.rightView = QWidget(self)
        self.rightView.setStyleSheet("background:blue")

        # 将左右塞进布局 addwidget（左右布局名，占据区域比例）
        self.totalBoxLayout.addWidget(self.leftView, 3)
        self.totalBoxLayout.addWidget(self.rightView, 7)
        # 将总布局加入布局
        self.setLayout(self.totalBoxLayout)
        # 加上这两行布局贴边
        self.totalBoxLayout.setSpacing(0)
        self.totalBoxLayout.setContentsMargins(0, 0, 0, 0)
        # 将该函数在上方def __init__(self)调用

    # 初始化数据
    def init_data(self):
        pass

    # 初始化连接  调用该函数
    def init_connection(self):
        """
        self.loginBtn.Clicked.connect(self.toLogin)
        调用发送登陆类的自定义返回信号--表示登陆成功，要返回主界面
        --需要写对应的槽函数
            （登陆界面隐藏，显示主界面，用户名显示到主界面，主界面登录按钮显示为退出）
        """
        self.loginBtn.clicked.connect(self.toLogin)
        self.loginWin.back_signal.connect(self.successlogin)

    # 登录函数
    def toLogin(self):
        # 判断按钮内容是登陆的话
        if self.loginBtn.text() =="登录":
            # 隐藏当前界面
            self.hide()
            # 弹出登陆界面
            self.loginWin.show()
        #  按钮内容为退出
        elif self.loginBtn.text() =="退出":
            # 按钮内容变为请登录
            self.loginBtn.setText("登录")
            self.usrname.hide()

    # 登陆成功槽函数
    def successlogin(self,name):
        # 登陆界面隐藏，
        self.loginWin.hide()
        # 显示主界面，
        self.show()
        # 用户名显示到主界面，
        self.usrname.setText("你好，"+name)
        self.usrname.show()
        # 主界面登录按钮显示为退出）
        self.loginBtn.setText("退出")


#
# #1.创建应用
# app=QApplication(sys.argv)
# #2.创建窗口
# mainView=MainWin()
# #3.窗口显示 show
# mainView.show()
# #4.程序运行
# sys.exit(app.exec())


















