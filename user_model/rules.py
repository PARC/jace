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
    if user.Days_since_activty_start % 14 == 0:
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
    if (user.Days_since_start - user.Last_day_reported) > 3:
        if user.Days_since_activty_start + 3 % 14 >= 3:
            change_condition(studyId=user.studyId, attribute="settings.{}".format("selfCompassion"),
                             value=random.choice(["yes", "no"]))
        else:
            pass


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
        interventionList = ["SelfAffirmation", "implementationIntention", "Control"]
        change_time_intervention(user, interventionList)  # check self aff
        change_for_miss(user)  # check for miss.
        user.Days_since_start += 1  # update the day
        user.Days_since_activty_start += 1
        user.save()


if __name__ == "__main__":
    upkeep()
    print("Running")
