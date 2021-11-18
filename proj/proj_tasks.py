# -*-coding=utf-8-*-


from __future__ import absolute_import

from celery import Celery

from kombu import Queue

app = Celery("test",

             broker="redis://192.168.56.102:6379/1",

             include=['proj_tasks']

             )

app.conf.update(

    CELERY_DEFAULT_QUEUE='hotplay_sh_default_queue',  # 可省略，但不能和server1的配置不一样

    CELERY_QUEUES=(Queue('hotplay_jy_queue'),),

)


@app.task()
def test1(hotplay_id, start_dt, end_dt):  # 注意，名字要和tornado_server中send_task()函数用的func_name名字一样
    print('hotplay_id is %s, stat from %s to %s' % (hotplay_id, start_dt, end_dt))



