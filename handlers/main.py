#!/usr/bin/python
# -*- coding: utf-8 -*

import hashlib
import tornado.web
from models.sqloperate import isexists, add_user

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')

    def post(self):
        sign = {
            'username':self.get_argument("username", ""),
            'email':self.get_argument("email", ""),
            'password1':self.get_argument("password1", ""),
            'password2':self.get_argument("password2", ""),
        }
        if not (sign['username'].strip() and
                sign['email'].strip() and
                sign['password1'].strip() and
                sign['password2'].strip()):
            print('请完整填写注册信息')
            self.write("请完整填写注册信息")
            self.render('register.html')
            return
        elif sign['password1'] != sign['password2']:
            print('两次输入的密码不相同')
            self.write("两次输入的密码不相同")
            self.render('register.html')
            return
        elif isexists(sign['username']):
            print("用户名已经被注册")
            self.write("用户名已经被注册")
            self.render('register.html')
            return
        else:
            # 对密码进行md5加密
            sign['password'] = hashlib.md5(sign['password1'].encode()).hexdigest()
            print(sign)
            # 将用户数据添加到数据库
            add_user(sign)
            print('注册成功')

