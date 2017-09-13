import arrow
from huey import crontab
from user_model.rules import *
from huey.contrib.djhuey import periodic_task, task

"""

Scheduler

"""
@periodic_task(crontab(minute='*/5'))
def runupkeep():
    utc = arrow.utcnow()
    currTime = utc.to("US/Hawaii")
    if currTime.format("HH:mm") == ("12:03"):
        upkeep()

