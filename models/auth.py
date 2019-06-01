#!/usr/bin/python
# -*- coding: utf-8 -*


from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(50))
    email = Column(String(80))
    creatime = Column(DateTime, default=datetime.now)


    def __repr__(self):
        return "<User:#{}-{}".format(self.id,self.username)


class Picurl(Base):
    __tablename__ = 'pics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image_url = Column(String(200))
    thumb_url = Column(String(200))
    user = relationship('User', backref='pics', uselist=False, cascade='all')

    def __repr__(self):
        return "<Picurl:#{}".format(self.id)


if __name__ == '__main__':
    # 把创建好的Module映射到数据库中
    Base.metadata.create_all()
