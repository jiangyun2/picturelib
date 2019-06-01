#!/usr/bin/python
# -*- coding: utf-8 -*

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库数据
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'picturelib'
USERNAME = 'admin'
PASSWORD = 'Root110qwe'
# 数据连接 URL
Db_Uri = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,DATABASE)
# 连接数据库
engine = create_engine(Db_Uri)
# 创建 Module 的 Base 类
Base = declarative_base(engine)
# 创建会话类
Session = sessionmaker(engine)
# 第六步：测试连接


if __name__=='__main__':
    connection = engine.connect()
    # 返回(1,)证明连接成功
    result = connection.execute('select 1') # (1,)
    print(result.fetchone())