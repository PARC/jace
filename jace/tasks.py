import arrow
from datetime import datetime
from huey import crontab
from user_model.rules import *
from huey.contrib.djhuey import periodic_task, task

"""

Scheduler

"""


utc = arrow.utcnow()
local = utc.to("US/Hawaii")
time = arrow.get("2017-09-12T03:00:00.865001-10:00")




print(time.humanize())


currTime = utc.to("US/Pacific")
print(currTime.format("HH"))
print(time.format("HH:mm"))



@periodic_task(crontab(minute='0', hour='3'))
def runupkeep():
    utc = arrow.utcnow()
    currTime = utc.to("US/Hawaii")
    if currTime.format("HH:mm") == ("12:03"):
        upkeep()

