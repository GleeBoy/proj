from django.shortcuts import render
from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from django_apscheduler.models import DjangoJob, DjangoJobExecution
import time

# Create your views here.

import logging

logging.basicConfig(
    level=20,
    filename='testSchedule.log',
    format="%(levelname)-5s %(asctime)s %(message)s"
)

executors = {
    'default': ThreadPoolExecutor(8),
    'processpool': ProcessPoolExecutor(2)
}
scheduler = BackgroundScheduler(executors=executors)
scheduler.add_jobstore(DjangoJobStore(), "default")


def test_job():
    print('start!')
    logging.info('test!')
    time.sleep(4)
    print("I'm a test job!")
    # raise ValueError("Olala!")


# scheduler.start()
# print("Scheduler started!")


def schecount(request):
    print(len(scheduler.get_jobs()), scheduler.get_jobs())
    scheduler.remove_all_jobs('default')
    print(len(scheduler.get_jobs()))
    return HttpResponse('tets')


def addjob(request):
    print(len(scheduler.get_jobs()))
    addjob = scheduler.add_job(test_job, 'interval', seconds=10)
    print(len(scheduler.get_jobs()))
    return HttpResponse('tets')


def jobdetails(request):
    jobList = scheduler.get_jobs()
    print(dir(jobList[0]))
    return HttpResponse(str(dir(jobList[0])))


def getJob(request):
    # jobID = request.GET.get('jobID', '')
    jobs = DjangoJob.objects.all()
    jobExectList = []
    for job in jobs:
        jobExectList.append(job.djangojobexecution_set.all()[0])
    return HttpResponse(str(jobExectList))
