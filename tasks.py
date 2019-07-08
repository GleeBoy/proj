# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/1')

@app.task
def add():
    print('add')
    return 2

