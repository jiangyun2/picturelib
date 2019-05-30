#!/usr/bin/python
# -*- coding: utf-8 -*
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html')

    def post(self):
        username = self.get_argument("username", "")
        email = self.get_argument("email", "")
        password1 = self.get_argument("password1", "")
        password2 = self.get_argument("password2", "")
        if not (username.strip() and email.strip() and password1.strip() and password2.strip()):
            print('请完整填写注册信息')
            self.write("请完整填写注册信息")
            self.render('register.html')
            return
        else:
            print(username,email, password1, password2)
            # 判断账号是否存在，是则返回错误信息，否将账号密码写入数据库，完成注册。

