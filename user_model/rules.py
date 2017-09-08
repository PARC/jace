import random
from communications import outgoing
from communications.outgoing import change_condition
from user_model.models import User
from celery import Celery




def change_time_intervention(user, intervention):
    """

    :param user: user object
    :param intervention: which intervention you want to change
    :posts: value to app
    """
    if user.time_to_change():
        decision = {"user": user, intervention: random.choice([True, False])}
        outgoing.change_condition(decision)
        change_condition(studyId=user.studyId, attribute="settings.{}".format(intervention), value=random.choice(["yes",
                                                                                                                  "no"]))


def change_for_miss(user):
    """
    activates if user.days_since_last reports greater than 3
    :param user:
    :return:
    """
    if (user.Days_since_start - user.Last_day_reported) > 3:
        decision = {"user": user, "SC": random.choice([True, False])}
        outgoing.question_to_server()


def upkeep(user):
    """

    :param user: user to change
    :return:
    """

    for user in User.objects.all():
        user.Days_since_start += 1
        change_time_intervention(user, "SelfAffirmation")
        change_time_intervention(user, "implementationIntention")
        change_time_intervention(user, "Control")
        change_for_miss(user)
