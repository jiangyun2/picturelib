#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
from models.auth import User, Picurl
from sqlalchemy import exists


class Sqloperation():
    '''
    数据库操作
    '''
    def __init__(self, db_session):
        self.db_session = db_session

    def isexists(self, username):
        # 查询满足条件的项目是否存在
        exist = self.db_session.query(exists().where(User.username == username)).scalar()
        return exist

    def hsah_password(self, password):
        return hashlib.md5(password.encode()).hexdigest()

    def add_user(self, sign):
        # 添加用户到数据库
        sign['password'] = self.hsah_password(sign['password1'])
        adduser = User(username=sign['username'], password=sign['password'], email=sign['email'])
        self.db_session.add(adduser)
        self.db_session.commit()

    def get_user_byusername(self, username):
        return self.db_session .query(User).filter(User.username == username).first()

    def verify(self, login):
        sql_password = self.get_user_byusername(login['username']).password
        return sql_password == self.hsah_password(login['password'])

    def updatepassd(self, update):
        # 更新密码
        update['newpassword'] = self.hsah_password(update['password2'])
        self.db_session.query(User).filter(User.username == update['username']).update({User.password: update['newpassword']})
        self.db_session.commit()

    def save_picurl(self, username, img_url, thumb_url):
        user_id = self.get_user_byusername(username).id
        # 添加用户到数据库
        addpicurl = Picurl(user_id=user_id,
                           image_url=img_url,
                           thumb_url=thumb_url)
        self.db_session.add(addpicurl)
        self.db_session.flush()
        self.db_session.commit()
        pic_id = addpicurl.id
        return pic_id

    def get_pic(self, pic_id):
        pic = self.db_session.query(Picurl).filter(Picurl.id == pic_id).first()
        return pic

    def get_all_pic(self):
        pics = self.db_session.query(Picurl).all()
        return pics







