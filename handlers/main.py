#!/usr/bin/python
# -*- coding: utf-8 -*


import logging
import tornado.web
from pycket.session import SessionMixin
from models.sqloperate import isexists, add_user, verify, updatepassd, save_picurl
from models.savepic import SavePicture

logging.basicConfig(level=logging.DEBUG)

class BaseHandler(tornado.web.RequestHandler,SessionMixin):
    def get_current_user(self):
        # 使用self.session.get获取cookie值
        return self.session.get("mycookie")


class MainHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('home.html', user=self.current_user)


class RegisterHandler(BaseHandler):
    def get(self):
        self.render('register.html', user=self.current_user)

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
            logging.info("请完整填写注册信息")
            self.write("请完整填写注册信息")
            self.render('register.html', user=self.current_user)
            return
        elif sign['password1'] != sign['password2']:
            logging.info("两次输入的密码不相同")
            self.write("两次输入的密码不相同")
            self.render('register.html', user=self.current_user)
            return
        elif isexists(sign['username']):
            logging.info("用户名已经被注册")
            self.write("用户名已经被注册")
            self.render('register.html', user=self.current_user)
            return
        else:
            # 将用户数据添加到数据库
            add_user(sign)
            logging.info("注册成功")


class LoginHandler(BaseHandler):
    def get(self):
        next = self.get_argument("next", "")
        self.render("login.html", user=self.current_user, next=next)


    def post(self):
        login = {
            'username': self.get_argument("username", ""),
            'password': self.get_argument("password", ""),
            'next': self.get_argument("next", ""),
        }
        if not login['username'].strip() and login['password'].strip():
            logging.info("登录信息不能为空")
            self.write("登录信息不能为空")
            self.render("login.html", user=self.current_user)
            return
        # 验证账号密码
        if verify(login):
            logging.info("通过验证")
            # set cookies
            self.session.set('mycookie', login['username'])
            logging.info(login['next'])
            if login['next']:
                self.redirect(login['next'])
            else:
                self.redirect("/")
        else:
            logging.info("账号或者密码错误")
            self.write("账号或者密码错误")
            self.render("login.html", user=self.current_user)


class UpdatepasswordHandler(BaseHandler):
    def get(self):
        self.render("updatepassword.html", user=self.current_user)

    def post(self):
        update = {
            'username': self.get_argument("username", ""),
            'password': self.get_argument("password1", ""),
            'password2': self.get_argument("password2", ""),
        }
        if verify(update):
            logging.info("验证通过")
            # 更新密码
            updatepassd(update)
            logging.info("密码修改完成")
            if update['username'] == self.current_user:
                self.redirect('/logout')
            else:
                self.redirect('/login')
        else:
            logging.info("账号或者密码错误")
            self.write("账号或者密码错误")
            self.render("updatepassword.html", user=self.current_user)


class LogoutHandler(BaseHandler):
    def get(self):
        logging.info("退出登录")
        self.write('退出登录！')
        self.session.set('mycookie', None)
        self.redirect("/login")


class PicuploadHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("picupload.html", user=self.current_user)

    def post(self):
        # 获取上传图片的信息
        pic = {}
        pics = self.request.files.get('picture', [])
        logging.info(pics)
        if pics:
            pic = pics[0]
        else:
            logging.info("上传内容为空")
            self.write("上传内容为空")
            self.render("picupload.html", user=self.current_user)
            return
        # 保存图片
        sp = SavePicture(pic)
        img_url = sp.save_image()
        thumb_url = sp.save_thumb()
        logging.info(img_url)
        logging.info(thumb_url)
        # 将图片url写入数据库
        picid = save_picurl(self.current_user, img_url, thumb_url)
        logging.info(picid)




