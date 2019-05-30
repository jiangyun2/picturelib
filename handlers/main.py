#!/usr/bin/python
# -*- coding: utf-8 -*

import tornado.web
from models.sqloperate import isexists, add_user, verify


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
            print(sign)
            # 将用户数据添加到数据库
            add_user(sign)
            print('注册成功')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        login = {
            'username': self.get_argument("username", ""),
            'password': self.get_argument("password", ""),
        }
        print(login)
        if not login['username'].strip() and login['password'].strip():
            print("登录信息不能为空")
            self.write("登录信息不能为空")
            self.render("login.html")
        # 验证账号密码
        if verify(login):
            print("通过验证")
        else:
            print("账号或者密码错误")
            self.write("账号或者密码错误")
            self.render("login.html")







