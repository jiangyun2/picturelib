#!/usr/bin/python
# -*- coding: utf-8 -*
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('home.html')