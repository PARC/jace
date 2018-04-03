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

import random

from communications.outgoing import change_condition
from user_model.models import User

#####################
"""
Change Intervention on a regular schedule
"""


#######################
def change_time_intervention(user, interventionList):
    """

    :param user: user object
    :param intervention: which intervention you want to change
    :posts: value to app
    """
    print(user.Days_since_activty_start % 14 == 0)
    if user.Days_since_activty_start % 14 == 0:  # checks if the day since activity starts is modulo to the day 14 for
        #  two week changes
        for intervention in interventionList:
            change_condition(studyId=user.studyId, attribute="settings.{}".format(intervention),
                             value=random.choice(["yes", "no"]))
        user.Days_since_activty_start = 0
        user.save()


##########################
"Change for a Missed day Rule Self Compassion"


#########################

def change_for_miss(user):
    """
    activates if user.days_since_last reports greater than 3
    :param user:
    :return:
    """

    print(user.Days_since_start - user.Last_day_reported)
    if (user.Days_since_start - user.Last_day_reported) > 3:  # check if user missed 3 days by seeing if current day is
        # three days after the last report
        if user.Days_since_activty_start + 3 % 14 >= 3:  #Check if there are more than 3 days remaining in program
            change_condition(studyId=user.studyId, attribute="settings.{}".format("selfCompassion"),
                             value=random.choice(["yes", "no"]))
        else:  #Turn off intervention if there is a responce
            change_condition(studyId=user.studyId, attribute="settings.{}".format("selfCompassion"),
                             value="no")
            # question_to_server()


####################
"""
Upkeep
"""


#####################


def upkeep():
    """
    Upkeep updates each users day, and then calls all of the rules
    :param None
    :return:
    """

    for user in User.objects.all():
        interventionList = ["selfAffirmation", "implementationIntention", "controlCondition"]
        change_time_intervention(user, interventionList)  # check self aff
        change_for_miss(user)  # check for miss.
        user.Days_since_start += 1  # update the day
        user.Days_since_activty_start += 1
        user.save()


if __name__ == "__main__":
    upkeep()
    print("Running")

