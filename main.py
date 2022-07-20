#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 10:15
# @Author  : hkiny
# @File    : main.py
# @Software: win10 Tensorflow1.13.1 python3.10.0

"""
主入口文件
"""
import sys
import MySQLdb
from PyQt5.QtWidgets import QApplication
from view.mainwin import MainWin
from tool.readconfig import ReadConfig

if __name__ == '__main__':
    readcon = ReadConfig("config.ini")
    config_dict = readcon.get_db_info()
    try:
        db = MySQLdb.connect(config_dict['host'],
                             config_dict['user'],
                             config_dict['pwd'],
                             config_dict['dbname'],
                             charset=config_dict['charset'])
        db.close()
        print("数据库连接成功")
        print(config_dict)
        # 1.创建应用
        app = QApplication(sys.argv)
        # 2.创建窗口
        mainView = MainWin()
        # 3.窗口显示 show
        mainView.show()
        # 4.程序运行
        sys.exit(app.exec())
    except:
        print("数据库连接失败")
