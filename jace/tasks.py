import arrow
from datetime import datetime
from huey import crontab
from .config import huey
from user_model.rules import *
utc = arrow.utcnow()
local = utc.to("US/Hawaii")
time = arrow.get("2017-09-12T03:00:00.865001-10:00")

print(time.humanize())


currTime = utc.to("US/Pacific")
print(currTime.format("HH"))
print(time.format("HH:mm"))


@huey.periodic_task(crontab(minute='0', hour='3'))
def upkeep():
    upkeep()

if time.format("HH:mm") == "03:00":
    print("Hello")

