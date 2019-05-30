#!/usr/bin/python
# -*- coding: utf-8 -*


from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from models.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(50))
    email = Column(String(80))
    creatime = Column(DateTime, default=datetime.now)


    def __repr__(self):
        return "<User:#{}-{}".format(self.id,self.username)


if __name__ == '__main__':
    # 把创建好的Module映射到数据库中
    Base.metadata.create_all()
