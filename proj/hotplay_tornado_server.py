# -*-coding=utf-8-*-


from __future__ import absolute_import

import sys

import os

import tornado.web

import tornado.ioloop

import tornado.httpserver

from celery.execute import send_task

from hotplay_task import do_init_catchup, do_catchup

# reload(sys)

# sys.setdefaultencoding('utf-8')

TORNADO_SERVER_PORT = 8000


class InitCatchupHandler(tornado.web.RequestHandler):

    def get(self, path):

        # user_name = self.get_argument("user_name", None)

        album_id = self.get_argument("id", None)

        # album_name = self.get_argument("album_name", None)
        #
        # channel_name = self.get_argument("channel_name", None)

        # print("request user_name+album_id+album_name+channel_name:%s+%s_%s+%s" % (
        # user_name, album_id, album_name, channel_name))
        print("request user_name+album_id+album_name+channel_name:%s" % album_id)

        if album_id == '0':
            self.write('test tornado server init catch up handler. sucess. just return\n')
            return
        try:
            self.write("0")
            # do_init_catchup.delay(user_name, album_id, album_name, channel_name)
            do_init_catchup.delay(album_id)
        except Exception as e:
            print(e)
            self.write("-1")
        # self.write("not found")
        return


class DoCatchupHandler(tornado.web.RequestHandler):

    def get(self, path):

        hotplay_id = self.get_argument("hotplay_id", None)

        start_dt = self.get_argument("start_dt", None)

        end_dt = self.get_argument("end_dt", None)

        print("request hotplay_id+start_dt+end_dt:%s+%s+%s" % (hotplay_id, start_dt, end_dt))

        if hotplay_id == '0':
            self.write('test tornado server catch up handler. sucess. just return\n')
            return
        try:
            self.write("0")

            do_catchup.delay(hotplay_id, start_dt, end_dt)
        except:

            self.write("-1")


class DoCatchupJYHandler(tornado.web.RequestHandler):

    def get(self, path):
        hotplay_id = self.get_argument("hotplay_id", None)

        start_dt = self.get_argument("start_dt", '2021-09-01')

        end_dt = self.get_argument("end_dt", '2021-09-02')

        print("request jy hotplay_id+start_dt+end_dt:%s+%s+%s" % (hotplay_id, start_dt, end_dt))

        # if hotplay_id == '0':

        #    self.write('test tornado server catch up handler. sucess. just return\n')

        #    return

        send_task('proj_tasks.test1', args=[hotplay_id, start_dt, end_dt],
                  queue='hotplay_jy_queue')  # tasks.test1是server2上celery任务函数的file_name.func_name


# file_name是任务函数所在文件相对于celery worker的路径


# try:


#    self.write("0")


#    do_catchup.delay(hotplay_id, start_dt, end_dt)


# except:


#    self.write("-1")


application = tornado.web.Application(

    [

        (r"/init_catchup/(.*)", InitCatchupHandler),

        (r"/do_catchup/(.*)", DoCatchupHandler),

        (r"/do_catchup_jy/(.*)", DoCatchupJYHandler),

    ],

    template_path="template", static_path="static"

)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)

    http_server.listen(TORNADO_SERVER_PORT)

    tornado.ioloop.IOLoop.instance().start()




