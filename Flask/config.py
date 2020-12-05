# -*- coding: UTF-8 -*-
"""
@Author ：WangJie
@Date   ：2020/12/3 23:53 
@Desc   ：
"""

# setting配置文件
DEBUG = True                # 开启调试模式
SECRET_KEY = "962464"       # 随机输入字符串
PER_PAGE = 10               # 设置分页每页显示数据的个数为10
# SQLALCHEMY_DATABASE_URI = 链接的数据库类型+使用的驱动://用户名:密码@数据库地址:端口/数据库名称?数据库编码
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.181.128:3306/Flask?charset=utf8'    # 连接数据库
# SQLALCHEMY_ECHO = True      # 查询时会显示原始的sql语句
SQLALCHEMY_TRACK_MODIFICATIONS = False

