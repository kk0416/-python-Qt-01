#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/19 15:39
# @Author  : hkiny
# @File    : readconfig.py
# @Software: win10 Tensorflow1.13.1 python3.10.0
import configparser
import os


class ReadConfig(object):
    # 读取配置文件，所以参数要给文件路径
    def __init__(self, file_path):
        self.config_path = ""
        # 判断文件是否存在
        if os.path.isfile(file_path):
            self.config_path = file_path
        # 配置文件不存在--创建
        else:
            # 当前文件的路径
            root_dir = os.path.dirname(os.path.abspath(__file__))
            print(root_dir)
            self.config_path = os.path.join(root_dir, "config.ini")
        # 实例化对象
        self.cf = configparser.ConfigParser()
        # 读取该文件
        self.cf.read(self.config_path)

    def get_db_info(self):
        secs = self.cf.sections()
        print(secs)
        host = self.cf.get(secs[0], "host")
        user = self.cf.get(secs[0], "user")
        pwd = self.cf.get(secs[0], "pwd")
        dbname = self.cf.get(secs[0], "db")
        charset = self.cf.get(secs[0], "charset")
        # print(host,user,pwd,dbname,charset)
        # 返回dict形式的信息
        return {"host": host, "user": user, "pwd": pwd, "dbname": dbname, "charset": charset}
