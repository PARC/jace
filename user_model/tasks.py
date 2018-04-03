'''
*************************************************************************
*
*  © [2018] PARC Inc., A Xerox Company
*  All Rights Reserved.
*
* NOTICE:  All information contained herein is, and remains
* the property of Xerox Corporation.
* The intellectual and technical concepts contained
* herein are proprietary to PARC Inc. and Xerox Corp.,
* and may be covered by U.S. and Foreign Patents,
* patents in process, and may be protected by copyright law.
* This file is subject to the terms and conditions defined in
* file 'LICENSE.md', which is part of this source code package.
*
**************************************************************************
'''


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
    if utc.format("HH:mm") == "4:00":  # is the time 4:00 in hawaii?
        upkeep()  # run upkeep program
