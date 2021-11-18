# -*-coding=utf-8-*-
from __future__ import absolute_import

import sys

import os

import hashlib

import time

import subprocess

from cele import app

# reload(sys)

# sys.setdefaultencoding('utf-8')

sys.path.append(os.path.join(os.path.dirname(__file__), "./"))

HOTPLAY_CATCHUP_DIR = '/home/geiliboy/projects/newproject/proj'


@app.task(bind=True)
def do_init_catchup(self, album_id):
    print(self)
    print('start to init catch up of user  album %s in channel' % (album_id))

    # job_args = 'source %s/init_catch_up.sh %s > ./logs/%s_%s.log' % (
    # HOTPLAY_CATCHUP_DIR, album_id)
    # print('job_args:', job_args)
    # P = subprocess.Popen(job_args, shell=True)
    # rt_code = P.wait()
    # if rt_code == 0:
    #     print('job success...')
    # else:
    #     print('job error:%d' % (rt_code))

    #    print 'job error:%d, will retry in 5 min'%(rt_code)

    #    raise self.retry(countdown=300)


@app.task(bind=True)
def do_catchup(self, hotplay_id, start_dt, end_dt):
    print('start to catch up of %s:%s-%s' % (hotplay_id, start_dt, end_dt))
    job_args = 'source %s/catch_up_all_run.sh %s %s %s > ./logs/%s.log 2>&1' % (
    HOTPLAY_CATCHUP_DIR, hotplay_id, start_dt, end_dt, hotplay_id)

    print('job_args:', job_args)

    # P = subprocess.Popen(job_args, shell=True)
    # rt_code = P.wait()
    # if rt_code == 0:
    #     print('job success...')
    #
    # else:
    #     print('job error:%d' % (rt_code))
    #
    #    print 'job error:%d, will retry in 5 min'%(rt_code)
    #
    #    raise self.retry(countdown=300)
