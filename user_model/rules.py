
from communications import outgoing
import random

def change_time_intervention(user,intervention):
    if user.time_to_change():
        decision = {"user":user,intervention:random.choice([True,False])}
        outgoing.change_condition(decision)
def change_for_miss(user):
    if user.days_since_last_report > 3:
        decision = {"user": user, "SC": random.choice([True, False])}
        outgoing.question_to_server()
