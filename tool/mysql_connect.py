#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 14:59
# @Author  : hkiny
# @File    : readconfig.py
# @Software: win10 Tensorflow1.13.1 python3.10.0
import MySQLdb


class Mysql_base:
    # protected静态成员变量
    _is_connect = False

    """
    mysql 数据库连接，对数据库操作类
    """
    # 类方法：单例的那个函数 是否创建新的数据库对象
    def __new__(cls, *args, **kwargs):
        # "单例"
        if not hasattr(cls, "_instance"):
            cls._instance = super(Mysql_base, cls).__new__(cls)
        return cls._instance
    # '192.168.1.3'
    def __init__(self, db_name, passwd, usr_name='root', host='localhost', port='3306'):
        if Mysql_base._is_connect is False:
            try:        # 异常处理：数据库连接
                self.__db = MySQLdb.connect(host, usr_name, passwd, db_name)
                print("success")
                Mysql_base._is_connect = True
                # 获取游标
                self.__cursor = self.__db.cursor()
            except:
                print('cannot connect db!')

    def execute(self, sql):
        """
        执行任何的sql语句
        :param sql: sql语句
        :return:
        """
        try:
            # 执行sql语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
        except:
            # 发生错误时回滚
            print("execute error")
            self.__db.rollback()

    def select_op(self, sql):
        """
        执行sql语句
        :param sql: sql语句
        :return:
        """
        data = 0
        try:
            # 执行sql语句
            self.__cursor.execute(sql)
            # 提交到数据库执行
            self.__db.commit()
            # 使用 fetchone() 方法获取一条数据
            data = self.__cursor.fetchall()
        except:
            # 发生错误时回滚
            print("execute error")
            self.__db.rollback()
        return data

    def insert_opr(self, sql):
        """
        更新、插入、删除操作
        :param sql: SQL语句
        :return: 所有记录列表
        """
        try:
            # 执行SQL语句
            self.__cursor.execute(sql)
            self.__db.commit()
            return self.__cursor.rowcount
        except:
            print("Error: unable to fecth data")

    def __del__(self):
        # 关闭数据库
        self.__db.close()


if __name__ == "__main__":
    # 数据库连接
    db = Mysql_base(db_name="omo210802416", passwd="123456")
    # # ----例子01：查找语句并返回数据----
    data = db.select_op("select * from tbl_user WHERE user_name='{}' ;".format(
        "xiaoan"
    ))
    print(data)
    print(len(data))
    # ----例子02：更新数据-----
    # 如果搜索到了该用户，更改其状态为0：冻结
    if len(data) > 0:
        # 冻结
        id = db.insert_opr("update tbl_user set usr_status=0 where user_name='{}';".format("xiaoan"))
        print(id)
    #
    # ((1, 'user01', '123456', 'user01.png', 0),)
    # ----例子03：插入数据-----
#     user_name = "guli"
#     img_path = "userImg/20220619guli.png"
#     reg_time = '2022-06-29 15:31:30'
#     sql = "INSERT into tbl_user(user_name, img_path, reg_time) \
# values('{}', '{}', '{}')".format(user_name, img_path, reg_time)
#     print(sql)
#     user_id = db.insert_opr(sql)
#     print(user_id)

