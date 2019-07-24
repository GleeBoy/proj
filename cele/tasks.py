# -*- coding: utf-8 -*-
from celery import Celery

app = Celery('tasks', backend='redis://localhost:6379/2', broker='redis://localhost:6379/1')

@app.task
def add(x, y):
    return x + y

