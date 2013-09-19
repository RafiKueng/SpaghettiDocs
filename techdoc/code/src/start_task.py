from lmt.tasks import calculateModel
from celery.result import AsyncResult

@csrf_exempt
def getSimulationJSON(request, result_id):
  # ...
  res = ModellingResult.objects.get(id=result_id)
  # ...

  # set time limits
  dt = 60*30 # task has 30min till it gets revoked
  expire = 60 # task gets canceled after 60s in queue
  
  task = calculateModel.apply_async(args=(result_id,), timeout=dt,
                                    expires=expire)
  res.is_rendered = False
  res.task_id = task.task_id
  res.rendered_last = now();
  res.save()
