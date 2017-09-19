import arrow
from huey import crontab
from user_model.rules import *
from huey.contrib.djhuey import periodic_task, task

"""

Scheduler

"""


@periodic_task(crontab(hour='*/1'))
def runupkeep():
    """
    check every hour if the time is 04:00 in hawaii
    :return:
    """
    utc = arrow.utcnow().to("US/Hawaii")  # get time in UTC
    if utc.format("HH:mm") == "4:00":  # is the time 4:00?
        upkeep()  # run upkeep program
