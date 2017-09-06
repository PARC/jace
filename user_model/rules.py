
from communications import outgoing
import random
from communications.outgoing import change_condition


def change_time_intervention(user,intervention):
    """

    :param user: user object
    :param intervention: which intervention you want to change
    :posts: value to app
    """
    if user.time_to_change():
        decision = {"user":user,intervention:random.choice([True,False])}
        outgoing.change_condition(decision)
        change_condition(studyId=user.studyId,attribute= "settings.{}".format(intervention), value=random.choice(["yes",
                                                                                                       "no"]))


def change_for_miss(user):
    """
    activates if user.days_since_last reports greater than 3
    :param user:
    :return:
    """
    if user.days_since_last_report > 3:
        decision = {"user": user, "SC": random.choice([True, False])}
        outgoing.question_to_server()

def upkeep(user):
        #todo get most recent post, if most recent post is greater than 1 day ago, update
        pass