import random
from communications.outgoing import change_condition, question_to_server
from user_model.models import User

#####################
"""
Change Intervention on a regular schedule
"""
#######################
def change_time_intervention(user, intervention):
    """

    :param user: user object
    :param intervention: which intervention you want to change
    :posts: value to app
    """
    if user.time_to_change():
        decision = {"user": user, intervention: random.choice([True, False])}
        change_condition(decision)
        change_condition(studyId=user.studyId, attribute="settings.{}".format(intervention), value=random.choice(["yes",
                                                                                                                  "no"]))
##########################
"Change for a Missed day Rule Self Compassion"
#########################

def change_for_miss(user):
    """
    activates if user.days_since_last reports greater than 3
    :param user:
    :return:
    """
    if (user.Days_since_start - user.Last_day_reported) > 3:
        decision = {"user": user, "SC": random.choice([True, False])}
        question_to_server()

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
        user.Days_since_start += 1  # update the day
        change_time_intervention(user, "SelfAffirmation")  # check self aff
        change_time_intervention(user, "implementationIntention")  # check implementation intention
        change_time_intervention(user, "Control")  # check control
        change_for_miss(user)  # check for miss.

if __name__ == "__main__":
    upkeep()
    print("Running")
