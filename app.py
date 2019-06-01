#!/usr/bin/python
# -*- coding: utf-8 -*

import tornado.ioloop
import tornado.web
from tornado.options import define, options
from handlers import main
import utils.ui_modules,utils.ui_methods

# 定义端口信息
define('port', default=8888, type=int, help="Listening port")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", main.MainHandler),
            (r"/register", main.RegisterHandler),
            (r"/login", main.LoginHandler),
            (r"/updatepassword", main.UpdatepasswordHandler),
            (r"/logout", main.LogoutHandler),
            (r"/picupload", main.PicuploadHandler),
            (r"/picture", main.PictureHandler),
            # (?P < post_id >[0-9]+) 捕获输入的id值传入到pic_id中
            (r"/picture/(?P<pic_id>[0-9]+)", main.PicdetialHandler),
        ]
        settings = dict(
            # debug模式下，检测到代码改变将自动重启tornado
            debug=True,
            # 模板
            template_path='templates',
            # 静态文件
            static_path='statics',
            ui_modules=utils.ui_modules,
            ui_methods=utils.ui_methods,
            cookie_secret="ashdghsajgdhgasfdwqtehasdvnsav",
            login_url='/login',
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    # 'password': '',
                    'db_sessions': 5,  # redis db index
                    # 'db_notifications': 11,
                    'max_connections': 2 ** 30,
                },
                'cookies': {
                    'expires_days': 30,
                },
            }
        )
        # 继承父类的init，主要起作用的是父类的init
        super().__init__(handlers=handlers, **settings)


if __name__ == "__main__":
    app = Application()
    # 命令行参数转换
    tornado.options.parse_command_line()
    # 控制台输出port
    print("Server start on port {}".format(options.port))
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



