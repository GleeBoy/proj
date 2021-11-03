# import os
#
# from celery import Celery
#
# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')
#
# app = Celery('proj')
#
# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
#
# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()    # 发现所有tasks.py
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# -*-coding=utf-8-*-


from __future__ import absolute_import

from celery import Celery

from kombu import Queue

app = Celery("cele",
             broker="redis://192.168.56.102:6379/1",
             include=['hotplay_task']
             )

app.conf.update(
    CELERY_DEFAULT_QUEUE='hotplay_sh_default_queue',
    # CELERY_QUEUES = (Queue('hotplay_jy_queue'),),  #该队列是给server2用的，并不需要在这里申明

)



