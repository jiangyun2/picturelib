#!/usr/bin/python
# -*- coding: utf-8 -*

import tornado.ioloop
import tornado.web
from tornado.options import define,options

# 定义端口信息
define('port', default=8888, type=int, help="Listening port")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
        # debug模式下，检测到代码改变将自动重启tornado
        debug=True,
    )


if __name__ == "__main__":
    app = make_app()
    # 命令行参数转换
    tornado.options.parse_command_line()
    # 控制台输出port
    print("Server start on port {}".format(options.port))
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()



