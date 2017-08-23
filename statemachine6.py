import os
import random

import redis
from durable.lang import *

from communications.outgoing import *

with ruleset('coach'):


    @when_all(m.time_to_change())
    def determine_con():
        """
        Will activate if it is time for the user to change conditions based on a two week interval
        :return:
        """
        #todo send message to API to turn on each condition randomly
        question_to_server(
            '{"studyId":"shszxqlpkw89s98f6","attribute":"settings.selfAffirmation", "value":"{}"}'.format(
                random.choice(["yes", "no"])))
        question_to_server(
            '{"studyId":"shszxqlpkw89s98f6","attribute":"settings.implementationIntention", "value":"y{}"}'.format(
                random.choice(["yes", "no"])))
    @when_all(m.NO_responce_number >=3)
    def turn_on_reminders():
        """
        Will activate if the number of lack responces is greater than 3.
        :return:
        """
        #todo send message to API to turn on reminders
        question_to_server(question_to_server(
            '{"studyId":"shszxqlpkw89s98f6","attribute":"settings.selfCompassion", "value":"y{}"}'.format(
                random.choice(["yes", "no"]))))




    @when_start
    def start(host):
        for i in range(32):
            host.post('coach',{"Rx_setup":False})

if __name__ == '__main__':
    """
    This runs the program. Perhaps. copy over to API to start it for each case?
    """
    redis.StrictRedis(port=os.environ['REDIS'].split(':')[1]).flushall()
    run_all([{'REDIS': os.environ['REDIS'].split(':')[0], 'port': os.environ['REDIS'].split(':')[1]}],
            port=os.environ['REDIS'].split(':')[1]);
