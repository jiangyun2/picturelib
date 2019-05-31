#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
from models.auth import User
from models.db import Session
from sqlalchemy import exists


def isexists(username):
    db_session = Session()
    # 查询满足条件的项目是否存在
    exist = db_session.query(exists().where(User.username == username)).scalar()
    db_session.close()
    return exist


def add_user(sign):
    db_session = Session()
    # 添加用户到数据库
    sign['password'] = hashlib.md5(sign['password1'].encode()).hexdigest()
    adduser = User(username=sign['username'], password=sign['password'], email=sign['email'])
    db_session.add(adduser)
    db_session.commit()
    db_session.close()


def verify(login):
    db_session = Session()
    sql_password = db_session .query(User).filter(User.username == login['username']).first().password
    db_session.close()
    return sql_password == hashlib.md5(login['password'].encode()).hexdigest()

def updatepassd(update):
    db_session = Session()
    # 更新密码
    update['newpassword'] = hashlib.md5(update['password2'].encode()).hexdigest()
    db_session.query(User).filter(User.username == update['username']).update({User.password: update['newpassword']})
    db_session.commit()
    db_session.close()
