import time, os, subprocess
from django.conf import settings as s
from celery import task, current_task

if s.ROLE == "production_worker": #standalone worker?
  @task()
  def calculateModel(result_id):
    rq = current_task.request
    retval = subprocess.call(['../run_worker_glass',
                              '%06i' % result_id])
    return
    
else:  #worker running on server machine
  @task()
  def calculateModel(result_id):
    rq = current_task.request
    os.chdir(s.WORKER_DIR_FULL)
    retval = subprocess.call(['%s/run_glass' % s.WORKER_DIR_FULL,
                              '../tmp_media/%06i/cfg.gls' % result_id])
    return