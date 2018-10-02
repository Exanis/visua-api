from celery import shared_task
from requests import get, exceptions
from django.utils import timezone
from pipeline import models


@shared_task
def refresh_runners_status():
    runners = models.Runner.objects.all()
    for runner in runners:
        try:
            status = get(runner.addr + '/ping', headers={
                'X-Auth-Token': runner.key
            })
            if status.status_code != 204:
                runner.alive = False
            else:
                runner.alive = True
                runner.last_update = timezone.now()
        except exceptions.RequestException:
            runner.alive = False
        runner.save()
