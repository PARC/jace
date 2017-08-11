import redis
from durable.lang import *
import random
import question_builder2 as QB2
from django.db import models
import time
import os


base_instruction = "Research shows that  having a positive self-image is important to making healthy lifestyle changes"
selfaff_eat2 = "I’m going to ask you to use a tool called a {kind} for the eat slower program"
selfaff_eat3 = "Here’s how it works. A  {description} "
selfaff_eat4 = "Use a {kind} in situations that diminishes your motivation or threatens your self-image"
selfaff_eat5 = 'It helps to make tiny plans to do your {kind} using statements of the form: “IF situation' \
           ' X is encountered THEN I will do a {kind}"'
selfaff_eat6 = 'The “IF” part is a specific situation that  diminishes your motivation or threatens your self-image' \
               ' The “THEN” part is  a specific {kind}'
quest_list = [base_instruction,selfaff_eat2,selfaff_eat3,selfaff_eat4,selfaff_eat5,selfaff_eat6]


with ruleset('coach'):


    @when_all(m.time_to_change())
    def determine_con():
        """
        Will activate if it is time for the user to change conditions based on a two week interval
        :return:
        """
        #todo send message to API to turn on each condition randomly
        pass
    @when_all(m.NO_responce_number >=3)
    def turn_on_reminders():
        """
        Will activate if the number of lack responces is greater than 3.
        :return:
        """
        #todo send message to API to turn on reminders
        pass




    @when_start
    def start(host):
        for i in range(32):
            host.post('coach',{"Rx_setup":False})

if __name__ == '__main__':
    redis.StrictRedis(port=os.environ['REDIS'].split(':')[1]).flushall()
    run_all([{'REDIS': os.environ['REDIS'].split(':')[0], 'port': os.environ['REDIS'].split(':')[1]}], port=os.environ['REDIS'].split(':')[1]);
